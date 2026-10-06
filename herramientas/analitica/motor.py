#!/usr/bin/env python3
"""Motor de decisión: aplica la lógica de un recomendador a nuestras decisiones.

Un recomendador (TikTok, YouTube) recoge señales, filtra candidatos, predice cuáles
interesarán, ordena con diversidad y exploración, y vuelve a aprender. Este motor
hace lo mismo a escala de canal, con los datos de YouTube Studio:

  diagnostico  Para cada vídeo, en qué fase del recomendador falla (candidatos,
               atractivo, retención o suscripción) y qué hacer.
  puerta       Puntuación relativa de los canales para elegir el principal (plan,
               20 de octubre).
  siguiente    Ordena los próximos temas con lo aprendido por serie, la demanda
               externa, la saturación, una cuota de exploración y una regla de
               diversidad.

Entrada: la exportación de YouTube Studio → Estadísticas → Modo avanzado →
Exportar → CSV («Datos de la tabla.csv»), con estas columnas: visualizaciones,
tiempo de visualización (horas), impresiones, CTR de impresiones, duración media,
porcentaje medio visto y suscriptores. Se aceptan los nombres en español y en
inglés.

Uso:
    python3 herramientas/analitica/motor.py diagnostico --studio historia.csv
    python3 herramientas/analitica/motor.py puerta --canal historia=historia.csv --canal ciencia=ciencia.csv \\
        --horas-trabajo historia=18 --horas-trabajo ciencia=14
    python3 herramientas/analitica/motor.py siguiente --temas docs/datos/temas_candidatos.csv \\
        --canal historia --studio historia.csv --n 6
Solo usa la biblioteca estándar de Python.
"""

import argparse
import csv
import math
import re
import statistics
import unicodedata
from pathlib import Path

ALIAS = {
    "titulo": ["titulo del video", "video title", "titulo"],
    "vistas": ["visualizaciones", "views"],
    "horas": ["tiempo de visualizacion (horas)", "watch time (hours)"],
    "impresiones": ["impresiones", "impressions"],
    "ctr": ["porcentaje de clics de las impresiones (%)", "impressions click-through rate (%)", "ctr de las impresiones"],
    "duracion_media": ["duracion media de las visualizaciones", "average view duration"],
    "pct_visto": ["porcentaje medio visto (%)", "average percentage viewed (%)"],
    "subs": ["suscriptores", "subscribers"],
}


def normal(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().strip()
    return re.sub(r"\s+", " ", s)


def numero(v: str) -> float:
    v = (v or "").strip()
    if not v:
        return 0.0
    if ":" in v:  # H:MM:SS o MM:SS → minutos
        partes = [float(p) for p in v.split(":")]
        while len(partes) < 3:
            partes.insert(0, 0.0)
        return partes[0] * 60 + partes[1] + partes[2] / 60
    v = v.replace("%", "").replace(" ", "")
    if "," in v and "." in v:
        v = v.replace(".", "").replace(",", ".") if v.rfind(",") > v.rfind(".") else v.replace(",", "")
    elif "," in v:
        v = v.replace(",", ".")
    return float(v)


def leer_studio(ruta: Path) -> list[dict]:
    with ruta.open(encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f))
    if not filas:
        return []
    columnas = {normal(c): c for c in filas[0]}
    mapa = {}
    for clave, nombres in ALIAS.items():
        for n in nombres:
            hit = next((orig for norm, orig in columnas.items() if norm == n or norm.startswith(n)), None)
            if hit:
                mapa[clave] = hit
                break
    faltan = [k for k in ("titulo", "vistas", "horas", "impresiones", "ctr") if k not in mapa]
    if faltan:
        raise SystemExit(f"{ruta}: faltan columnas {faltan}. Exporta desde Modo avanzado con esas métricas.")
    videos = []
    for fila in filas:
        titulo = fila.get(mapa["titulo"], "").strip()
        if not titulo or normal(titulo) in ("total", "totales"):
            continue
        v = {"titulo": titulo}
        for clave, col in mapa.items():
            if clave != "titulo":
                v[clave] = numero(fila.get(col, ""))
        v["h_1000_imp"] = v["horas"] / v["impresiones"] * 1000 if v["impresiones"] else 0.0
        v["subs_1000_vis"] = v.get("subs", 0) / v["vistas"] * 1000 if v["vistas"] else 0.0
        videos.append(v)
    return videos


def mediana(vals):
    vals = [x for x in vals if x is not None]
    return statistics.median(vals) if vals else 0.0


# ---------------------------------------------------------------- diagnóstico
def diagnostico(args) -> None:
    videos = leer_studio(args.studio)
    if not videos:
        raise SystemExit("La exportación no tiene vídeos.")
    m = {k: mediana([v.get(k) for v in videos if v.get("impresiones", 0) >= args.min_impresiones])
         for k in ("impresiones", "ctr", "pct_visto", "duracion_media", "subs_1000_vis", "h_1000_imp")}
    print(f"Medianas del canal: {m['impresiones']:,.0f} impresiones · CTR {m['ctr']:.1f}% · "
          f"visto {m['pct_visto']:.0f}% · {m['duracion_media']:.1f} min · {m['subs_1000_vis']:.1f} subs/1.000 vis · "
          f"{m['h_1000_imp']:.1f} h/1.000 impresiones\n")
    for v in sorted(videos, key=lambda x: -x["h_1000_imp"]):
        print(f"■ {v['titulo'][:70]}")
        print(f"  {v['impresiones']:,.0f} imp · CTR {v['ctr']:.1f}% · visto {v.get('pct_visto', 0):.0f}% · "
              f"{v['h_1000_imp']:.1f} h/1.000 imp · {v['subs_1000_vis']:.1f} subs/1.000 vis")
        if v["impresiones"] < args.min_impresiones:
            print(f"  → Pocos datos (menos de {args.min_impresiones:,} impresiones). Esperar antes de juzgarlo.\n")
            continue
        consejos = []
        bajo = lambda k: m[k] and v.get(k, 0) < 0.8 * m[k]  # noqa: E731
        alto = lambda k: m[k] and v.get(k, 0) > 1.2 * m[k]  # noqa: E731
        if bajo("ctr"):
            consejos.append("ATRACTIVO: la gente ve la miniatura y no hace clic. Prueba otra miniatura y otro título en «Probar y comparar».")
        if m["pct_visto"] and bajo("pct_visto"):
            consejos.append("RETENCIÓN: hace clic pero se va. Revisa la curva de retención: la promesa del título se cumple tarde o el primer minuto no engancha.")
        if bajo("impresiones") and not bajo("ctr") and not bajo("pct_visto"):
            consejos.append("CANDIDATOS: gusta a quien lo ve, pero YouTube lo enseña poco. Tema con poca demanda o metadatos poco claros: título con el término que busca la gente, enlaza el vídeo desde los que funcionan e inclúyelo en una lista de reproducción.")
        if bajo("subs_1000_vis"):
            consejos.append("SUSCRIPCIÓN: se ve pero no convierte. Anuncia la serie («cada lunes, otra ciudad») y pon una pantalla final hacia el siguiente vídeo.")
        if alto("ctr") and m["pct_visto"] and alto("pct_visto"):
            consejos.append("GANADOR: buena entrada y buena retención. Haz secuela o serie y enlázala desde los demás vídeos.")
        print("  → " + ("\n  → ".join(consejos) if consejos else "En la media del canal. Sin acción urgente.") + "\n")


# ---------------------------------------------------------------- puerta
PESOS = {"h_1000_imp": 0.35, "subs_1000_vis": 0.25, "pct_visto": 0.20, "ctr": 0.10, "eficiencia": 0.10}


def pares(lista: list[str] | None) -> dict[str, str]:
    out = {}
    for s in lista or []:
        k, _, v = s.partition("=")
        out[k] = v
    return out


def puerta(args) -> None:
    canales = pares(args.canal)
    trabajo = {k: float(v) for k, v in pares(args.horas_trabajo).items()}
    datos = {}
    for nombre, ruta in canales.items():
        vids = leer_studio(Path(ruta))
        imp = sum(v["impresiones"] for v in vids)
        vis = sum(v["vistas"] for v in vids)
        horas = sum(v["horas"] for v in vids)
        datos[nombre] = {
            "h_1000_imp": horas / imp * 1000 if imp else 0,
            "subs_1000_vis": sum(v.get("subs", 0) for v in vids) / vis * 1000 if vis else 0,
            "pct_visto": mediana([v.get("pct_visto") for v in vids]),
            "ctr": sum(v["ctr"] * v["impresiones"] for v in vids) / imp if imp else 0,
            "eficiencia": horas / trabajo[nombre] if trabajo.get(nombre) else 0,
            "impresiones": imp, "horas": horas,
        }
    if not trabajo:
        print("Aviso: sin --horas-trabajo, la eficiencia (10%) no se tiene en cuenta.")
    puntos = {}
    for n, d in datos.items():
        puntos[n] = sum(w * (d[k] / max(x[k] for x in datos.values()) if max(x[k] for x in datos.values()) else 0)
                        for k, w in PESOS.items())
    print("Canal       h/1.000 imp  subs/1.000 vis  % visto   CTR   horas públicas/h trabajo  impresiones  PUNTOS")
    for n, d in sorted(datos.items(), key=lambda x: -puntos[x[0]]):
        print(f"{n:<11} {d['h_1000_imp']:>10.1f}  {d['subs_1000_vis']:>13.1f}  {d['pct_visto']:>6.0f}%  {d['ctr']:>4.1f}%"
              f"  {d['eficiencia']:>23.1f}  {d['impresiones']:>11,.0f}  {puntos[n]:.2f}")
    orden = sorted(puntos, key=lambda n: -puntos[n])
    if len(orden) >= 2:
        a, b = orden[0], orden[1]
        pocos = [n for n, d in datos.items() if d["impresiones"] < args.min_impresiones * 2]
        if pocos:
            print(f"\nDatos aún escasos en: {', '.join(pocos)}. La decisión es provisional.")
        if puntos[b] and (puntos[a] - puntos[b]) / puntos[a] < 0.10:
            print(f"\nDiferencia menor del 10% entre {a} y {b}: no hay ganador claro. Mantener los dos 7 días más y repetir.")
        else:
            print(f"\nCanal principal: {a} (70–80% del tiempo). {b}: un episodio quincenal, o semanal si mantiene su trayectoria.")


# ---------------------------------------------------------------- siguiente
SATURACION = {"baja": 1.0, "media": 0.6, "alta": 0.3}


def siguiente(args) -> None:
    with args.temas.open(encoding="utf-8") as f:
        temas = [t for t in csv.DictReader(f) if t["canal"] == args.canal]
    videos = leer_studio(args.studio) if args.studio else []
    # aprendizaje por serie: h/1.000 impresiones de los vídeos publicados, encogido hacia la media del canal
    rend = {}
    for t in temas:
        clave = (t.get("titulo_publicado") or "").strip()
        if clave:
            v = next((v for v in videos if normal(clave) in normal(v["titulo"]) and v["impresiones"] >= args.min_impresiones), None)
            if v:
                rend.setdefault(t["serie"], []).append(v["h_1000_imp"])
    todos = [x for xs in rend.values() for x in xs]
    media = statistics.mean(todos) if todos else 0.0
    k = 2.0  # pseudo-observaciones: con pocos datos, la serie se parece a la media del canal
    aprendido = {s: (sum(xs) + k * media) / (len(xs) + k) for s, xs in rend.items()}
    n_serie = {s: len(xs) for s, xs in rend.items()}

    pendientes = [t for t in temas if (t.get("estado") or "pendiente") == "pendiente"]
    fijos = sorted((t for t in pendientes if (t.get("fecha_fija") or "").strip()), key=lambda t: t["fecha_fija"])
    pendientes = [t for t in pendientes if t not in fijos]  # los de fecha fija no compiten: van anclados al calendario
    if not pendientes:
        raise SystemExit("No hay temas pendientes para ese canal.")
    max_dem = max((float(t.get("demanda") or 0) for t in pendientes), default=0) or 1
    max_apr = max(aprendido.values(), default=0) or 1

    def puntuar(t, ya_elegidas):
        s = t["serie"]
        dem = math.log1p(float(t.get("demanda") or 0)) / math.log1p(max_dem)
        apr = aprendido.get(s, media) / max_apr if (aprendido or media) else 0.5
        sat = SATURACION.get((t.get("saturacion") or "media").lower(), 0.6)
        exploracion = args.exploracion / math.sqrt(1 + n_serie.get(s, 0))  # serie sin probar = más bonus
        base = 0.40 * apr + 0.35 * dem + 0.25 * sat + exploracion
        return base * (0.7 ** ya_elegidas.count(s))  # diversidad: penaliza repetir serie en el plan

    plan, ultimas = [], []
    resto = pendientes[:]
    for i in range(min(args.n, len(resto))):
        explorar = (i + 1) % 5 == 0  # cuota de exploración: 1 de cada 5 huecos, una serie sin datos
        candidatos = [t for t in resto if not ultimas or t["serie"] != ultimas[-1]] or resto
        if explorar:
            sin_datos = [t for t in candidatos if t["serie"] not in n_serie]
            candidatos = sin_datos or candidatos
        mejor = max(candidatos, key=lambda t: puntuar(t, ultimas))
        plan.append((mejor, puntuar(mejor, ultimas), explorar))
        ultimas.append(mejor["serie"])
        resto.remove(mejor)

    print(f"Aprendido por serie (h/1.000 impresiones, media del canal {media:.1f}): "
          + (", ".join(f"{s} {v:.1f} (n={n_serie[s]})" for s, v in aprendido.items()) or "aún sin datos; ordena por demanda y saturación"))
    if fijos:
        print("\nAnclados al calendario (fecha fija, fuera del ranking): "
              + "; ".join(f"{t['fecha_fija']} {t['tema']}" for t in fijos))
    print(f"\nPróximos {len(plan)} episodios flexibles — {args.canal} (rellenan las semanas sin fecha fija):")
    for i, (t, p, exp) in enumerate(plan, 1):
        print(f"{i}. {t['tema']}  [serie {t['serie']} · puntos {p:.2f}{' · EXPLORACIÓN' if exp else ''}]")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="modo", required=True)
    d = sub.add_parser("diagnostico")
    d.add_argument("--studio", type=Path, required=True)
    g = sub.add_parser("puerta")
    g.add_argument("--canal", action="append", required=True, help="nombre=export.csv (repetible)")
    g.add_argument("--horas-trabajo", action="append", help="nombre=horas tuyas invertidas (repetible)")
    s = sub.add_parser("siguiente")
    s.add_argument("--temas", type=Path, required=True)
    s.add_argument("--canal", required=True)
    s.add_argument("--studio", type=Path)
    s.add_argument("--n", type=int, default=6)
    s.add_argument("--exploracion", type=float, default=0.15)
    for x in (d, g, s):
        x.add_argument("--min-impresiones", type=int, default=1000)
    args = p.parse_args()
    {"diagnostico": diagnostico, "puerta": puerta, "siguiente": siguiente}[args.modo](args)


if __name__ == "__main__":
    main()
