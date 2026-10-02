#!/usr/bin/env python3
"""Ritmo hacia el YPP, canal por canal, con proyección y avisos.

Dos formas de uso:

1) Lectura rápida de un canal (solo el dato de hoy):
    python3 herramientas/ritmo_ypp.py --horas 850 --subs 240 --minutos-por-visita 22

2) Con historial (recomendado). Un CSV con una fila por canal y día, con las cifras
   que da YouTube Studio → Ingresos (horas públicas válidas en 365 días y
   suscriptores):
       fecha,canal,horas,subs
       2026-10-20,historia,120,35
       2026-10-20,ciencia,310,90
       ...
    python3 herramientas/ritmo_ypp.py --historial docs/datos/ritmo.csv

Studio ya descuenta las horas que no cuentan: Shorts, anuncios y vídeos privados,
ocultos o borrados. Usa siempre esa cifra y no el «tiempo de visualización» total.

La proyección usa la velocidad media de los últimos 7, 14 y 28 días y la del
periodo completo. El crecimiento rara vez es lineal: mira sobre todo la de 7 días.
"""

import argparse
import csv
from collections import defaultdict
from datetime import date, timedelta

HORAS_YPP, HORAS_YPP_2027, SUBS_YPP = 4000, 8000, 1000
CAMBIO_2027 = date(2027, 2, 1)
DOBLAJE_MAX_MIN = 120


def velocidad(serie: list[tuple[date, float, float]], dias: int | None):
    """(horas/día, subs/día) entre el último punto y el de hace `dias` (None = todo)."""
    fin = serie[-1]
    if dias is None:
        ini = serie[0]
    else:
        previos = [p for p in serie if p[0] <= fin[0] - timedelta(days=dias)]
        if not previos:
            return None
        ini = previos[-1]
    d = (fin[0] - ini[0]).days
    if d <= 0:
        return None
    return (fin[1] - ini[1]) / d, (fin[2] - ini[2]) / d


def fecha_llegada(hoy: date, falta: float, por_dia: float) -> date | None:
    if falta <= 0:
        return hoy
    if por_dia <= 0:
        return None
    return hoy + timedelta(days=int(-(-falta // por_dia)))


def informe(canal: str, serie, args) -> None:
    hoy, horas, subs = serie[-1]
    faltan_h, faltan_s = max(0.0, HORAS_YPP - horas), max(0.0, SUBS_YPP - subs)
    print(f"\n=== {canal} · {hoy} ===")
    print(f"Horas válidas: {horas:,.0f}/{HORAS_YPP:,} ({horas / HORAS_YPP:.0%}) · Suscriptores: {subs:,.0f}/{SUBS_YPP:,} ({subs / SUBS_YPP:.0%})")
    if not faltan_h and not faltan_s:
        print("Cumple los umbrales: solicita ya (después de la auditoría del canal, plan §5).")
    dias_obj = (args.objetivo - hoy).days
    if dias_obj > 0 and (faltan_h or faltan_s):
        hd, sd = faltan_h / dias_obj, faltan_s / dias_obj
        print(f"Para solicitar el {args.objetivo}: {hd:,.1f} h/día ≈ {hd * 60 / args.minutos_por_visita:,.0f} visualizaciones largas/día"
              f" (a {args.minutos_por_visita:g} min por visualización) y {sd:,.1f} suscriptores/día")

    if len(serie) >= 2:
        print("Proyección (fecha en que se cumplen los dos umbrales → aceptación estimada):")
        for nombre, dias in (("7 días", 7), ("14 días", 14), ("28 días", 28), ("total", None)):
            v = velocidad(serie, dias)
            if not v:
                print(f"  {nombre:>8}: sin datos suficientes")
                continue
            lh, ls = fecha_llegada(hoy, faltan_h, v[0]), fecha_llegada(hoy, faltan_s, v[1])
            if lh is None or ls is None:
                print(f"  {nombre:>8}: {v[0]:,.1f} h/día, {v[1]:,.1f} subs/día → al ritmo actual no se llega")
                continue
            solicitud = max(lh, ls)
            aceptacion = solicitud + timedelta(days=args.dias_revision)
            aviso = ""
            if solicitud > args.limite:
                aviso = "  ⚠️ después de la fecha límite"
            if aceptacion >= CAMBIO_2027 or solicitud >= CAMBIO_2027:
                aviso += f"  ⚠️ riesgo de quedar bajo el umbral de {HORAS_YPP_2027:,} h (1-feb-2027)"
            print(f"  {nombre:>8}: {v[0]:,.1f} h/día, {v[1]:,.1f} subs/día → solicitud {solicitud} → aceptación ~{aceptacion}{aviso}")
    if args.vistas_shorts is not None:
        print(f"Vía Shorts (90 días): {args.vistas_shorts:,.0f}/10.000.000 visualizaciones válidas"
              f" ({args.vistas_shorts / 1e7:.0%}). Desde el 1-feb-2027 serán 20 millones.")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--historial", help="CSV con columnas fecha,canal,horas,subs")
    p.add_argument("--canal", help="analizar solo este canal del historial")
    p.add_argument("--horas", type=float, help="horas públicas válidas hoy (modo rápido)")
    p.add_argument("--subs", type=float, help="suscriptores hoy (modo rápido)")
    p.add_argument("--hoy", type=date.fromisoformat, default=date.today())
    p.add_argument("--objetivo", type=date.fromisoformat, default=date(2026, 11, 30), help="fecha objetivo de solicitud")
    p.add_argument("--limite", type=date.fromisoformat, default=date(2026, 12, 10), help="última fecha razonable de solicitud")
    p.add_argument("--dias-revision", type=int, default=30, help="días que tarda la revisión (YouTube: ~1 mes)")
    p.add_argument("--minutos-por-visita", type=float, default=25.0, help="duración media vista en vídeos largos")
    p.add_argument("--vistas-shorts", type=float, help="visualizaciones válidas de Shorts en 90 días")
    p.add_argument("--duracion", type=float, nargs="*", default=[], help="duración (min) de los episodios previstos, para el aviso de doblaje")
    a = p.parse_args()

    for d in a.duracion:
        if d >= DOBLAJE_MAX_MIN:
            print(f"⚠️ Un episodio de {d:g} min supera los {DOBLAJE_MAX_MIN} min: no tendrá doblaje automático.")

    series: dict[str, list] = defaultdict(list)
    if a.historial:
        with open(a.historial, encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                series[fila["canal"]].append((date.fromisoformat(fila["fecha"]), float(fila["horas"]), float(fila["subs"])))
    elif a.horas is not None and a.subs is not None:
        series[a.canal or "canal"].append((a.hoy, a.horas, a.subs))
    else:
        p.error("usa --historial o bien --horas y --subs")

    for canal, serie in sorted(series.items()):
        if a.canal and canal != a.canal:
            continue
        informe(canal, sorted(serie), a)


if __name__ == "__main__":
    main()
