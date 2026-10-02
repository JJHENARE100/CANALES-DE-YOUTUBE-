#!/usr/bin/env python3
"""Prepara un guion para grabar y montar.

A partir del guion maestro (guiones/epNN-*.md, sección «## F. Guion») genera en la
carpeta de salida:

  lectura.md  versión limpia para leer en voz alta: párrafos numerados, pausas
              visibles y el nombre del archivo que corresponde a cada capítulo.
  planos.csv  un plano (una imagen) por cada ~70–100 palabras de narración (unos 40–50 s), con su
              texto. El montaje reparte el tiempo de cada capítulo entre sus planos
              en proporción a las palabras; la columna «visual» se rellena con la
              descripción o el prompt de la imagen.

Uso:
    python3 herramientas/montaje/exportar.py guiones/ep01-un-dia-en-la-roma-de-trajano.md produccion/ep01
"""

import csv
import re
import sys
from pathlib import Path

PALABRAS_POR_PLANO = 70
PALABRAS_POR_MINUTO = 115


def leer_capitulos(guion: str) -> list[dict]:
    """Devuelve [{num, titulo, parrafos}] con «[pausa]» como párrafo propio."""
    cuerpo = guion.split("## F. Guion", 1)[1]
    capitulos = []
    for bloque in re.split(r"^### ", cuerpo, flags=re.M)[1:]:
        cabecera, _, texto = bloque.partition("\n")
        m = re.match(r"(\d+)\.\s*(.*)", cabecera.strip())
        num, titulo = (int(m.group(1)), m.group(2)) if m else (0, cabecera.strip())
        parrafos = [" ".join(p.split()) for p in re.split(r"\n\s*\n", texto) if p.strip()]
        parrafos = [p.replace("*", "") for p in parrafos if not p.startswith("#")]
        capitulos.append({"num": num, "titulo": titulo, "parrafos": parrafos})
    return capitulos


def contar(texto: str) -> int:
    return len(texto.split())


def escribir_lectura(capitulos: list[dict], titulo: str, destino: Path) -> None:
    total = sum(contar(p) for c in capitulos for p in c["parrafos"] if p != "[pausa]")
    lineas = [
        f"# {titulo} — versión para grabar",
        "",
        f"{total:,} palabras · unos {total / PALABRAS_POR_MINUTO:.0f} min. "
        "Un archivo por capítulo. Si te equivocas: 2 s de silencio, una palmada, "
        "1 s de silencio y vuelve a leer **el párrafo entero** desde su número.",
        "",
    ]
    for c in capitulos:
        palabras = sum(contar(p) for p in c["parrafos"] if p != "[pausa]")
        lineas += ["---", "", f"## Archivo `cap{c['num']:02d}` — {c['titulo']}",
                   f"*{palabras} palabras · ~{palabras / PALABRAS_POR_MINUTO:.0f} min*", ""]
        n = 0
        for p in c["parrafos"]:
            if p == "[pausa]":
                lineas += ["*— pausa larga —*", ""]
            else:
                n += 1
                lineas += [f"**{c['num']}.{n}** {p}", ""]
    destino.write_text("\n".join(lineas), encoding="utf-8")


def escribir_planos(capitulos: list[dict], destino: Path) -> int:
    """Agrupa frases hasta ~PALABRAS_POR_PLANO; un resto pequeño se une al plano anterior."""
    filas = []
    for c in capitulos:
        texto = " ".join(p for p in c["parrafos"] if p != "[pausa]")
        frases = [f for f in re.split(r"(?<=[.!?…»])\s+", texto) if f]
        grupos, actual = [], []
        for frase in frases:
            actual.append(frase)
            if contar(" ".join(actual)) >= PALABRAS_POR_PLANO:
                grupos.append(actual)
                actual = []
        if actual:
            if grupos and contar(" ".join(actual)) < PALABRAS_POR_PLANO / 3:
                grupos[-1] += actual
            else:
                grupos.append(actual)
        for k, g in enumerate(grupos, 1):
            plano = f"{c['num']:02d}-{k:02d}"
            frag = " ".join(g)
            filas.append({"plano": plano, "capitulo": c["num"], "palabras": contar(frag),
                          "imagen": f"{plano}.jpg", "visual": "", "texto": frag})
    with destino.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["plano", "capitulo", "palabras", "imagen", "visual", "texto"])
        w.writeheader()
        w.writerows(filas)
    return len(filas)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    origen, salida = Path(sys.argv[1]), Path(sys.argv[2])
    guion = origen.read_text(encoding="utf-8")
    titulo = guion.splitlines()[0].lstrip("# ").strip()
    capitulos = leer_capitulos(guion)
    salida.mkdir(parents=True, exist_ok=True)
    escribir_lectura(capitulos, titulo, salida / "lectura.md")
    n = escribir_planos(capitulos, salida / "planos.csv")
    print(f"{len(capitulos)} capítulos · {n} planos → {salida}/lectura.md, {salida}/planos.csv")


if __name__ == "__main__":
    main()
