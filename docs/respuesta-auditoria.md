# Respuesta a la auditoría externa del 2 de octubre de 2026

Auditoría: [`auditoria-externa-2026-10-02.md`](auditoria-externa-2026-10-02.md).
Resumen: se acepta casi todo. Hay **dos correcciones a la auditoría**,
comprobadas en fuentes, y **un punto que se resuelve de otra forma**.

## Aceptado y aplicado

| Punto | Dónde se ha aplicado |
|---|---|
| Pilotos con puerta el 20 de octubre y 70–80% del tiempo al ganador, con la fórmula de puntuación | [`plan-ejecucion.md`](plan-ejecucion.md), tabla de hitos y [`README`](../README.md) |
| Solicitud entre el 30 de noviembre y el 10 de diciembre; el 15 de enero es la fecha de aceptación | Plan, README, [`analisis-nichos.md`](analisis-nichos.md) y valores por defecto de `ritmo_ypp.py` |
| Escenario base: un canal monetizado; los dos a la vez, escenario optimista | Plan y análisis (escenarios en lugar de una probabilidad) |
| Controles del 2 de noviembre (≥ 50%) y del 16 de noviembre (≥ 75%) con proyección de 7 y 14 días | Plan y `herramientas/ritmo_ypp.py` |
| Semana de auditoría del canal antes de solicitar | Plan §5 |
| Separar el calendario editorial del de monetización | Plan: la tabla de hitos es el calendario de monetización |
| Separar *fan funding* de anuncios | Plan (tras la tabla de hitos) y análisis §1 |
| La regla de no borrar vídeos era demasiado absoluta | README, regla 6, y plan §5 |
| Doblaje automático: no funciona en vídeos de 120 min o más | Comprobado ([ayuda de YouTube](https://support.google.com/youtube/answer/15569972?hl=en), [ppc.land](https://ppc.land/auto-dubbing/)). Historia pasa a 90–119 min; `video.py` y `ritmo_ypp.py` avisan. Los episodios 1 (~90 min) y 2 (~95 min) cumplen |
| Ciencia: 45–70 min de entrada | [`canal-ciencia.md`](canal-ciencia.md). Los episodios 1 (~50 min) y 2 (~60 min) cumplen |
| Copyright y política de contenido reutilizado son cosas distintas | Análisis §3 y plan §5 |
| Registro de procedencia de cada imagen, créditos automáticos y bloqueo si falta la licencia | `planos.csv` tiene ahora `fuente`, `licencia`, `atribucion` y `url`; `video.py` genera `creditos.txt` y se detiene si falta algo (salvo `--borrador`) |
| Más variedad de planos | `video.py`: 7 movimientos, elegidos sin repetir el anterior, y columna `movimiento` para fijar uno |
| Pantalla final | `video.py --pantalla-final 20` |
| Distinguir observación real, ilustración y IA | `canal-ciencia.md` y lista de control de cada guion |
| Claqueta, conservar el audio bruto y el proyecto, consentimiento del clon | [`grabacion.md`](grabacion.md) y `audio.py --claqueta` |
| Promesa, pregunta central y control de publicación en cada guion | Los cuatro guiones: cabecera y nueva sección «Control de publicación» |
| Lo que la medición de temas no permite saber y protocolo ampliado | [`validacion-temas.md`](validacion-temas.md) |
| Calculadora por canal, con proyección a 7, 14 y 28 días, fechas de solicitud y aceptación y avisos de 8.000 h y 120 min | `herramientas/ritmo_ypp.py`, reescrita y probada con un historial de prueba |
| Modelo de negocio: 55% de los anuncios, Premium, fórmulas con datos reales y segunda fuente de ingresos solo tras demostrar audiencia | Plan §6 |
| Reglas revisadas (8 reglas) | README |

## Correcciones a la auditoría

1. **Voz clonada propia.** La auditoría dice que el clon de voz se debe marcar
   como contenido alterado. Para la voz **propia** no es así: YouTube pone
   «clonar tu propia voz para hacer locuciones o doblajes» entre los ejemplos que
   **no** hay que etiquetar. Solo obliga cuando se clona la voz de otra persona
   ([ytzolo](https://ytzolo.com/blog/youtube-altered-synthetic-content-policy-2026/),
   [syncstudio](https://syncstudio.ai/blog/youtube-synthetic-content-disclosure),
   [ayuda](https://support.google.com/youtube/answer/14328491)). El proyecto
   mantiene, por transparencia, la declaración en la descripción cuando se use
   el clon. La etiqueta de YouTube es opcional en ese caso.
2. **La auditoría no pudo ver el repositorio**, como reconoce en su alcance. Varias
   peticiones ya existían:
   - la lista de comprobación de hechos de cada guion;
   - las ideas de Shorts por episodio (5–8);
   - la cifra de 4.000 h por canal por separado;
   - la exclusión de las horas de Shorts;
   - el aviso del umbral de 8.000 h.

## Resuelto de otra forma

- **«Tres aperturas alternativas por guion».** YouTube no permite comparar
  aperturas: solo títulos y miniaturas, con «Probar y comparar». Por eso cada
  guion trae varias opciones de título y la lista de control pide probar dos
  variantes de título y miniatura. La apertura se ajusta después, con la curva
  de retención del piloto.
- **Subtítulos revisados.** El montaje no puede sincronizar subtítulos con
  precisión sin un modelo de transcripción, y este entorno no puede
  descargarlo. Se usan los subtítulos automáticos de YouTube, corregidos con el
  guion: Studio → Subtítulos → «Sincronizar automáticamente» pegando el texto
  de `lectura.md`.
## Error mío que la auditoría detectó

- **Licencia de las imágenes de ESA:** yo había dicho que ESA publica con CC BY
  4.0, y no es así. Solo sirven sus imágenes marcadas con CC
  BY-SA 3.0 IGO ([condiciones de ESA](https://open.esa.int/image-usage-creative-commons/)).
  Corregido en `canal-ciencia.md`.
