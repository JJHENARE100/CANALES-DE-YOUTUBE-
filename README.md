# Canales de YouTube

**Objetivo:** crear y monetizar canales de YouTube antes del **15 de enero de 2027**.

Hay una razón para correr. El **1 de febrero de 2027** YouTube duplica los
requisitos de entrada al Programa de Partners para los canales nuevos: pasan de
4.000 h a **8.000 h**, o de 10 M a **20 M** de vistas de Shorts, siempre con
1.000 suscriptores ([fuente oficial](https://support.google.com/youtube/answer/12843009?hl=en)).
Como la revisión tarda alrededor de un mes, **la solicitud tiene que salir entre
el 30 de noviembre y el 10 de diciembre de 2026**.

## Decisión

**Dos canales como pilotos y un canal principal desde el 20 de octubre.**
Revisado tras la [auditoría externa](docs/auditoria-externa-2026-10-02.md)
([respuesta](docs/respuesta-auditoria.md)):

1. **Historia para dormir**, en español: episodios de 90–119 min. A partir de 120
   min no hay doblaje automático.
2. **Ciencia y espacio**, en español: documentales de 45–70 min de entrada.

- **20 de octubre:** con los datos de los dos primeros episodios de cada canal se
  elige el **canal principal**, que se lleva el 70–80% del tiempo.
- **Escenario base:** monetizar un canal antes del cambio de febrero.
- **Solicitud del YPP:** entre el **30 de noviembre y el 10 de diciembre**. El 15
  de enero es la fecha de aceptación.
- **Validación de temas:** ciencia mostró más demanda que historia.

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
| [`docs/auditoria-externa-2026-10-02.md`](docs/auditoria-externa-2026-10-02.md) · [`docs/respuesta-auditoria.md`](docs/respuesta-auditoria.md) | Auditoría externa del 2 de octubre y qué se ha hecho con cada punto |
| [`docs/rpm-y-audiencia.md`](docs/rpm-y-audiencia.md) | CPM y RPM por país y por nicho, de dónde vendrá la audiencia y RPM combinado esperado de cada canal |
| [`docs/validacion-temas.md`](docs/validacion-temas.md) | **Demanda y competencia medidas en YouTube** para los 21 temas, qué ha cambiado y el protocolo para validar cada tema nuevo |
| [`docs/canal-ciencia.md`](docs/canal-ciencia.md) | Canal de ciencia y espacio: formato, nombres, imágenes reales y calendario hasta el 24 de diciembre |
| [`docs/grabacion.md`](docs/grabacion.md) | Cómo grabar con tu voz: material, ajustes y la palmada para marcar errores |
| [`herramientas/montaje/`](herramientas/montaje/) | Exportar el guion, editar el audio y montar el vídeo 1080p con ffmpeg |
| [`produccion/`](produccion/) | Por episodio: versión para grabar y `planos.csv` (descripción, fuente y licencia de cada imagen) |
| [`herramientas/ritmo_ypp.py`](herramientas/ritmo_ypp.py) | Calcula qué ritmo diario de horas, visitas y suscriptores hace falta para llegar a tiempo |

```
python3 herramientas/ritmo_ypp.py --horas 850 --subs 240 --minutos-por-visita 22
python3 herramientas/ritmo_ypp.py --historial docs/datos/ritmo.csv   # por canal, con proyección a 7, 14 y 28 días
```

## Reglas del proyecto

1. Ningún guion se publica sin revisión humana de hechos, pronunciación,
   derechos y contexto (lista «Control de publicación» de cada guion).
2. Las fuentes van en la descripción. Cada imagen real lleva además su
   atribución y licencia, en `planos.csv` y `creditos.txt`.
3. Si la narración sale de tu clon de voz, se declara en la descripción.
4. Ningún personaje IA se presenta como experto, y no se tocan salud, finanzas,
   derecho ni política con voz IA.
5. Nada de sub4sub, bots, compra de visitas ni tráfico incentivado engañoso.
6. No se borra ni se pone en privado contenido para manipular métricas. Sí se
   retira o corrige lo que tenga riesgo de política, copyright o autenticidad,
   aunque sus horas dejen de contar.
7. No se publica ningún episodio que solo se diferencie de otro en lo
   superficial (estructura, imágenes o narración).
8. Cada episodio conserva su expediente: guion, fuentes, audio bruto, imágenes,
   licencias, proyecto y revisión final.
