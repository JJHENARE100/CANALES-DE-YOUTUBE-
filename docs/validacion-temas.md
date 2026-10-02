# Validación de temas con datos de YouTube (2 de octubre de 2026)

Se midieron los 21 temas propuestos para saber si tienen demanda y cuánta
competencia hay antes de dedicarles horas. Los datos en bruto están en
[`datos/youtube_demanda_2026-10-02.json`](datos/youtube_demanda_2026-10-02.json).

## Método y límites

- **Datos:** 25 búsquedas en YouTube, en español y desde España, con unos 20
  resultados cada una. De cada vídeo se apuntó el título, el canal, las
  visualizaciones, la antigüedad y la duración.
- **Herramienta:** las búsquedas se hicieron a través de Firecrawl, porque este
  entorno no puede acceder directamente a YouTube ni a Google Trends.
- **Indicadores:**
  - **Demanda:** visualizaciones de los vídeos que ya existen, sobre todo de los
    que tienen menos de 12 meses. Si un vídeo reciente supera las 50.000
    visualizaciones, hay gente buscando ese tema ahora.
  - **Saturación:** vídeos recientes con menos de 2.000 visualizaciones. Muchos
    vídeos así indican que hay clones compitiendo por un público escaso.
- **Límites:**
  - Las visualizaciones son un indicador indirecto, no el volumen de búsqueda.
  - Los resultados estaban localizados en España y sin sesión iniciada; en dos
    búsquedas el proxy salió por Lituania.
  - No se midió el tamaño de los canales.
  - Los temas de telescopios y de estrellas fugaces no se midieron.

## Resultados por búsqueda

En la tabla, «recientes» son los vídeos de menos de 12 meses; las dos últimas
columnas cuentan solo los recientes.

| Búsqueda | Mediana de visualizaciones | Recientes | Recientes ≥ 50.000 | Recientes < 2.000 |
|---|---|---|---|---|
| mitología griega para dormir | 378.000 | 9 | 6 | 1 |
| viaje por el sistema solar | 398.000 | 4 | 4 | 0 |
| universo para dormir | 277.000 | 8 | 7 | 0 |
| sistema solar para dormir | 191.000 | 9 | 4 | 2 |
| la Luna, documental | 182.000 | 7 | 6 | 0 |
| Voyager 1, documental | 143.000 | 10 | 7 | 1 |
| lunas de Júpiter y Saturno | 105.000 | 3 | 0 | 0 |
| tamaño del universo | 92.000 | 14 | 8 | 0 |
| historia aburrida para dormir (genérico) | 63.000 | 13 | 5 | 1 |
| vida de una estrella | 54.000 | 4 | 1 | 0 |
| Egipto para dormir | 44.000 | 13 | 5 | 1 |
| agujeros negros, documental | 43.000 | 7 | 3 | 0 |
| galeón de Manila | 35.000 | 6 | 3 | 1 |
| Marte, documental | 27.000 | 2 | 1 | 0 |
| agujeros negros para dormir | 13.000 | 12 | 2 | 1 |
| Tenochtitlan / aztecas para dormir | 12.000 | 17 / 14 | 4 / 3 | 5 / 3 |
| al-Ándalus / Córdoba | 12.000 | 16 / 7 | 1 / 2 | 6 / 1 |
| Roma para dormir | 10.000 | 10 | 3 | 6 |
| incas para dormir | 9.000 | 13 | 3 | 5 |
| mitología nórdica para dormir | 7.700 | 13 | 0 | 7 |
| vikingos para dormir | 7.000 | 15 | 4 | 6 |
| Constantinopla para dormir | 4.100 | 14 | 2 | 6 |
| estrella de Belén (medido en octubre) | 661 | 11 | 1 | 8 |

## Conclusiones

1. **Ciencia para dormir en español tiene más demanda que historia para dormir.**
   - **Ciencia:** las búsquedas de sistema solar, universo, la Luna y la Voyager
     tienen medianas de entre 140.000 y 400.000 visualizaciones, y casi ningún
     vídeo reciente se queda por debajo de 2.000.
   - **Historia:** en temas genéricos (Roma, vikingos, Constantinopla, mitología
     nórdica) la mediana se queda en unas 4.000–10.000 visualizaciones, y hay
     muchos clones recientes por debajo de 2.000.
   - **Consecuencia:** el canal de ciencia es probablemente el que antes llegará
     a las 4.000 horas. Si una semana hay que elegir, se prioriza ciencia.
2. **Copiar el formato no basta.**
   - Los vídeos del tipo «Un día / Una noche en X | Historia para dormir» de
     canales nuevos se quedan en 100–500 visualizaciones.
   - Ya existían «Un Día en la Antigua Roma» (124 visualizaciones en 4 meses) y
     «Del Caos al Olimpo» (104.000, de un canal ya asentado).
3. **El ángulo hispano está casi vacío en el formato para dormir**, aunque en el
   documental normal rinde mucho: galeón español, 1,2 millones de
   visualizaciones en 3 semanas; caída del Imperio inca, 1,7 millones en 10
   meses. Es el hueco más claro y el criterio con el que se han revisado los
   calendarios.
4. **Fórmulas de título que funcionan:**
   - «¿Qué tan grande es realmente…?»
   - «¿Cómo era un día completo en…?»
   - «Lo que X encontró…»
   - «Por qué es imposible…»
5. **Duración:** los vídeos que mejor funcionan duran entre 1 h 20 min y 2 h
   40 min. Hacer vídeos de 3 o 4 horas no da ventaja.
6. **Actualidad:** Artemis II (851.000 y 634.000 visualizaciones en 5 meses) y la
   Voyager. El episodio de la Voyager se adelanta al 12 de noviembre, antes de
   que se cumpla el día-luz.

## Qué ha cambiado

| Tema original | Veredicto | Ahora |
|---|---|---|
| Un día en la Roma de Trajano | Demanda alta, saturación alta, casi duplicado | Mismo guion con título nuevo: **«El emperador que vino de Hispania»** |
| Córdoba, año 1000 | Demanda media, casi duplicados (961, 929) | Mismo guion con título nuevo: **«Córdoba en tiempos de Almanzor»** |
| Mitología griega, del Caos al Olimpo | Duplicado exacto | **Los mitos griegos de Hispania** (Gerión, las Hespérides, Gadir) |
| Mitología nórdica | Demanda baja, 7 clones | Sustituido: **un día completo en la Castilla medieval** (el modelo, «un día completo en la Edad Media», tiene 1 millón de visualizaciones en 8 meses) |
| Caída de Constantinopla | Demanda baja, saturación alta | Sustituido: **corsarios y piratas** |
| Un invierno vikingo | Fórmula repetida | **Los vikingos en la Península (Sevilla, año 844)** |
| Tenochtitlan | Clones con muy pocas visualizaciones | **Lo que vieron los españoles, según Bernal Díaz** |
| Galeón, Egipto, incas | Hueco | Se mantienen, con ángulo concreto |
| Sistema solar a escala | Demanda alta, nadie lo hace a escala | Mismo guion con título nuevo: **«¿Qué tan grande es REALMENTE…?»** |
| Agujeros negros | Saturado | Mismo guion con título nuevo: **«¿Qué pasaría si la Tierra se convirtiera en un agujero negro?»** |
| Luna, Voyager | Demanda alta | Ángulo español: **Robledo de Chavela y Fresnedillas** |
| Estrellas fugaces | Sin medir | Sustituido: **la estrella más cercana** (familia de «viajes imposibles») |
| Estrella de Belén | Demanda baja en octubre | Se publica el 3 de diciembre, con el ángulo del cometa del año 5 a. C. |

## «¿Recibirán otros la misma idea de Claude?»

- **Lo que no ocurre:** Claude no recuerda otras conversaciones ni comparte lo
  que se habla con otros usuarios.
- **Lo que sí ocurre:** cualquier modelo de IA tiende a sugerir ideas parecidas a
  quien hace preguntas parecidas. Estos datos lo demuestran: «Un día en la
  antigua Roma | Historia para dormir» ya estaba publicado por un canal nuevo,
  con 124 visualizaciones.
- **Cómo se protege este proyecto:**
  1. **Los temas se deciden con datos**, no con la primera idea, y se comprueba
     cada título en YouTube antes de escribir.
  2. **Ángulo propio:** España y Latinoamérica (Itálica, Almanzor, Robledo de
     Chavela, Bernal Díaz), que los clones genéricos no cubren.
  3. **Tu voz real**, que nadie más tiene.
  4. **Guiones con fuentes y datos comprobados**, que es lo contrario del
     contenido genérico.
  5. **Recursos propios:** la maqueta del Sol de un metro y la Tierra hecha
     canica son ideas que vertebran el canal y que nadie más usa.

## Lo que esta medición no permite saber (auditoría del 2 de octubre)

- **Faltan datos de los resultados:** el tamaño de cada canal, su frecuencia de
  publicación, los comentarios por 1.000 visualizaciones y el formato de
  miniatura.
- **No separa la demanda de búsqueda de la de recomendación.** Eso solo lo da
  YouTube Studio una vez publicados los vídeos (Fuentes de tráfico → Búsqueda de
  YouTube frente a Funciones de exploración y Vídeos sugeridos).
- **Las visualizaciones acumuladas mezclan antigüedad e interés actual.** Por
  eso se usan sobre todo los vídeos de menos de 12 meses.

## Protocolo para cada tema nuevo (antes de escribir)

Para cada búsqueda se anotan, en `docs/datos/`: fecha, país e idioma, consulta
exacta, URL de los 10 primeros resultados, visualizaciones, fecha de
publicación, duración y, si se puede, tamaño del canal y frecuencia reciente.

1. Buscar en YouTube 2 o 3 formas de preguntar por el tema, en español.
2. Anotar:
   - los vídeos de menos de 12 meses con más de 50.000 visualizaciones (indican
     demanda);
   - los de menos de 2.000 visualizaciones (indican saturación);
   - cualquier título casi igual al previsto.
3. **Decidir:**
   - Si hay demanda y no hay duplicado, se escribe.
   - Si hay demanda y algún duplicado, se cambia el ángulo.
   - Si no hay demanda, se sustituye el tema.
4. Revisar cada 4–6 semanas con YouTube Studio: las búsquedas que traen
   visualizaciones a tus vídeos son el mejor dato que habrá a partir de ahora.
