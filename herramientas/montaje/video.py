#!/usr/bin/env python3
"""Monta el vídeo final a partir de la narración, los planos y las imágenes.

Cada plano de planos.csv es una imagen con movimiento lento. Hay siete movimientos
(acercar, alejar, barrer a izquierda o derecha, subir, bajar y fijo). Se eligen de
forma variada sin repetir el anterior, o se fijan con la columna «movimiento». El
tiempo de cada capítulo se reparte entre sus planos en proporción a sus palabras.

Clips de vídeo: si la columna «clip» nombra un vídeo (por ejemplo 01-08.mp4,
generado a partir de la imagen del plano) y está en la carpeta de imágenes, el
plano empieza con el clip y funde en 1 s a la imagen con movimiento durante el
resto de su tiempo. Si el clip no está, el plano usa solo la imagen.

Derechos: cada imagen real («REAL:» en «visual», o con «fuente» rellena) necesita
«licencia» y «atribucion». Si falta alguna, el montaje se detiene, salvo con
--borrador. Siempre se genera creditos.txt con la procedencia de cada imagen, para
la descripción del vídeo y como expediente de producción.

Uso:
    python3 herramientas/montaje/video.py --carpeta produccion/ep01 --imagenes produccion/ep01/imagenes \\
        --musica musica/ambiente.mp3 --tipografia /ruta/a/una_fuente.ttf --pantalla-final 20
Requiere: ffmpeg en el PATH y Python 3.10+.
"""

import argparse
import csv
import json
import os
import random
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ANCHO, ALTO, FPS = 1920, 1080, 25
FUNDIDO = 0.8
DOBLAJE_MAX_S = 119.5 * 60  # YouTube no dobla automáticamente vídeos de más de 120 min

MOVIMIENTOS = {
    "acercar": "z='1+0.10*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
    "alejar": "z='1.10-0.10*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
    "derecha": "z='1.08':x='(iw-iw/zoom)*on/{n}':y='ih/2-(ih/zoom/2)'",
    "izquierda": "z='1.08':x='(iw-iw/zoom)*(1-on/{n})':y='ih/2-(ih/zoom/2)'",
    "subir": "z='1.08':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(1-on/{n})'",
    "bajar": "z='1.08':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*on/{n}'",
    "fijo": "z='1.02':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
}
VARIADOS = [m for m in MOVIMIENTOS if m != "fijo"]


def texto_seguro(t: str) -> str:
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace("%", "\\%")


def es_real(pl: dict) -> bool:
    return pl.get("visual", "").startswith("REAL:") or bool(pl.get("fuente", "").strip())


def duracion_clip(ruta: Path) -> float:
    salida = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "format=duration",
                             "-of", "csv=p=0", str(ruta)], capture_output=True, text=True, check=True).stdout
    return float(salida.strip())


def imagen_en_movimiento(movimiento: str, frames: int) -> str:
    return (f"scale={ANCHO * 2}:{ALTO * 2}:force_original_aspect_ratio=increase,crop={ANCHO * 2}:{ALTO * 2},"
            f"zoompan={MOVIMIENTOS[movimiento].format(n=frames)}:d={frames}:s={ANCHO}x{ALTO}:fps={FPS},setsar=1,format=yuv420p")


def renderizar_plano(tarea: dict) -> Path:
    n = max(int(round(tarea["duracion"] * FPS)), 2)
    d = n / FPS
    entradas = ["-i", str(tarea["imagen"])]
    clip = tarea.get("clip")
    if clip:
        cd = min(duracion_clip(clip) * tarea["lentitud"], d)
        resto = d - cd
        video_clip = (f"[0:v]setpts={tarea['lentitud']}*PTS,fps={FPS},scale={ANCHO}:{ALTO}:force_original_aspect_ratio=increase,"
                      f"crop={ANCHO}:{ALTO},setsar=1,format=yuv420p,trim=duration={cd:.3f},setpts=PTS-STARTPTS")
        entradas = ["-i", str(clip), "-i", str(tarea["imagen"])]
        if resto >= 2:
            nb = int(round((resto + 1) * FPS))
            grafo = (f"{video_clip}[a];[1:v]{imagen_en_movimiento(tarea['movimiento'], nb)}[b];"
                     f"[a][b]xfade=transition=fade:duration=1:offset={cd - 1:.3f}")
        else:
            grafo = f"{video_clip},tpad=stop_mode=clone:stop_duration={resto:.3f}"
        filtros = [grafo, f"fade=t=in:st=0:d={FUNDIDO}"]
    else:
        filtros = [imagen_en_movimiento(tarea["movimiento"], n), f"fade=t=in:st=0:d={FUNDIDO}"]
    if not tarea.get("sin_fundido_final"):
        filtros.append(f"fade=t=out:st={max(d - FUNDIDO, 0):.2f}:d={FUNDIDO}")
    if tarea.get("oscurecer"):
        filtros.append("eq=brightness=-0.25")
    if tarea.get("rotulo") and tarea.get("tipografia"):
        alpha = "if(lt(t,1),0,if(lt(t,2),t-1,if(lt(t,6),1,if(lt(t,7),7-t,0))))"
        filtros.append(
            f"drawtext=fontfile='{tarea['tipografia']}':text='{texto_seguro(tarea['rotulo'])}':"
            f"fontcolor=white:fontsize=64:x=(w-text_w)/2:y=h*0.78:"
            f"shadowcolor=black@0.7:shadowx=3:shadowy=3:alpha='{alpha}'")
    opcion = "-filter_complex" if clip else "-vf"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", *entradas, opcion, ",".join(filtros),
         "-frames:v", str(n), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
         "-pix_fmt", "yuv420p", "-threads", "2", str(tarea["salida"])],
        check=True)
    return tarea["salida"]


def escribir_creditos(planos: list[dict], destino: Path) -> list[str]:
    """Escribe el manifiesto de imágenes y devuelve los planos reales sin licencia o atribución."""
    faltan, reales, ia = [], [], 0
    for pl in planos:
        if es_real(pl):
            if not pl.get("licencia", "").strip() or not pl.get("atribucion", "").strip():
                faltan.append(pl["plano"])
            reales.append(pl)
        else:
            ia += 1
    lineas = ["CRÉDITOS DE IMAGEN", ""]
    for pl in reales:
        lineas.append(f"[{pl['plano']}] {pl.get('atribucion') or '¿atribución?'} · {pl.get('licencia') or '¿licencia?'}"
                      + (f" · {pl['url']}" if pl.get("url") else ""))
    if ia:
        lineas += ["", f"Ilustraciones generadas con IA: {ia} planos."]
    destino.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return faltan


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--carpeta", type=Path, required=True,
                   help="carpeta con narracion.wav, capitulos.json y planos.csv")
    p.add_argument("--imagenes", type=Path, required=True)
    p.add_argument("--musica", type=Path, help="pista de música de fondo (se repite en bucle)")
    p.add_argument("--vol-musica", type=float, default=-24, help="volumen de la música (dB)")
    p.add_argument("--tipografia", type=Path, help="archivo .ttf u .otf para los títulos de capítulo")
    p.add_argument("--pantalla-final", type=float, default=0,
                   help="segundos extra al final (imagen oscurecida y música) para la pantalla final de YouTube")
    p.add_argument("--clip-lentitud", type=float, default=1.0,
                   help="ralentiza los clips (1.5 = un 50 %% más lentos, más calma)")
    p.add_argument("--borrador", action="store_true", help="monta aunque falten licencias (no publicar)")
    p.add_argument("--salida", type=Path, help="vídeo final (por defecto <carpeta>/video.mp4)")
    p.add_argument("--procesos", type=int, default=max(1, (os.cpu_count() or 2) // 2))
    args = p.parse_args()

    capitulos = json.loads((args.carpeta / "capitulos.json").read_text(encoding="utf-8"))
    with (args.carpeta / "planos.csv").open(encoding="utf-8") as f:
        planos = list(csv.DictReader(f))
    salida = args.salida or args.carpeta / "video.mp4"

    faltan = escribir_creditos(planos, args.carpeta / "creditos.txt")
    if faltan:
        msg = f"{len(faltan)} imágenes reales sin licencia o atribución: {', '.join(faltan[:12])}{'…' if len(faltan) > 12 else ''}"
        if not args.borrador:
            raise SystemExit(msg + "\nRellena las columnas licencia y atribucion en planos.csv, o usa --borrador para una prueba.")
        print("⚠️ BORRADOR — " + msg)

    narrado = capitulos[-1]["fin"]
    if narrado + args.pantalla_final > DOBLAJE_MAX_S:
        print(f"⚠️ El vídeo durará {(narrado + args.pantalla_final) / 60:.0f} min: con más de 120 min no tendrá doblaje automático.")

    tmp = args.carpeta / "_planos"
    tmp.mkdir(exist_ok=True)
    rng = random.Random(str(args.carpeta.resolve().name))
    tareas, avisos, anterior_mov = [], [], None
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
            mov = (pl.get("movimiento") or "").strip()
            if mov not in MOVIMIENTOS:
                mov = rng.choice([m for m in VARIADOS if m != anterior_mov])
            anterior_mov = mov
            clip = args.imagenes / pl["clip"] if pl.get("clip") else None
            tareas.append({
                "clip": clip if clip and clip.exists() else None, "lentitud": args.clip_lentitud,
                "imagen": img, "salida": tmp / f"{pl['plano']}.mp4", "movimiento": mov,
                "duracion": duracion * int(pl["palabras"]) / peso,
                "rotulo": c["titulo"] if k == 0 and c["num"] > 0 else None,
                "tipografia": str(args.tipografia) if args.tipografia else None,
            })
    if avisos:
        print("Avisos:\n  " + "\n  ".join(avisos))
    if not tareas:
        raise SystemExit("No hay ninguna imagen con la que montar el vídeo.")
    if args.pantalla_final > 0:
        tareas.append({"imagen": tareas[-1]["imagen"], "salida": tmp / "zz_pantalla_final.mp4", "movimiento": "fijo",
                       "duracion": args.pantalla_final, "oscurecer": True, "sin_fundido_final": True})

    print(f"Renderizando {len(tareas)} planos ({sum(1 for x in tareas if x.get('clip'))} con clip de vídeo) con {args.procesos} procesos…")
    with ThreadPoolExecutor(args.procesos) as ex:
        clips = list(ex.map(renderizar_plano, tareas))

    lista = tmp / "lista.txt"
    lista.write_text("".join(f"file '{c.resolve().as_posix()}'\n" for c in clips), encoding="utf-8")
    imagen_muda = tmp / "_imagen.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lista),
                    "-c", "copy", str(imagen_muda)], check=True)

    total = narrado + args.pantalla_final
    voz = f"[1:a]aformat=channel_layouts=stereo,apad=whole_dur={total:.2f}[v]"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(imagen_muda), "-i", str(args.carpeta / "narracion.wav")]
    if args.musica:
        cmd += ["-stream_loop", "-1", "-i", str(args.musica), "-filter_complex",
                f"{voz};[2:a]aformat=channel_layouts=stereo,volume={args.vol_musica}dB,afade=t=in:d=8,"
                f"afade=t=out:st={max(total - 8, 0):.2f}:d=8[m];"
                "[v][m]amix=inputs=2:duration=first:normalize=0[a]"]
    else:
        cmd += ["-filter_complex", voz.replace("[v]", "[a]")]
    cmd += ["-map", "0:v", "-map", "[a]", "-t", f"{total:.2f}", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", str(salida)]
    subprocess.run(cmd, check=True)
    shutil.rmtree(tmp)
    print(f"Vídeo listo: {salida}\nCréditos: {args.carpeta / 'creditos.txt'}")


if __name__ == "__main__":
    main()
