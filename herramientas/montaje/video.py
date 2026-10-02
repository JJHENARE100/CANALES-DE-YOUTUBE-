#!/usr/bin/env python3
"""Monta el vídeo final a partir de la narración, los planos y las imágenes.

Cada plano de planos.csv es una imagen con movimiento lento: acercamiento,
alejamiento o barrido, alternándolos. Los planos funden desde negro y a negro. El
tiempo de cada capítulo se reparte entre sus planos en proporción a las palabras
que cubren, así que cada imagen aparece más o menos cuando se narra su texto.

Si falta una imagen, el plano reutiliza la anterior del mismo capítulo y lo avisa.
La música, opcional, suena en bucle muy por debajo de la voz.

Uso:
    python3 herramientas/montaje/video.py --carpeta produccion/ep01 --imagenes produccion/ep01/imagenes \\
        --musica musica/ambiente.mp3 --fuente /ruta/a/una_fuente.ttf
Requiere: ffmpeg en el PATH y Python 3.10+.
"""

import argparse
import csv
import json
import os
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ANCHO, ALTO, FPS = 1920, 1080, 25
FUNDIDO = 0.8


def movimiento(i: int, n: int) -> str:
    """Expresiones de zoompan: acercar, alejar o barrer, según el plano."""
    centro = "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
    return [
        f"z='1+0.10*on/{n}':{centro}",
        f"z='1.10-0.10*on/{n}':{centro}",
        f"z='1.08':x='(iw-iw/zoom)*on/{n}':y='ih/2-(ih/zoom/2)'",
        f"z='1.08':x='(iw-iw/zoom)*(1-on/{n})':y='ih/2-(ih/zoom/2)'",
    ][i % 4]


def texto_seguro(t: str) -> str:
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace("%", "\\%")


def renderizar_plano(tarea: dict) -> Path:
    n = max(int(round(tarea["duracion"] * FPS)), 2)
    d = n / FPS
    filtros = [
        f"scale={ANCHO * 2}:{ALTO * 2}:force_original_aspect_ratio=increase",
        f"crop={ANCHO * 2}:{ALTO * 2}",
        f"zoompan={movimiento(tarea['indice'], n)}:d={n}:s={ANCHO}x{ALTO}:fps={FPS}",
        f"fade=t=in:st=0:d={FUNDIDO}",
        f"fade=t=out:st={max(d - FUNDIDO, 0):.2f}:d={FUNDIDO}",
    ]
    if tarea.get("rotulo") and tarea.get("fuente"):
        alpha = "if(lt(t,1),0,if(lt(t,2),t-1,if(lt(t,6),1,if(lt(t,7),7-t,0))))"
        filtros.append(
            f"drawtext=fontfile='{tarea['fuente']}':text='{texto_seguro(tarea['rotulo'])}':"
            f"fontcolor=white:fontsize=64:x=(w-text_w)/2:y=h*0.78:"
            f"shadowcolor=black@0.7:shadowx=3:shadowy=3:alpha='{alpha}'")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(tarea["imagen"]), "-vf", ",".join(filtros),
         "-frames:v", str(n), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
         "-pix_fmt", "yuv420p", "-threads", "2", str(tarea["salida"])],
        check=True)
    return tarea["salida"]


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--carpeta", type=Path, required=True,
                   help="carpeta con narracion.wav, capitulos.json y planos.csv")
    p.add_argument("--imagenes", type=Path, required=True)
    p.add_argument("--musica", type=Path, help="pista de música de fondo (se repite en bucle)")
    p.add_argument("--vol-musica", type=float, default=-24, help="volumen de la música (dB)")
    p.add_argument("--fuente", type=Path, help="archivo .ttf u .otf para los títulos de capítulo")
    p.add_argument("--salida", type=Path, help="vídeo final (por defecto <carpeta>/video.mp4)")
    p.add_argument("--procesos", type=int, default=max(1, (os.cpu_count() or 2) // 2))
    args = p.parse_args()

    capitulos = json.loads((args.carpeta / "capitulos.json").read_text(encoding="utf-8"))
    with (args.carpeta / "planos.csv").open(encoding="utf-8") as f:
        planos = list(csv.DictReader(f))
    salida = args.salida or args.carpeta / "video.mp4"
    tmp = args.carpeta / "_planos"
    tmp.mkdir(exist_ok=True)

    tareas, avisos, indice = [], [], 0
    for c in capitulos:
        suyos = [pl for pl in planos if int(pl["capitulo"]) == c["num"]]
        if not suyos:
            avisos.append(f"capítulo {c['num']}: sin planos en planos.csv")
            continue
        duracion = c["fin"] - c["inicio"]
        peso = sum(int(pl["palabras"]) for pl in suyos)
        anterior = None
        for k, pl in enumerate(suyos):
            img = args.imagenes / pl["imagen"]
            if not img.exists():
                avisos.append(f"plano {pl['plano']}: falta {img.name}"
                              + (", se repite la imagen anterior" if anterior else ""))
                img = anterior
            if img is None:
                continue
            anterior = img
            tareas.append({
                "indice": indice, "imagen": img, "salida": tmp / f"{pl['plano']}.mp4",
                "duracion": duracion * int(pl["palabras"]) / peso,
                "rotulo": c["titulo"] if k == 0 and c["num"] > 0 else None,
                "fuente": str(args.fuente) if args.fuente else None,
            })
            indice += 1
    if avisos:
        print("Avisos:\n  " + "\n  ".join(avisos))
    if not tareas:
        raise SystemExit("No hay ninguna imagen con la que montar el vídeo.")

    print(f"Renderizando {len(tareas)} planos con {args.procesos} procesos…")
    with ThreadPoolExecutor(args.procesos) as ex:
        clips = list(ex.map(renderizar_plano, tareas))

    lista = tmp / "lista.txt"
    lista.write_text("".join(f"file '{c.resolve().as_posix()}'\n" for c in clips), encoding="utf-8")
    imagen_muda = tmp / "_imagen.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lista),
                    "-c", "copy", str(imagen_muda)], check=True)

    narracion = args.carpeta / "narracion.wav"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(imagen_muda), "-i", str(narracion)]
    if args.musica:
        total = capitulos[-1]["fin"]
        cmd += ["-stream_loop", "-1", "-i", str(args.musica), "-filter_complex",
                f"[2:a]aformat=channel_layouts=stereo,volume={args.vol_musica}dB,afade=t=in:d=8,"
                f"afade=t=out:st={max(total - 8, 0):.2f}:d=8[m];"
                "[1:a]aformat=channel_layouts=stereo[v];"
                "[v][m]amix=inputs=2:duration=first:normalize=0[a]",
                "-map", "0:v", "-map", "[a]"]
    else:
        cmd += ["-map", "0:v", "-map", "1:a", "-ac", "2"]
    cmd += ["-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(salida)]
    subprocess.run(cmd, check=True)
    shutil.rmtree(tmp)
    print(f"Vídeo listo: {salida}")


if __name__ == "__main__":
    main()
