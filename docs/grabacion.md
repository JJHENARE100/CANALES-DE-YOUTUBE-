# Cómo grabar un episodio

Grabar el episodio con tu voz tiene una ventaja doble:

- **Es lo más seguro frente a la revisión del YPP.** Una voz humana real no
  entra en ninguna de las categorías de contenido no auténtico.
- **Sirve para entrenar tu clon.** El clon profesional de ElevenLabs pide 1–3 h
  de audio limpio. Con grabar el episodio 1 (unos 90 min) ya lo tienes, y los
  siguientes episodios se pueden generar con el clon cuando no tengas tiempo de
  grabar.

## Material

| Qué | Recomendación | Precio orientativo |
|---|---|---|
| Micrófono | USB dinámico (por ejemplo, Samson Q2U, Audio-Technica ATR2100x o Fifine K688). Un dinámico capta menos la habitación que un condensador | 60–100 € |
| Alternativa barata | Micrófono de solapa con cable conectado al móvil | 15–25 € |
| Antipop | Espuma o filtro de malla | 5–10 € |
| Auriculares | Cualquiera cerrado, para oírte mientras grabas | — |
| Programa | [Audacity](https://www.audacityteam.org/), gratuito | 0 € |

## Habitación

- **Elige la habitación más «muerta» de la casa**, la que tenga más tela:
  cortinas, sofá, alfombra, armario con ropa. Un vestidor o un armario abierto
  funcionan muy bien.
- **Apaga neveras, ventiladores y aire acondicionado**, y graba cuando la calle
  esté tranquila.
- **Colócate a 10–15 cm del micrófono**, un poco de lado, y mantén siempre la
  misma distancia.

## Ajustes en Audacity

1. Frecuencia de 48.000 Hz, 1 canal (mono).
2. Ajusta la ganancia hasta que, leyendo en el tono del episodio, los picos
   lleguen a unos **−12 dB** en el medidor. Si suben por encima de −6 dB, baja
   la ganancia.
3. Antes de empezar a leer, deja **5 segundos de silencio** grabados. Sirven para
   medir el ruido de fondo.
4. Exporta cada capítulo como **WAV o FLAC** con el nombre exacto que indica la
   versión para grabar: `cap00.wav` (bienvenida), `cap01.wav`… `cap14.wav`.

## Cómo leer

- **Lee de la [versión para grabar](../produccion/ep01/lectura.md).** Los
  párrafos van numerados (por ejemplo **3.7**) y las pausas largas están marcadas.
- **Tono:** grave, cálido, más lento que una conversación (unas 110–120 palabras
  por minuto), como si se lo contaras a alguien que está a punto de dormirse. Sin
  énfasis teatral.
- **Pausas:** un respiro tranquilo entre párrafos y 2–3 segundos en cada «pausa
  larga». No hace falta cronometrarlas: el montaje acorta las que se pasen.
- **Cansancio:** graba como mucho 3–4 capítulos seguidos. La voz cansada se nota
  y cambia de color entre capítulos.
- **Agua:** ten un vaso de agua a mano. Bebe en las pausas largas, no a mitad de
  frase.

## Si te equivocas

**No pares la grabación.** Haz esto:

1. Quédate **2 segundos en silencio**.
2. Da **una palmada fuerte y seca** cerca del micrófono.
3. Quédate **1 segundo en silencio**.
4. Vuelve a leer **el párrafo entero**, desde su número.

El montaje localiza cada palmada, borra el párrafo fallido y la palmada, y deja
la versión buena. Todos los cortes quedan anotados en `informe.txt` con sus
tiempos, para que puedas comprobarlos en Audacity si algo suena raro.

**Lo que confunde al montaje:**

- Dar la palmada sin el silencio de 2 segundos delante.
- Golpear la mesa en lugar de dar una palmada.
- Hacer una pausa de más de un segundo a mitad de un párrafo. El montaje la
  tomaría por el final del párrafo y solo borraría desde ahí.

## Qué hacer con los archivos

Copia los 15 archivos (`cap00`–`cap14`) en una carpeta, por ejemplo
`grabaciones/ep01/`. Los pasos siguientes están en
[`../herramientas/montaje/README.md`](../herramientas/montaje/README.md).
