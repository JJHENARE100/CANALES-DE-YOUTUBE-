# Cómo aplicamos la lógica de un recomendador (TikTok, YouTube) a los canales

Partimos de una investigación sobre el algoritmo de TikTok, aportada el 6 de
octubre de 2026. Ese algoritmo funciona como un ciclo:

1. recoge señales;
2. construye perfiles;
3. busca candidatos;
4. predice;
5. ordena con diversidad y exploración;
6. vuelve a aprender.

**No vamos a construir una plataforma:** nuestros canales viven dentro del
recomendador de YouTube, que sigue la misma lógica. La investigación se aplica de
dos formas:

1. **Diseñar los vídeos para las señales que mide YouTube.**
2. **Montar nuestro propio mini-recomendador de decisiones**
   ([`herramientas/analitica/motor.py`](../herramientas/analitica/motor.py)).
   Aprende cada semana de nuestros datos qué temas hacer y qué arreglar, con
   exploración y diversidad.

Las obligaciones del Reglamento de Servicios Digitales sobre transparencia del
recomendador son para las plataformas, no para los creadores. No nos aplican.

## Qué dice YouTube de su propio sistema

- **Aprende a diario** de más de 80.000 millones de señales. Su objetivo es la
  **satisfacción a largo plazo** del espectador, no solo los clics
  ([ayuda de YouTube](https://support.google.com/youtube/answer/16089387?hl=en)).
- **Mide tres cosas de cada vídeo**
  ([rendimiento en el recomendador](https://support.google.com/youtube/answer/16559650?hl=en)):
  - **atractivo:** ¿lo eligen o lo ignoran?
  - **compromiso:** ¿se quedan viendo?
  - **satisfacción:** me gusta y encuestas tras el vídeo.
- **Arquitectura publicada:** primero **selecciona candidatos** (cientos entre
  miles de millones) y después los **ordena** según el tiempo de visualización
  esperado ([Covington et al., 2016](https://blog.acolyer.org/2016/09/19/deep-neural-networks-for-youtube-recommendations/)).
  Más tarde pasó a ordenar combinando compromiso y satisfacción
  ([Zhao et al., 2019](https://daiwk.github.io/assets/youtube-multitask.pdf)).
  Los pesos reales no son públicos.

## Fase por fase: qué hacemos

| Fase del recomendador | Qué mira YouTube | Qué hacemos | Cómo lo medimos |
|---|---|---|---|
| **Señales** | Historial, búsquedas, suscripciones, me gusta, «no me interesa» | Exportar YouTube Studio cada lunes a `docs/datos/` | Exportación CSV de Studio (modo avanzado) |
| **Perfil del contenido** | Tema, idioma, metadatos, a quién gustan vídeos parecidos | Un solo idioma y un tema claro por canal; **series** reconocibles; ángulo hispano, que da contexto de idioma y ubicación | Columna `serie` de [`temas_candidatos.csv`](datos/temas_candidatos.csv) |
| **Candidatos** (¿a quién se le enseña?) | Relación con lo que ya ve la gente y con lo que busca | Títulos con el término que la gente busca (validado en [`validacion-temas.md`](validacion-temas.md)); listas de reproducción por serie; pantalla final hacia un solo vídeo siguiente | `motor.py diagnostico`: «CANDIDATOS» = pocas impresiones aunque guste |
| **Predicción: atractivo** | ¿Lo elige o lo ignora? (CTR) | Miniatura y título con la fórmula que funciona en el nicho; 2 variantes en «Probar y comparar» | «ATRACTIVO» = CTR < 80% de la mediana del canal |
| **Predicción: compromiso** | Tiempo visto y % visto | Promesa del título cumplida en el primer minuto; capítulos; ritmo pausado pero con hilo narrativo | «RETENCIÓN» = % visto < 80% de la mediana |
| **Predicción: satisfacción** | Me gusta, encuestas, volver al canal | **Nada de *clickbait***: un título que engaña sube el CTR y hunde la satisfacción. En vídeos para dormir, pocos anuncios a mitad de vídeo | Me gusta por 1.000 visualizaciones y espectadores que vuelven (Studio) |
| **Diversidad y exploración** | Prueba vídeos nuevos con públicos pequeños; no repite siempre lo mismo | No borrar ni volver a subir un vídeo porque tarde en despegar (a menudo despega semanas después); alternar series | `motor.py siguiente`: cuota de exploración y penalización por repetir serie |
| **Aprender** | Cada interacción cambia lo siguiente | **Bucle semanal** (abajo) | `motor.py` + `ritmo_ypp.py` |

## Arranque en frío (canal sin historial)

Igual que un recomendador con un usuario o un vídeo nuevo, un canal nuevo no
tiene datos. Se compensa así:

1. **Búsqueda:** títulos con demanda medida, porque la búsqueda funciona sin
   historial.
2. **Shorts:** su feed, parecido al de TikTok, enseña vídeos a desconocidos. Cada
   Short enlaza al episodio largo.
3. **Series:** el recomendador encadena vídeos parecidos. Una serie le da
   candidatos obvios para el «siguiente vídeo».

## Shorts: diseñados para un feed tipo TikTok

En el feed de Shorts pesan sobre todo el **% visto**, las **repeticiones** y
**deslizar para pasar**. Reglas para cada Short:

- **Gancho en el primer segundo y medio:** una pregunta o una imagen que intrigue
  («¿Por qué decimos siesta?»).
- **20–45 segundos, una sola idea.** Si caben dos ideas, son dos Shorts.
- **El final enlaza con el principio** para que se repita de forma natural.
- **Texto en pantalla:** mucha gente lo ve sin sonido.
- **«Vídeo relacionado» apuntando al episodio largo.** El Short es la puerta, no
  el producto.

## Vídeos largos para dormir: el equilibrio

- **A favor:** el contenido para dormir genera sesiones larguísimas, que es lo
  que optimiza la ordenación por tiempo de visualización.
- **El riesgo es la satisfacción:**
  - **Anuncios:** demasiados anuncios a mitad de vídeo despiertan al espectador y
    provocan malas valoraciones.
  - **Promesas:** si el título promete algo que no se cumple, también se valora
    mal.
- **Calidad por encima de la duración:** YouTube premia el tiempo «valioso», no
  la duración en sí. Por eso los episodios duran 90–119 min y no 3 horas: más
  largo no daba ventaja en los datos del nicho.

## Bucle semanal (cada lunes, 20 minutos)

1. Exportar de Studio (Estadísticas → Modo avanzado → Exportar) un CSV por canal
   y guardarlo en `docs/datos/studio_<canal>_<fecha>.csv`.
2. Diagnosticar cada vídeo:
   ```
   python3 herramientas/analitica/motor.py diagnostico --studio docs/datos/studio_historia_2026-10-19.csv
   ```
   Arreglar lo que diga: miniatura si falla el **atractivo**, el primer minuto
   de los siguientes guiones si falla la **retención**, título y metadatos si
   fallan los **candidatos**.
3. Decidir los próximos temas:
   ```
   python3 herramientas/analitica/motor.py siguiente --temas docs/datos/temas_candidatos.csv --canal historia --studio docs/datos/studio_historia_2026-10-19.csv
   ```
   - Los temas con fecha fija (la Voyager, la estrella de Belén) van anclados al
     calendario.
   - El resto se ordena según lo aprendido por serie, la demanda, la saturación,
     la exploración y la diversidad.
4. Cuando se publique un vídeo, poner `estado = publicado` y una parte del título
   en `titulo_publicado`, para que el motor aprenda de su serie.
5. Actualizar el ritmo hacia el YPP con `ritmo_ypp.py`.

**El 20 de octubre:**
```
python3 herramientas/analitica/motor.py puerta --canal historia=… --canal ciencia=… --horas-trabajo historia=18 --horas-trabajo ciencia=14
```
Aplica la fórmula de la puerta del plan (35/25/20/10/10). Si la diferencia entre
canales es menor del 10%, recomienda esperar 7 días.

## Límites

- **Con 2–4 vídeos por canal, los datos son escasos.** El motor encoge lo
  aprendido hacia la media del canal y no juzga un vídeo con menos de 1.000
  impresiones. No reacciones a un solo vídeo.
- **Es una ayuda para decidir, no un piloto automático:** el calendario lo
  aprueba una persona.
- **No conocemos los pesos reales de YouTube.** El motor usa las señales que
  YouTube dice medir, con los pesos que fijamos en el plan.
