#!/usr/bin/env python3
"""Genera la guía de producción de un episodio (grabación, imágenes y clips), plano a plano.

Uso:
    python3 herramientas/montaje/guia.py guiones/ep01-un-dia-en-la-roma-de-trajano.md produccion/ep01

Lee <carpeta>/planos.csv y los títulos de los capítulos del guion, y escribe
<carpeta>/guia-produccion.md: plan de sesiones de grabación, biblia visual y, para
cada capítulo, cada plano con el texto con el que entra, su imagen y, si lo
tiene, su clip de vídeo.
"""

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

PALABRAS_POR_MINUTO = 115
ESTILO = ("painterly digital illustration, soft warm light, muted ochre and dusk-blue palette, "
          "gentle atmosphere, historical accuracy, no text, no watermark, 16:9")
VIDEO = ("Image-to-video from the attached image, 5–10 seconds. Slow, calm, steady camera; only natural, "
         "subtle motion; keep the exact composition, characters and painterly style of the image; "
         "no new people or objects, no text, no camera shake, no fast movement, no morphing faces.")


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    guion, carpeta = Path(sys.argv[1]), Path(sys.argv[2])
    texto = guion.read_text(encoding="utf-8")
    titulo = texto.splitlines()[0].lstrip("# ").strip()
    cuerpo = texto.split("## F. Guion", 1)[1]
    titulos = {0: "Bienvenida"} | {int(n): t.strip() for n, t in re.findall(r"^### (\d+)\.\s*(.+)$", cuerpo, flags=re.M)}
    with (carpeta / "planos.csv").open(encoding="utf-8") as f:
        planos = list(csv.DictReader(f))
    por_cap = defaultdict(list)
    for pl in planos:
        por_cap[int(pl["capitulo"])].append(pl)
    minutos = {c: sum(int(p["palabras"]) for p in pls) / PALABRAS_POR_MINUTO for c, pls in por_cap.items()}
    clips = [p for p in planos if p.get("clip")]
    caps = sorted(por_cap)

    # sesiones de grabación de ~25–30 min de lectura
    sesiones, actual, acum = [], [], 0.0
    for c in caps:
        actual.append(c)
        acum += minutos[c]
        if acum >= 25:
            sesiones.append((actual, acum))
            actual, acum = [], 0.0
    if actual:
        if sesiones and acum < 10:  # una sesión final muy corta se une a la anterior
            cs, m = sesiones.pop()
            actual, acum = cs + actual, m + acum
        sesiones.append((actual, acum))

    L = [f"# Guía de producción — {titulo}", "",
         f"{len(planos)} planos · {len(clips)} clips de vídeo "
         f"({sum(1 for p in clips if p.get('prioridad_clip') == 'A')} de prioridad A) · "
         f"unos {sum(minutos.values()):.0f} min de narración.", "",
         "Hay tres trabajos que se pueden hacer a la vez: **grabar**, **generar imágenes** y **generar clips**.",
         "Todo se coordina por el código de plano (`01-08`): la imagen es `01-08.jpg` y el clip `01-08.mp4`, y los dos",
         "van en `imagenes/`. El montaje coloca cada plano mientras se narra su texto.", "",
         "## 1. Grabación", "",
         "Lee de [`lectura.md`](lectura.md) y sigue [`docs/grabacion.md`](../../docs/grabacion.md): claqueta, palmada si",
         "te equivocas, un archivo por capítulo. Sesiones propuestas (descansa la voz entre una y otra):", ""]
    for i, (cs, m) in enumerate(sesiones, 1):
        L.append(f"- **Sesión {i}** (~{m:.0f} min de lectura, ~{m * 1.6:.0f} min con repeticiones): "
                 + ", ".join(f"`cap{c:02d}` {titulos.get(c, '')}" for c in cs))
    L += ["", "**Antes de grabar todo:** graba `cap00` y `cap01` y pásalos por `audio.py` (o súbelos al chat para que",
          "los revise). Así se ajustan la palmada, las pausas y el volumen a tu voz y a tu habitación antes de invertir horas.", "",
          "## 2. Biblia visual (para que todo parezca del mismo canal)", "",
          "**Estilo, al final de cada descripción de imagen:**", "", f"```\n, {ESTILO}\n```", "",
          "- **Midjourney:** añade `--ar 16:9`. Cuando tengas 3–4 imágenes que te gusten, usa una como referencia de estilo",
          "  (`--sref <url>`) en todas las demás.",
          "- **ChatGPT, Gemini o Ideogram:** pide formato horizontal 16:9 y adjunta una imagen aprobada como referencia de estilo.",
          "- **Personajes que se repiten** (usa siempre la misma descripción y, si la herramienta lo permite, una imagen de referencia del personaje):",
          "  - la mujer de la insula: *a woman in a simple undyed wool tunic and brown shawl* (casi siempre de espaldas o de lejos);",
          "  - su marido: *a husband in a plain brown tunic*; la abuela: *a grandmother in a dark grey mantle*;",
          "  - el senador: *a grey-haired senator in a white toga*; su mujer: *a matron in a long pale blue stola*;",
          "  - la viuda de la tienda: *a middle-aged widow in a dark stola*.",
          "- **Caras:** de lejos, de espaldas o de perfil suave. Los primeros planos de caras delatan la IA y se deforman en los clips.",
          "- **Lugares reales de hoy** (Fontana de Trevi `06-04`, puerto de Trajano `07-04`, Monte Testaccio `08-08`, obelisco",
          "  `11-03`): mejor una **foto real** con licencia libre (Wikimedia Commons, anotando fuente, licencia y atribución en",
          "  `planos.csv`). Si se hace con IA, que se note pictórica, nunca una falsa fotografía.",
          "- **Resolución:** 1920×1080 o mayor. Guarda en `imagenes/` con el nombre exacto del plano.", "",
          "## 3. Clips de vídeo (máximo 10 s)", "",
          "- **Cómo se generan:** en tu herramienta de vídeo (Kling, Runway, Veo, Hailuo o Luma), en modo *imagen a vídeo*, a partir",
          "  de la imagen del plano. Así el clip encaja con ella.",
          "- **Prioridad:** **A** primero (la mayoría son agua, luz, río o carros, que se generan bien); **B** si sobran créditos.",
          "- **Cómo se montan:** el plano empieza con el clip y funde a la imagen con movimiento. Para más calma, monta con",
          "  `--clip-lentitud 1.25`. Si un clip sale raro, no lo uses: el plano funciona igual solo con la imagen.",
          "- **Texto común, al final de cada descripción de clip:**", "", f"```\n{VIDEO}\n```", ""]
    L += ["## 4. Plano a plano", ""]
    for c in caps:
        L += [f"### `cap{c:02d}` · {titulos.get(c, '')} (~{minutos[c]:.0f} min)", ""]
        for p in por_cap[c]:
            palabras = p["texto"].split()
            L.append(f"**{p['plano']}** · entra con «{' '.join(palabras[:9])}…» → `{p['imagen']}`")
            L.append(f"- Imagen: {p['visual']}")
            if p.get("clip"):
                L.append(f"- 🎬 Clip **{p.get('prioridad_clip', '')}** `{p['clip']}`: {p['prompt_video']}")
            L.append("")
    (carpeta / "guia-produccion.md").write_text("\n".join(L), encoding="utf-8")
    print(f"Guía: {carpeta / 'guia-produccion.md'} · {len(sesiones)} sesiones de grabación")


if __name__ == "__main__":
    main()
