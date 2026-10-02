#!/usr/bin/env python3
"""Calcula el ritmo diario necesario para llegar al YPP antes de la fecha objetivo.

Uso:
    python3 herramientas/ritmo_ypp.py --horas 850 --subs 240
    python3 herramientas/ritmo_ypp.py --horas 850 --subs 240 --minutos-por-visita 22 --objetivo 2026-12-20

Los datos actuales se leen en YouTube Studio → Ingresos (horas públicas de los
últimos 365 días y suscriptores). Los minutos por visita son el «tiempo medio de
visualización» de los vídeos largos en Studio → Estadísticas.
"""

import argparse
from datetime import date

HORAS_YPP = 4000
SUBS_YPP = 1000


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--horas", type=float, required=True, help="horas públicas acumuladas (365 días)")
    p.add_argument("--subs", type=int, required=True, help="suscriptores actuales")
    p.add_argument("--minutos-por-visita", type=float, default=25.0, help="tiempo medio de visualización en vídeo largo (min)")
    p.add_argument("--objetivo", type=date.fromisoformat, default=date(2026, 12, 10), help="fecha para solicitar (AAAA-MM-DD)")
    p.add_argument("--hoy", type=date.fromisoformat, default=date.today(), help="fecha de la lectura (AAAA-MM-DD)")
    a = p.parse_args()

    dias = (a.objetivo - a.hoy).days
    faltan_horas = max(0.0, HORAS_YPP - a.horas)
    faltan_subs = max(0, SUBS_YPP - a.subs)

    print(f"Días hasta {a.objetivo}: {dias}")
    print(f"Horas: {a.horas:,.0f}/{HORAS_YPP:,} ({a.horas / HORAS_YPP:.0%}) · faltan {faltan_horas:,.0f}")
    print(f"Suscriptores: {a.subs:,}/{SUBS_YPP:,} ({a.subs / SUBS_YPP:.0%}) · faltan {faltan_subs:,}")

    if not faltan_horas and not faltan_subs:
        print("Requisitos cumplidos: solicita ya.")
        return
    if dias <= 0:
        print("La fecha objetivo ya ha pasado. Límite práctico: 20 de diciembre; después, apuntar a fan funding y 8.000 h.")
        return

    horas_dia = faltan_horas / dias
    visitas_dia = horas_dia * 60 / a.minutos_por_visita
    print(f"Ritmo necesario: {horas_dia:,.1f} h/día ≈ {visitas_dia:,.0f} visitas/día en vídeo largo "
          f"(a {a.minutos_por_visita:g} min por visita) y {faltan_subs / dias:,.1f} suscriptores/día")


if __name__ == "__main__":
    main()
