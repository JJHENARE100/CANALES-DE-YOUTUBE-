# Montaje de episodios

Tres programas que convierten un guion, tu grabación y las imágenes en el vídeo
final. Se ejecutan en tu ordenador. Este entorno en la nube solo tiene acceso
limitado a internet, y un vídeo de 90 minutos ocupa cerca de 1 GB, demasiado para
moverlo por GitHub.

```
guion.md ──exportar.py──► lectura.md   (lo que lees al grabar)
                      └─► planos.csv   (una imagen cada ~40–50 s, con su descripción)

capNN.wav ──audio.py──► narracion.wav + capitulos.json + capitulos_youtube.txt + informe.txt

narracion.wav + planos.csv + imágenes (+ música) ──video.py──► video.mp4 (1080p)
```

## Instalación (una sola vez)

1. **Python 3.10 o superior.**
   - Windows: [python.org](https://www.python.org/downloads/); marca «Add Python to PATH» al instalar.
   - Mac: `brew install python`.
2. **ffmpeg.**
   - Windows: `winget install Gyan.FFmpeg`.
   - Mac: `brew install ffmpeg`.
3. **numpy:** `pip install numpy`.
4. **El repositorio:** clónalo, o descárgalo como ZIP desde GitHub.

Para comprobarlo, abre una terminal en la carpeta del repositorio y escribe
`ffmpeg -version` y `python --version`. Ambos deben responder.

## Paso a paso (episodio 1)

### 1. Exportar el guion

Ya está hecho para el episodio 1: `produccion/ep01/lectura.md` y
`produccion/ep01/planos.csv`. Para un guion nuevo:

```
python herramientas/montaje/exportar.py guiones/ep02-....md produccion/ep02
```

### 2. Grabar

Sigue [`docs/grabacion.md`](../../docs/grabacion.md) y guarda `cap00`–`cap14` en
`grabaciones/ep01/`.

### 3. Editar el audio

```
python herramientas/montaje/audio.py --entrada grabaciones/ep01 --salida produccion/ep01 --guion guiones/ep01-un-dia-en-la-roma-de-trajano.md
```

- **Si hay ruido de fondo**, añade `--limpiar`.
- **Si grabaste con claqueta** («episodio 1, capítulo 3, toma 1» y 2 s de silencio), añade `--claqueta`.
- **Revisa `informe.txt`.** Comprueba en Audacity las retomas que se hayan
  cortado: el informe da el segundo exacto de cada corte.
- **Si alguna palmada no se detecta**, prueba con `--palmada-db -10`. Si se borra
  de más, con `--pausa-parrafo 1.2`.
- **Pega `capitulos_youtube.txt` en la descripción** del vídeo.

### 4. Imágenes

Cada fila de `planos.csv` tiene:

- `imagen`: el nombre de archivo que espera el montaje (`01-03.jpg`).
- `visual`: la descripción de la escena, en inglés.
- `texto`: lo que se narra mientras se ve la imagen.

**Para generarlas,** pega en tu generador de imágenes (Midjourney, ChatGPT,
Gemini, Ideogram…) el `visual` de cada fila seguido siempre del mismo estilo:

```
, painterly digital illustration, soft warm light, muted ochre and dusk-blue palette,
gentle atmosphere, historical accuracy, no text, no watermark, 16:9
```

- En Midjourney, añade además `--ar 16:9`.
- **Guarda cada imagen con su nombre** en `produccion/ep01/imagenes/`. Vale JPG o
  PNG con el mismo nombre (si es PNG, cambia la extensión en el CSV).
- **Si falta alguna**, el montaje repite la anterior del mismo capítulo y te avisa.
  Así puedes probar el vídeo con solo unas pocas imágenes.
- **Canal de ciencia:** el `visual` empieza por `REAL:` o por `IA:`.
  - `REAL:` es una foto real que hay que buscar en NASA, ESA o ESO por su
    descripción. Comprueba la licencia y copia la atribución en la descripción
    del vídeo.
  - `IA:` es una descripción para tu generador de imágenes, como en el canal de
    historia.
- **Estilo pictórico, no fotográfico.** Con este estilo las imágenes no necesitan
  la etiqueta de contenido sintético. Si alguna parece una fotografía real de algo
  que no ocurrió, márcala como contenido alterado al subir el vídeo.

### Derechos de cada imagen (obligatorio)

- **Qué rellenar:** en `planos.csv`, cada imagen real lleva `fuente`, `licencia`,
  `atribucion` y `url`. Por ejemplo: NASA · dominio público (guía de medios de
  la NASA) · «NASA/JPL-Caltech» · enlace a la página de la imagen.
- **Si falta algo, `video.py` se detiene.** Con `--borrador` monta igualmente para
  pruebas, pero ese vídeo no se publica.
- **Créditos:** siempre se genera `creditos.txt`; pégalo en la descripción.
- **Movimiento de cámara:** la columna `movimiento` lo fija para un plano
  (acercar, alejar, derecha, izquierda, subir, bajar o fijo). Si se deja vacía,
  se elige uno variado sin repetir el anterior.

### 5. Música (opcional)

Descarga una pista tranquila de la **Biblioteca de audio de YouTube** (YouTube
Studio → Biblioteca de audio), que se puede usar en vídeos monetizados. Elige una
sin atribución obligatoria, o copia la atribución en la descripción.

### 6. Montar el vídeo

```
python herramientas/montaje/video.py --carpeta produccion/ep01 --imagenes produccion/ep01/imagenes --musica musica/ambiente.mp3 --tipografia "C:/Windows/Fonts/georgia.ttf" --pantalla-final 20
```

- **Títulos de capítulo:** `--tipografia` los rotula al empezar cada capítulo; sin
  ella no se rotulan. En Mac puedes usar `/System/Library/Fonts/Supplemental/Georgia.ttf`.
- **Pantalla final:** `--pantalla-final 20` añade 20 s finales con la imagen
  oscurecida y música, para poner encima los elementos de pantalla final de
  YouTube.
- **Aviso de duración:** si el vídeo pasa de 119,5 min, el montaje avisa de que
  perderá el doblaje automático.
- **Volumen de la música:** `--vol-musica` (−24 dB por defecto). Para que suene
  más baja, usa −28.
- **Tiempo de render:** en este entorno de prueba salió a unas 3 veces tiempo
  real con 2 procesos. Un episodio de 90 minutos tarda entre 20 y 60 minutos,
  según el ordenador.

El resultado es `produccion/ep01/video.mp4`, listo para subir a YouTube.

## Probado

En el entorno de desarrollo, con audio sintético y una retoma marcada con
palmada:

- **Retoma:** se borró justo el párrafo fallido.
- **Pausas:** las largas se acortaron.
- **Volumen:** −18,0 LUFS medidos.
- **Vídeo:** 1080p a 25 fps, con audio AAC estéreo y los títulos de capítulo
  rotulados.
- **Imagen que falta:** el plano repitió la anterior y avisó.

Falta probarlo con una grabación real: es posible que haya que ajustar
`--palmada-db` o `--pausa-parrafo` a tu voz y a tu habitación.
