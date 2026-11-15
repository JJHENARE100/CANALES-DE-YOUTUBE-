"""Uso: python -m futuros <orden> ...

  ficha      SIMBOLO                      ficha del contrato y margen vigente
  cobertura  --cartera --beta --precio    contratos enteros para cubrir
  riesgo     ...                          evalúa; con --ticket emite el ticket
  resultado  --pnl                        anota el resultado de una operación cerrada
  enviar     TICKET --confirmo TICKET     envía la orden a eToro (demo por defecto)
  estado     ORDER_ID                     consulta una orden ya enviada
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date

from . import ejecutor, riesgo


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="futuros", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="orden", required=True)

    a = s.add_parser("ficha"); a.add_argument("simbolo")

    a = s.add_parser("cobertura")
    a.add_argument("--simbolo", required=True)
    a.add_argument("--cartera", type=float, required=True, help="valor de la cartera en USD")
    a.add_argument("--beta", type=float, default=1.0)
    a.add_argument("--precio", type=float, required=True, help="precio del futuro")

    a = s.add_parser("riesgo")
    a.add_argument("--simbolo", required=True, help="símbolo eToro con vencimiento, p. ej. SP500.DEC26")
    a.add_argument("--direccion", required=True, choices=["largo", "corto"])
    a.add_argument("--contratos", type=int, required=True)
    a.add_argument("--entrada", type=float, required=True)
    a.add_argument("--stop", type=float, required=True)
    a.add_argument("--ultimo-dia", required=True, help="último día de negociación en eToro, AAAA-MM-DD")
    a.add_argument("--tipo", default="direccional", choices=["direccional", "cobertura"])
    a.add_argument("--cartera", type=float, default=0.0)
    a.add_argument("--beta", type=float, default=1.0)
    a.add_argument("--ticket", action="store_true", help="si pasa, emite el ticket para el Ejecutor")
    a.add_argument("--a-mercado", action="store_true", help="orden a mercado en vez de limitIOC")

    a = s.add_parser("resultado")
    a.add_argument("--pnl", type=float, required=True, help="resultado en USD (negativo si fue stop)")
    a.add_argument("--nota", default="")

    a = s.add_parser("enviar")
    a.add_argument("ticket")
    a.add_argument("--confirmo", required=True, help="identificador del ticket, tecleado por Javier")
    a.add_argument("--real", action="store_true")
    a.add_argument("--simular", action="store_true", help="muestra la orden sin enviarla")

    a = s.add_parser("estado")
    a.add_argument("order_id"); a.add_argument("--real", action="store_true")

    x = p.parse_args(argv)
    try:
        if x.orden == "ficha":
            prod = riesgo.producto_de(x.simbolo)
            out = {"producto": prod, **riesgo.cargar("contratos.json")[prod],
                   "margen": riesgo.cargar("margenes.json").get(prod)}
        elif x.orden == "cobertura":
            out = riesgo.contratos_cobertura(x.cartera, x.beta, x.precio, x.simbolo)
        elif x.orden == "riesgo":
            op = riesgo.Operacion(x.simbolo, x.direccion, x.contratos, x.entrada, x.stop,
                                  x.ultimo_dia, x.tipo, x.cartera, x.beta)
            if x.ticket:
                t = ejecutor.emitir_ticket(op, "mkt" if x.a_mercado else "limitIOC")
                out = {"ticket": t["id"], "caduca": t["caduca"], **t["riesgo"]}
            else:
                out = riesgo.evaluar(op)
        elif x.orden == "resultado":
            riesgo.REGISTRO.mkdir(exist_ok=True)
            apunte = {"fecha": date.today().isoformat(), "pnl_usd": x.pnl, "nota": x.nota}
            with (riesgo.REGISTRO / "resultados.jsonl").open("a", encoding="utf-8") as f:
                f.write(json.dumps(apunte, ensure_ascii=False) + "\n")
            perdido, racha = riesgo.perdidas_de_hoy(date.today())
            out = {**apunte, "perdida_hoy_usd": perdido, "stops_seguidos_hoy": racha}
        elif x.orden == "enviar":
            out = ejecutor.enviar(x.ticket, x.confirmo, real=x.real, simular=x.simular)
        else:
            out = ejecutor.consultar(x.order_id, real=x.real)
    except (ejecutor.Rechazo, ValueError) as e:
        print(json.dumps({"rechazado": str(e)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 1 if out.get("veredicto") == "NO APTO" else 0


if __name__ == "__main__":
    sys.exit(main())
