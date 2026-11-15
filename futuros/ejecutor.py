"""Ejecutor eToro: el único módulo que habla con el bróker.

Cadena de seguridad, en este orden:
  1. Solo acepta un ticket emitido por Control de riesgos (huella intacta).
  2. El ticket caduca (ticket_validez_minutos) y solo se envía una vez.
  3. Vuelve a pasar el filtro de riesgos justo antes de enviar.
  4. Exige que Javier teclee el identificador del ticket (--confirmo).
  5. Por defecto opera en la cuenta DEMO. La cuenta real exige --real y
     además la variable de entorno ETORO_ENTORNO=real.

API pública de eToro (https://api-portal.etoro.com):
  POST /api/v2/trading/execution/[demo/]orders
  GET  /api/v2/trading/info/[demo/]orders:lookup
"""
from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from dataclasses import asdict
from datetime import datetime, timedelta

from .riesgo import REGISTRO, Operacion, cargar, evaluar

BASE = "https://public-api.etoro.com"
TICKETS = REGISTRO / "tickets"
ENVIOS = REGISTRO / "envios.jsonl"


class Rechazo(Exception):
    """La orden no se envía. El mensaje explica por qué."""


def _huella(cuerpo: dict) -> str:
    return hashlib.sha256(json.dumps(cuerpo, sort_keys=True).encode()).hexdigest()


def emitir_ticket(op: Operacion, tipo_orden: str = "limitIOC") -> dict:
    """Lo llama Control de riesgos. Solo emite si el veredicto no es NO APTO."""
    if tipo_orden not in ("limitIOC", "mkt"):
        raise Rechazo("tipo_orden debe ser limitIOC o mkt.")
    v = evaluar(op)
    if v["veredicto"] == "NO APTO":
        raise Rechazo("NO APTO: " + " | ".join(v["motivos"]))
    ahora = datetime.now()
    cuerpo = {
        "id": ahora.strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:6],
        "operacion": asdict(op),
        "tipo_orden": tipo_orden,
        "riesgo": v,
        "emitido": ahora.isoformat(timespec="seconds"),
        "caduca": (ahora + timedelta(minutes=cargar("limites.json")["ticket_validez_minutos"])
                   ).isoformat(timespec="seconds"),
    }
    ticket = {**cuerpo, "huella": _huella(cuerpo)}
    TICKETS.mkdir(parents=True, exist_ok=True)
    (TICKETS / f"{cuerpo['id']}.json").write_text(
        json.dumps(ticket, indent=2, ensure_ascii=False), encoding="utf-8")
    return ticket


def cuerpo_orden(ticket: dict) -> dict:
    """Traduce el ticket al cuerpo que espera eToro para un futuro real."""
    op = ticket["operacion"]
    orden = {
        "action": "open",
        "transaction": "buy" if op["direccion"] == "largo" else "sellShort",
        "symbol": op["simbolo"],
        "settlementType": "realFutures",
        "orderType": ticket["tipo_orden"],
        "contracts": op["contratos"],
        "stopLossRate": op["stop"],     # obligatorio en futuros reales
        "stopLossType": "fixed",
    }
    if ticket["tipo_orden"] == "limitIOC":
        # Se ejecuta a la entrada del ticket o mejor; si no, se cancela.
        # Así el riesgo aprobado es el riesgo real.
        orden["limitRate"] = op["entrada"]
    return orden


def _ya_enviado(ticket_id: str) -> bool:
    if not ENVIOS.exists():
        return False
    return any(json.loads(l)["ticket"] == ticket_id
               for l in ENVIOS.read_text(encoding="utf-8").splitlines())


def _http(metodo: str, url: str, cuerpo: dict | None, request_id: str) -> dict:
    api, usuario = os.environ.get("ETORO_API_KEY"), os.environ.get("ETORO_USER_KEY")
    if not api or not usuario:
        raise Rechazo("Faltan ETORO_API_KEY y ETORO_USER_KEY en el entorno.")
    req = urllib.request.Request(
        url, method=metodo,
        data=json.dumps(cuerpo).encode() if cuerpo is not None else None,
        headers={"x-api-key": api, "x-user-key": usuario, "x-request-id": request_id,
                 "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raise Rechazo(f"eToro respondió {e.code}: {e.read().decode(errors='replace')[:500]}")


def enviar(ticket_id: str, confirmo: str, real: bool = False,
           simular: bool = False, http=_http) -> dict:
    ruta = TICKETS / f"{ticket_id}.json"
    if not ruta.exists():
        raise Rechazo(f"No existe el ticket {ticket_id}. Solo Control de riesgos los emite.")
    ticket = json.loads(ruta.read_text(encoding="utf-8"))
    huella = ticket.pop("huella", None)
    if huella != _huella(ticket):
        raise Rechazo("El ticket ha sido modificado después de la aprobación de riesgos.")
    if confirmo != ticket["id"]:
        raise Rechazo("Falta el «sí» de Javier: --confirmo debe ser el identificador del ticket.")
    if datetime.now() > datetime.fromisoformat(ticket["caduca"]):
        raise Rechazo(f"Ticket caducado ({ticket['caduca']}). Vuelve a pasar por Control de riesgos.")
    if _ya_enviado(ticket["id"]):
        raise Rechazo("Este ticket ya se envió. Una aprobación, una orden.")
    v = evaluar(Operacion(**ticket["operacion"]))
    if v["veredicto"] == "NO APTO":
        raise Rechazo("Ya no pasa el filtro de riesgos: " + " | ".join(v["motivos"]))
    if real and os.environ.get("ETORO_ENTORNO") != "real":
        raise Rechazo("Cuenta real bloqueada: define ETORO_ENTORNO=real para habilitarla.")

    entorno = "real" if real else "demo"
    tramo = "" if real else "demo/"
    orden = cuerpo_orden(ticket)
    if simular:
        return {"simulacion": True, "entorno": entorno, "orden": orden}

    request_id = str(uuid.uuid4())
    # Se anota ANTES de enviar: si la respuesta se pierde, el request_id
    # (referenceId en eToro) es el único asidero para localizar la orden.
    apunte = {"ticket": ticket["id"], "entorno": entorno, "request_id": request_id,
              "orden": orden, "enviado": datetime.now().isoformat(timespec="seconds")}
    with ENVIOS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(apunte, ensure_ascii=False) + "\n")

    resp = http("POST", f"{BASE}/api/v2/trading/execution/{tramo}orders", orden, request_id)
    # 200 = aceptada para proceso, NO ejecutada. Hay que consultar el estado.
    estado = consultar(resp.get("orderId"), real=real, http=http)
    return {"entorno": entorno, "orden": orden, "respuesta": resp, "estado": estado}


ESTADOS = {1: "recibida", 2: "colocada", 3: "ejecutada", 4: "rechazada",
           5: "ejecutada parcialmente", 10: "rechazada tras ejecución parcial",
           11: "esperando mercado", 12: "pendiente de precio"}
EN_VUELO = {1, 2, 11, 12}


def consultar(order_id, real: bool = False, intentos: int = 5, http=_http) -> dict:
    tramo = "" if real else "demo/"
    url = (f"{BASE}/api/v2/trading/info/{tramo}orders:lookup?"
           + urllib.parse.urlencode({"orderId": order_id}))
    datos: dict = {}
    for i in range(intentos):
        datos = http("GET", url, None, str(uuid.uuid4()))
        sid = (datos.get("status") or {}).get("id")
        if sid not in EN_VUELO:
            break
        time.sleep(1 + i)
    sid = (datos.get("status") or {}).get("id")
    return {"estado": ESTADOS.get(sid, f"desconocido ({sid})"), "detalle": datos}
