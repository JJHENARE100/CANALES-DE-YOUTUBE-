# Canales de YouTube

**Objetivo:** crear y monetizar canales de YouTube antes del **15 de enero de 2027**.

Hay una razón para correr. El **1 de febrero de 2027** YouTube duplica los
requisitos de entrada al Programa de Partners para los canales nuevos: pasan de
4.000 h a **8.000 h**, o de 10 M a **20 M** de vistas de Shorts, siempre con
1.000 suscriptores ([fuente oficial](https://support.google.com/youtube/answer/12843009?hl=en)).
Como la revisión tarda alrededor de un mes, **la solicitud tiene que salir entre
el 10 y el 20 de diciembre de 2026**.

## Decisión

**Dos canales desde ya** (decisión del 2 de octubre), los dos con más tirón de
la [comparativa](docs/analisis-nichos.md#4-comparativa-de-nichos):

1. **Historia para dormir**, en español: episodios de 90–150 min.
2. **Ciencia y espacio**, en español: documentales de 40–90 min.

En los dos:

- **Narración:** **tu voz grabada**, o tu clon cuando no haya tiempo de grabar
  (en ese caso, declarado como IA).
- **Guion** investigado y con fuentes.
- **Apoyo:** Shorts para captar suscriptores y doblaje automático al inglés.

Cada canal necesita por su cuenta 4.000 h y 1.000 suscriptores. El montaje
automático (`herramientas/montaje/`) reduce el trabajo por episodio a revisar el
guion, grabarlo y generar las imágenes.

## Documentos

| Documento | Para qué |
|---|---|
| [`docs/analisis-nichos.md`](docs/analisis-nichos.md) | Reglas del YPP en 2026–2027, aritmética de horas, política de contenido no auténtico, comparativa puntuada de 10 nichos, recomendación, probabilidad realista y riesgos |
| [`docs/plan-ejecucion.md`](docs/plan-ejecucion.md) | Calendario con puertas de decisión, semana 0, ritmo semanal, primeros episodios, presupuesto y lista previa a la solicitud |
| [`guiones/`](guiones/) | Guiones de los episodios, con la lista de hechos que hay que comprobar, título, descripción e ideas para Shorts |
| [`docs/canal-ciencia.md`](docs/canal-ciencia.md) | Canal de ciencia y espacio: formato, nombres, imágenes reales y calendario hasta el 24 de diciembre |
| [`docs/grabacion.md`](docs/grabacion.md) | Cómo grabar con tu voz: material, ajustes y la palmada para marcar errores |
| [`herramientas/montaje/`](herramientas/montaje/) | Exportar el guion, editar el audio y montar el vídeo 1080p con ffmpeg |
| [`produccion/ep01/`](produccion/ep01/) | Versión para grabar y lista de planos con descripción de imagen del episodio 1 |
| [`herramientas/ritmo_ypp.py`](herramientas/ritmo_ypp.py) | Calcula qué ritmo diario de horas, visitas y suscriptores hace falta para llegar a tiempo |

```
python3 herramientas/ritmo_ypp.py --horas 850 --subs 240 --minutos-por-visita 22
```

## Reglas del proyecto

1. No se publica ningún guion sin revisión humana de los hechos.
2. Las fuentes van en la descripción de cada episodio. Si la narración sale de
   tu clon de voz, se indica que está generada con IA.
3. Ningún personaje IA se presenta como experto, y no se tocan salud, finanzas,
   derecho ni política con voz IA.
4. Nada de sub4sub, compra de visitas o bots.
5. No se borran ni se ponen en privado vídeos que ya han sumado horas.
