"""Control de riesgos: el filtro que nadie se salta.

Todo es aritmética determinista sobre datos/limites.json. Ningún agente
«opina» sobre si una operación pasa: la pasa o no la pasa esta función.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "datos"
REGISTRO = RAIZ / "registro"


def cargar(nombre: str) -> dict:
    return json.loads((DATOS / nombre).read_text(encoding="utf-8"))


def producto_de(simbolo: str) -> str:
    """SP500.DEC26 -> SP500 ; OIL.WTI.JAN27 -> OIL.WTI ; SP500 -> SP500."""
    contratos = cargar("contratos.json")
    if simbolo in contratos:
        return simbolo
    base = simbolo.rsplit(".", 1)[0]
    if base in contratos:
        return base
    raise ValueError(f"Contrato no reconocido: {simbolo}. Conocidos: "
                     + ", ".join(k for k in contratos if not k.startswith("_")))


@dataclass
class Operacion:
    simbolo: str            # símbolo de eToro con vencimiento, p. ej. SP500.DEC26
    direccion: str          # "largo" | "corto"
    contratos: int
    entrada: float
    stop: float
    ultimo_dia: str         # último día de negociación en eToro, AAAA-MM-DD
    tipo: str = "direccional"   # "direccional" | "cobertura"
    cartera_usd: float = 0.0    # solo cobertura: valor de la cartera cubierta
    beta: float = 1.0           # solo cobertura


def perdidas_de_hoy(hoy: date) -> tuple[float, int]:
    """(pérdida neta del día en USD como número positivo, stops seguidos)."""
    f = REGISTRO / "resultados.jsonl"
    if not f.exists():
        return 0.0, 0
    pnl, racha = 0.0, 0
    for linea in f.read_text(encoding="utf-8").splitlines():
        r = json.loads(linea)
        if r["fecha"] != hoy.isoformat():
            continue
        pnl += r["pnl_usd"]
        racha = racha + 1 if r["pnl_usd"] < 0 else 0
    return max(0.0, -pnl), racha


def evaluar(op: Operacion, hoy: date | None = None,
            limites: dict | None = None, margenes: dict | None = None) -> dict:
    hoy = hoy or date.today()
    lim = limites or cargar("limites.json")
    margenes = margenes or cargar("margenes.json")
    prod = producto_de(op.simbolo)
    spec = cargar("contratos.json")[prod]
    mult = spec["multiplicador"]
    capital = lim["capital_eur"] * lim["eurusd"]

    motivos: list[str] = []   # cualquiera de estos => NO APTO
    avisos: list[str] = []    # ámbar: pasa, pero Javier debe leerlo

    if op.direccion not in ("largo", "corto"):
        motivos.append("La dirección debe ser «largo» o «corto».")
    if op.contratos < 1 or int(op.contratos) != op.contratos:
        motivos.append("El tamaño debe ser un número entero de contratos, mínimo 1.")
    if op.entrada <= 0 or op.stop <= 0:
        motivos.append("Entrada y stop son obligatorios y positivos.")
    elif (op.direccion == "largo" and op.stop >= op.entrada) or \
         (op.direccion == "corto" and op.stop <= op.entrada):
        motivos.append("El stop está en el lado equivocado de la entrada.")
    for nombre, precio in (("entrada", op.entrada), ("stop", op.stop)):
        pasos = precio / spec["tick"]
        if abs(pasos - round(pasos)) > 1e-6:
            motivos.append(f"El precio de {nombre} ({precio}) no es múltiplo del tick ({spec['tick']}).")

    # Vencimiento: los contratos no se mantienen indefinidamente.
    dias_venc = (date.fromisoformat(op.ultimo_dia) - hoy).days
    if dias_venc < 0:
        motivos.append(f"El contrato dejó de negociarse el {op.ultimo_dia}.")
    elif dias_venc <= 5:
        avisos.append(f"Quedan {dias_venc} días para el último día de negociación ({op.ultimo_dia}): prever el roll.")

    # Margen: debe existir y estar fresco.
    m = margenes.get(prod, {})
    margen_u = m.get("margen_inicial_usd")
    if not margen_u or not m.get("fecha"):
        motivos.append(f"Falta el margen inicial de {prod} en datos/margenes.json.")
        margen_u = math.nan
    else:
        edad = (hoy - date.fromisoformat(m["fecha"])).days
        if edad > lim["margen_caducidad_dias"]:
            motivos.append(f"El margen de {prod} es del {m['fecha']} ({edad} días): hay que actualizarlo.")

    margen = margen_u * op.contratos
    nocional = op.entrada * mult * op.contratos
    riesgo = abs(op.entrada - op.stop) * mult * op.contratos
    r_margen = margen / capital
    r_riesgo = riesgo / capital

    tope_margen = (lim["margen_capital_max_cobertura"] if op.tipo == "cobertura"
                   else lim["margen_capital_max_direccional"])
    if r_margen > tope_margen:
        motivos.append(f"Margen/capital {r_margen:.1%} supera el límite del {tope_margen:.0%} ({op.tipo}).")
    if capital < lim["capital_minimo_veces_margen"] * margen:
        motivos.append(f"El capital no llega a {lim['capital_minimo_veces_margen']}× el margen inicial.")
    if r_riesgo > lim["riesgo_operacion_max"]:
        motivos.append(f"Riesgo por operación {r_riesgo:.2%} supera el máximo del {lim['riesgo_operacion_max']:.0%}.")
    elif r_riesgo > lim["riesgo_operacion_objetivo"]:
        avisos.append(f"Riesgo por operación {r_riesgo:.2%} por encima del objetivo del {lim['riesgo_operacion_objetivo']:.0%}.")

    perdido, racha = perdidas_de_hoy(hoy)
    tope_dia = lim["perdida_diaria_max"] * capital
    if racha >= lim["stops_seguidos_max"]:
        motivos.append(f"{racha} stops seguidos hoy: se acabó la sesión.")
    if perdido + riesgo > tope_dia:
        motivos.append(f"Pérdida del día ({perdido:.2f}) + riesgo de esta operación ({riesgo:.2f}) "
                       f"supera el límite diario de {tope_dia:.2f} USD.")

    if op.tipo == "cobertura":
        exposicion = op.cartera_usd * op.beta
        if op.direccion != "corto":
            motivos.append("Una cobertura de cartera se hace vendiendo futuros, no comprando.")
        if exposicion <= 0:
            motivos.append("Cobertura sin cartera documentada (valor y beta).")
        elif nocional > exposicion:
            motivos.append(f"El nocional vendido ({nocional:.0f}) supera la exposición cubierta "
                           f"({exposicion:.0f}): eso ya no es cobertura, aumenta el riesgo.")
    elif op.tipo != "direccional":
        motivos.append("El tipo debe ser «direccional» o «cobertura».")

    veredicto = "NO APTO" if motivos else ("APTO CON AVISOS" if avisos else "APTO")
    return {
        "veredicto": veredicto,
        "motivos": motivos,
        "avisos": avisos,
        "capital_usd": round(capital, 2),
        "margen_usd": None if math.isnan(margen) else round(margen, 2),
        "margen_capital": None if math.isnan(margen) else round(r_margen, 4),
        "nocional_usd": round(nocional, 2),
        "apalancamiento": round(nocional / capital, 2),
        "riesgo_usd": round(riesgo, 2),
        "riesgo_capital": round(r_riesgo, 4),
        "perdida_hoy_usd": round(perdido, 2),
        "limite_diario_usd": round(tope_dia, 2),
        "stops_seguidos_hoy": racha,
        "evaluado": datetime.now().isoformat(timespec="seconds"),
    }


def contratos_cobertura(cartera_usd: float, beta: float, precio: float, simbolo: str) -> dict:
    """Contratos enteros para cubrir una cartera. Redondea SIEMPRE hacia abajo:
    una cobertura nunca aumenta la exposición."""
    spec = cargar("contratos.json")[producto_de(simbolo)]
    nocional_u = precio * spec["multiplicador"]
    exposicion = cartera_usd * beta
    n = math.floor(exposicion / nocional_u)
    return {
        "exposicion_usd": round(exposicion, 2),
        "nocional_por_contrato_usd": round(nocional_u, 2),
        "contratos": n,
        "cubierto": round(n * nocional_u / exposicion, 4) if exposicion > 0 else 0.0,
        "sin_cubrir_usd": round(exposicion - n * nocional_u, 2),
    }
