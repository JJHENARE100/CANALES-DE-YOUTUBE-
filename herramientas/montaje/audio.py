#!/usr/bin/env python3
"""Edita la narración grabada y la deja lista para el vídeo.

Entrada: una carpeta con un archivo por capítulo (cap00.wav, cap01.wav… o .flac,
.m4a, .mp3: cualquier formato que lea ffmpeg).

Para cada capítulo:
  1. Filtro de graves (70 Hz) y, con --limpiar, reducción suave de ruido.
  2. Retomas: cada palmada precedida de un silencio de al menos 1,5 s marca un error.
     Se borra desde el inicio del párrafo fallido (la última pausa larga anterior)
     hasta el final del silencio que sigue a la palmada.
  3. Las pausas de más de --pausa-max segundos se acortan, y el silencio del
     principio y del final se recorta.
Después une los capítulos con --entre segundos de silencio y normaliza el
volumen a --lufs.

Salida en --salida:
  narracion.wav           narración completa
  capitulos.json          inicio y fin de cada capítulo, para video.py
  capitulos_youtube.txt   lista de capítulos para pegar en la descripción
  informe.txt             cada corte hecho, para comprobarlo en Audacity

Uso:
    python3 herramientas/montaje/audio.py --entrada grabaciones/ep01 --salida produccion/ep01 \\
        --guion guiones/ep01-un-dia-en-la-roma-de-trajano.md
Requiere: ffmpeg en el PATH, Python 3.10+ y numpy.
"""

import argparse
import json
import re
import subprocess
from pathlib import Path

import numpy as np

SR = 48000
FRAME = 480  # 10 ms


def decodificar(ruta: Path, limpiar: bool) -> np.ndarray:
    filtros = "highpass=f=70" + (",afftdn=nr=10:nf=-40" if limpiar else "")
    crudo = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(ruta), "-af", filtros, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        check=True, capture_output=True).stdout
    return np.frombuffer(crudo, dtype=np.float32).copy()


def tramos(mascara: np.ndarray) -> list[tuple[int, int]]:
    """Tramos [inicio, fin) en frames donde la máscara es True."""
    d = np.diff(np.concatenate(([0], mascara.astype(np.int8), [0])))
    return list(zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)))


def analizar(x: np.ndarray):
    n = len(x) // FRAME
    frames = x[: n * FRAME].reshape(n, FRAME)
    rms_db = 20 * np.log10(np.sqrt((frames ** 2).mean(axis=1)) + 1e-9)
    pico_db = 20 * np.log10(np.abs(frames).max(axis=1) + 1e-9)
    suelo = np.percentile(rms_db, 10)
    umbral = float(np.clip(suelo + 12, -60, -35))
    return rms_db, pico_db, rms_db < umbral, umbral


def editar(x: np.ndarray, args, nombre: str, informe: list[str]) -> np.ndarray:
    rms_db, pico_db, silencio, umbral = analizar(x)
    sonido = tramos(~silencio)
    silencios = tramos(silencio)
    s = lambda frames: frames * FRAME / SR  # noqa: E731
    borrar = []

    # Retomas: un sonido muy corto y fuerte, aislado entre silencios = palmada.
    for i, (a, b) in enumerate(sonido):
        corto = s(b - a) <= 0.35
        fuerte = pico_db[a:b].max() >= args.palmada_db
        # una palmada llega a su máximo en los primeros 20 ms; una palabra crece más despacio
        brusca = pico_db[a:a + 2].max() >= pico_db[a:b].max() - 3
        antes = [t for t in silencios if t[1] == a]
        despues = [t for t in silencios if t[0] == b]
        if not (corto and fuerte and brusca and antes and despues and s(antes[0][1] - antes[0][0]) >= 1.5):
            continue
        fin_retoma = despues[0][1]
        # inicio del párrafo fallido: final de la última pausa larga antes del silencio previo
        previas = [t for t in silencios if t[1] < antes[0][0] and s(t[1] - t[0]) >= args.pausa_parrafo]
        inicio = previas[-1][1] if previas else 0
        borrar.append((inicio, fin_retoma))
        informe.append(f"{nombre}: retoma en {s(a):7.1f} s → se borra {s(inicio):7.1f}–{s(fin_retoma):7.1f} s")

    # Pausas demasiado largas y silencios de los extremos.
    max_f = int(args.pausa_max * SR / FRAME)
    for a, b in silencios:
        if a == 0 or b == len(silencio):
            dejar = int(0.4 * SR / FRAME)
            borrar.append((a, b - dejar) if a == 0 else (a + dejar, b))
        elif b - a > max_f:
            borrar.append((a + max_f // 2, b - max_f // 2))

    conservar = np.ones(len(silencio), dtype=bool)
    for a, b in borrar:
        conservar[max(a, 0):max(b, 0)] = False
    muestras = np.repeat(conservar, FRAME)
    resto = x[len(muestras):]
    y = np.concatenate((x[: len(muestras)][muestras], resto))
    informe.append(f"{nombre}: {len(x) / SR / 60:5.1f} min → {len(y) / SR / 60:5.1f} min (umbral de silencio {umbral:.0f} dBFS)")
    return y


def titulos_del_guion(ruta: Path | None) -> dict[int, str]:
    if not ruta:
        return {}
    cuerpo = ruta.read_text(encoding="utf-8").split("## F. Guion", 1)[-1]
    titulos = {0: "Bienvenida"}
    for m in re.finditer(r"^### (\d+)\.\s*(.+)$", cuerpo, flags=re.M):
        titulos[int(m.group(1))] = m.group(2).strip()
    return titulos


def normalizar(entrada: Path, salida: Path, lufs: float) -> None:
    filtro = f"loudnorm=I={lufs}:TP=-2:LRA=11"
    medida = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(entrada), "-af", filtro + ":print_format=json",
                             "-f", "null", "-"], capture_output=True, text=True, check=True).stderr
    m = json.loads(medida[medida.rindex("{"):])
    filtro += (f":measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
               f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(entrada), "-af", filtro, "-ar", str(SR),
                    "-c:a", "pcm_s24le", str(salida)], check=True)


def hhmmss(seg: float) -> str:
    seg = int(seg)
    return f"{seg // 3600}:{seg % 3600 // 60:02d}:{seg % 60:02d}" if seg >= 3600 else f"{seg // 60:02d}:{seg % 60:02d}"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entrada", type=Path, required=True)
    p.add_argument("--salida", type=Path, required=True)
    p.add_argument("--guion", type=Path, help="guion maestro, para poner nombre a los capítulos")
    p.add_argument("--limpiar", action="store_true", help="reducción suave de ruido de fondo")
    p.add_argument("--pausa-max", type=float, default=2.6, help="duración máxima de una pausa (s)")
    p.add_argument("--pausa-parrafo", type=float, default=0.9, help="pausa mínima entre párrafos (s)")
    p.add_argument("--palmada-db", type=float, default=-6, help="pico mínimo de una palmada (dBFS)")
    p.add_argument("--entre", type=float, default=3.0, help="silencio entre capítulos (s)")
    p.add_argument("--lufs", type=float, default=-18, help="volumen final (LUFS integrados)")
    args = p.parse_args()

    archivos = sorted(f for f in args.entrada.iterdir() if re.match(r"cap\d+\.\w+$", f.name))
    if not archivos:
        raise SystemExit(f"No hay archivos capNN.* en {args.entrada}")
    args.salida.mkdir(parents=True, exist_ok=True)
    titulos = titulos_del_guion(args.guion)

    informe, partes, capitulos, t = [], [], [], 1.5
    partes.append(np.zeros(int(1.5 * SR), dtype=np.float32))
    for f in archivos:
        num = int(re.search(r"\d+", f.stem).group())
        y = editar(decodificar(f, args.limpiar), args, f.name, informe)
        capitulos.append({"num": num, "titulo": titulos.get(num, f"Capítulo {num}"),
                          "inicio": 0.0 if not capitulos else round(t, 2)})
        partes += [y, np.zeros(int(args.entre * SR), dtype=np.float32)]
        t += len(y) / SR + args.entre
    total = round(t, 2)
    for c, sig in zip(capitulos, capitulos[1:] + [{"inicio": total}]):
        c["fin"] = sig["inicio"]

    bruto = args.salida / "_narracion_sin_normalizar.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                    str(bruto)], input=np.concatenate(partes).astype(np.float32).tobytes(), check=True)
    normalizar(bruto, args.salida / "narracion.wav", args.lufs)
    bruto.unlink()

    (args.salida / "capitulos.json").write_text(json.dumps(capitulos, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.salida / "capitulos_youtube.txt").write_text(
        "\n".join(f"{hhmmss(c['inicio'])} {c['titulo']}" for c in capitulos) + "\n", encoding="utf-8")
    (args.salida / "informe.txt").write_text("\n".join(informe) + "\n", encoding="utf-8")
    print("\n".join(informe))
    print(f"Narración: {hhmmss(total)} · {len(capitulos)} capítulos → {args.salida}")


if __name__ == "__main__":
    main()
