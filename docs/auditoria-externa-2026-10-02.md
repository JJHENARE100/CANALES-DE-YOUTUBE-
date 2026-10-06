# Auditoría del proyecto de dos canales de YouTube y plan de monetización antes del 15 de enero de 2027

## Dictamen ejecutivo

El planteamiento es **viable como negocio editorial de bajo coste**, pero **no es prudente asumir que dos canales nuevos quedarán monetizados antes del 15 de enero de 2027**. El principal problema no es la producción: es lograr, en cada canal por separado, 1.000 suscriptores, 4.000 horas públicas válidas y superar la revisión integral del YPP en poco más de tres meses.

La urgencia es real. Hasta el 31 de enero de 2027, un solicitante nuevo puede entrar al reparto de anuncios con 1.000 suscriptores y 4.000 horas públicas válidas durante los 365 días anteriores; desde el 1 de febrero de 2027 el umbral para nuevos solicitantes se duplica a 8.000 horas o 20 millones de visualizaciones de Shorts, manteniéndose los 1.000 suscriptores. Haber alcanzado el contador no equivale a estar monetizado: YouTube revisa el canal completo y comunica la decisión normalmente en aproximadamente un mes, aunque puede tardar más.[^1][^2][^3][^4]

La recomendación central es **lanzar ambos conceptos como pilotos, escoger un canal principal antes del 20 de octubre y concentrar en él entre el 70% y el 80% de la capacidad**. El segundo canal solo debe continuar a ritmo completo si demuestra, con datos reales, que puede sostener su propia trayectoria hacia 4.000 horas y 1.000 suscriptores sin reducir la calidad del principal.

## Alcance de la auditoría

Esta auditoría verifica el contenido reproducido en la consulta y las reglas oficiales vigentes a 2 de octubre de 2026. Los archivos enlazados —incluidos los 21 temas, guiones, código y mediciones de YouTube— no están adjuntos ni accesibles en el entorno de revisión; por ello **no es posible certificar línea por línea** `docs/analisis-nichos.md`, `docs/validacion-temas.md`, `herramientas/ritmo_ypp.py` o los guiones.

Tampoco puede validarse que la demanda y la competencia de los 21 temas se hayan medido correctamente sin ver consultas, fecha, país, URLs, impresiones, visualizaciones, antigüedad de vídeos y metodología. El dictamen sobre mercado es, por tanto, condicional: valida la arquitectura del negocio y señala las pruebas que faltan, pero no sustituye la auditoría del repositorio.

## Qué es correcto

| Afirmación o regla | Dictamen | Ajuste necesario |
|---|---|---|
| Cada canal necesita 4.000 horas y 1.000 suscriptores | Correcto para ingresos por anuncios si se solicita antes del 1 de febrero de 2027[^4] | Añadir que el acceso inicial a financiación de fans exige 500 suscriptores, tres publicaciones públicas en 90 días y 3.000 horas; no desbloquea anuncios de la página de reproducción[^5][^6]. |
| Las horas son independientes por canal | Correcto | No sumar audiencia, horas o suscriptores de ambos canales en el plan financiero. |
| Shorts para captar suscriptores | Correcto como embudo | Las horas del feed de Shorts no cuentan para las 4.000; deben llevar a vídeos largos[^7][^8]. |
| Voz propia o clon declarado | Enfoque correcto | Cuando se use un clon realista, marcar también “contenido alterado” durante la subida; YouTube incluye la clonación de voz entre los supuestos de contenido sintético que deben declararse[^9][^10]. |
| Guiones investigados y con fuentes | Correcto y diferenciador | Incorporar una matriz de afirmación–fuente–fecha–revisor, no solo una bibliografía general. |
| Ningún guion sin revisión humana | Correcto | La revisión debe cubrir hechos, pronunciación, derechos de imágenes, música, miniatura y afirmaciones de actualidad. |
| No usar bots, compra de visitas o sub4sub | Correcto | Mantenerlo como prohibición absoluta y conservar trazabilidad del tráfico pagado u orgánico. |
| No tratar temas sensibles mediante un personaje IA que simule ser experto | Correcto | YouTube considera no monetizables los canales donde personajes IA se presentan como expertos humanos en salud, finanzas, derecho o política[^11]. |
| No borrar ni privatizar vídeos que aportaron horas | Demasiado absoluto | Los vídeos privados, ocultos o borrados dejan de aportar horas; pero YouTube recomienda editar o eliminar contenido infractor antes de volver a solicitar monetización[^7][^12]. La regla debe permitir retirar contenido con riesgos de política o copyright. |

## Cambios críticos de 2027

El documento debe destacar en su primera página que **la fecha operativa importante no es el 15 de enero, sino aproximadamente el 30 de noviembre–10 de diciembre de 2026**. Para aspirar a una aceptación antes del 15 de enero hay que alcanzar los umbrales y enviar la solicitud con margen para una revisión que normalmente dura alrededor de un mes. Presentarla el 15 de diciembre deja margen cero ante cualquier demora.[^1]

Desde el 1 de febrero de 2027, los nuevos solicitantes necesitarán 8.000 horas válidas en 365 días o 20 millones de visualizaciones válidas de Shorts en 90 días, además de 1.000 suscriptores. Los canales que ya estén dentro del YPP no quedan sujetos al nuevo umbral de entrada, aunque deberán aceptar los términos actualizados antes del 31 de enero de 2027.[^2][^3][^4]

## Aritmética del objetivo

Tomando el 30 de noviembre como fecha recomendada para solicitar, hay aproximadamente 60 días desde el 2 de octubre. **Cada canal**, desde cero, necesita de media:

| Magnitud por canal | Objetivo total | Ritmo medio hasta 30/11 |
|---|---:|---:|
| Horas públicas válidas | 4.000 | 66,7 horas/día |
| Suscriptores | 1.000 | 16,7 suscriptores/día |
| Vistas largas si la media vista es 22 minutos | 10.910 | 182 vistas/día |
| Vistas largas si la media vista es 35 minutos | 6.857 | 114 vistas/día |
| Vistas largas si la media vista es 50 minutos | 4.800 | 80 vistas/día |

Para los dos canales, el objetivo conjunto equivale a 8.000 horas y 2.000 suscriptores, pero YouTube seguirá evaluando cada canal por separado. Con una duración media vista de 22 minutos serían unas 21.820 visualizaciones largas combinadas; además, haría falta convertir una fracción inusualmente alta de esa audiencia en suscriptores o conseguir suscriptores adicionales mediante Shorts.

Si cada canal publica ocho episodios largos antes del 30 de noviembre, cada episodio debería aportar de media unas 500 horas. Con 22 minutos de visualización media, eso supone aproximadamente 1.364 vistas por episodio; con 35 minutos, unas 857. Esta aritmética es alcanzable para un canal que encuentre distribución, pero no está garantizada para dos canales nuevos y sin audiencia inicial.

## Riesgo de contenido inauténtico

La automatización del montaje no impide monetizar. YouTube permite utilizar IA, pero exige contenido original y auténtico y excluye material genérico, repetitivo o producido en masa; la política menciona expresamente como señales de riesgo las historias narradas con diferencias superficiales y las presentaciones de diapositivas repetidas.[^13][^11][^14]

El riesgo no se resuelve únicamente usando voz humana. Un canal con idéntica estructura, cadencia visual, música, miniaturas y arcos narrativos puede parecer producido mediante plantilla aunque la narración sea propia. Cada episodio debe mostrar decisiones editoriales visibles: tesis distinta, investigación específica, mapas o gráficos propios, variedad de secuencias, edición ligada al relato y comentario original.

También deben separarse copyright y elegibilidad YPP. Tener licencia para un clip no garantiza que el canal supere la política de contenido reutilizado; YouTube exige comentario original, modificación sustancial o valor educativo o de entretenimiento claramente añadido.[^15]

## Doblaje y duración

El doblaje automático español–inglés existe para creadores elegibles, pero no debe tratarse como garantizado para cada vídeo. Un vídeo puede quedar excluido si dura más de 120 minutos, contiene reclamaciones de Content ID, tiene poco diálogo, el idioma no se detecta o el habla es demasiado rápida.[^16][^17]

Esto obliga a cambiar el formato de “Historia para dormir: 90–150 minutos”. Si el doblaje automático es parte central de adquisición, la duración estándar debe ser **90–119 minutos**, dejando 119:30 como límite técnico prudente. Los especiales de 120–150 minutos deberán asumir doblaje manual o publicarse sin pista inglesa.

La pista inglesa debe permanecer en el mismo vídeo mediante audio multilingüe, no duplicarse como otro vídeo casi idéntico. YouTube también permite subir pistas dobladas propias cuando el canal tiene funciones avanzadas.[^18]

## Evaluación de los canales

| Dimensión | Historia para dormir | Ciencia y espacio |
|---|---|---|
| Potencial de horas | Alto si la audiencia escucha durante periodos largos | Medio–alto; depende más de retención y encadenamiento de vídeos |
| Potencial de suscripción | Medio–bajo: parte del consumo es pasivo | Medio–alto: la promesa editorial y el presentador pueden crear hábito |
| Riesgo YPP | Alto si parece una fábrica de relatos con imágenes genéricas | Medio si hay investigación, explicación original y edición específica |
| Carga de investigación | Media–alta | Alta; requiere control factual y actualización científica |
| Riesgo de derechos | Música, obras adaptadas, grabaciones y arte histórico | Imágenes, animaciones, música y material de agencias espaciales |
| Ventaja principal | Duración y uso en segundo plano | Mejor conversión potencial a suscriptor y mayor identidad de marca |
| Cambio recomendado | 90–119 minutos; historias reales muy diferenciadas y series temáticas | 45–70 minutos inicialmente; usar formatos de 80–90 solo cuando la retención lo justifique |

El canal de historia es el candidato más natural para acumular horas, pero también el más expuesto a parecer una plantilla automatizada y a convertir peor a suscriptor. Ciencia y espacio ofrece mejor oportunidad de marca, búsqueda, series y patrocinio futuro, aunque exige más control editorial.

## Derechos de imágenes

Para ciencia y espacio, priorizar NASA, material propio, dominio público y licencias comerciales verificadas. NASA permite normalmente el uso factual de sus materiales educativos o informativos, exige reconocer la fuente y prohíbe insinuar respaldo; además, cada activo debe comprobarse porque algunos incorporan derechos de terceros y los logotipos tienen protección específica.[^19][^20][^21]

No debe asumirse que todo material de ESA es reutilizable comercialmente. La fototeca de ESA limita sus activos a usos educativos, editoriales o informativos, exige créditos y excluye usos comerciales sin licencia específica; algunos elementos pertenecen a terceros y pueden necesitar autorización separada.[^22][^23]

En Wikimedia Commons hay que revisar la ficha de cada archivo: autor, licencia, atribución, enlace a la licencia, modificaciones y, cuando corresponda, obligación de compartir derivados bajo la misma licencia. El montaje debería generar automáticamente un registro de procedencia y créditos por plano.[^24][^25]

## Modelo de negocio

El modelo puede funcionar si se trata como una **cartera de propiedad intelectual editorial**, no como arbitraje de anuncios mediante vídeos automáticos. Los episodios largos permiten anuncios intermedios a partir de ocho minutos y YouTube reparte al creador el 55% de los ingresos netos de anuncios de la página de reproducción. YouTube Premium añade ingresos distribuidos en función de cuánto consumen los miembros el contenido, incluido el tiempo reproducido en segundo plano.[^26][^27][^28]

Sin datos reales de RPM, coste por episodio, horas humanas, visualizaciones y retención no puede afirmarse rentabilidad. La cuenta mínima por canal debe ser:

- Ingresos mensuales = vistas monetizadas / 1.000 × RPM real del canal.
- Margen de contribución = ingresos totales − coste de guion − voz − recursos visuales − software − revisión.
- Recuperación = inversión acumulada / margen mensual.

El plan debe contemplar una segunda capa de ingresos compatible con cada audiencia: afiliación editorial o astronómica, patrocinios, membresías y catálogo de audio. Estas vías deben probarse después de demostrar audiencia; no deben inflar las previsiones previas al YPP.

## Estrategia recomendada

### Fase piloto: 2–19 octubre

- Publicar dos episodios largos por canal, no ocho de golpe.
- Crear entre cuatro y seis Shorts por episodio con una promesa completa, no simples recortes sin contexto.
- Mantener la voz humana en todos los pilotos para evaluar la propuesta sin introducir el riesgo adicional del clon.
- Probar dos familias de título y miniatura por canal.
- Registrar por vídeo: impresiones, CTR, duración media vista, horas por 1.000 impresiones, suscriptores por 1.000 vistas, fuente de tráfico y retornos de audiencia.

YouTube indica que las recomendaciones dependen de la respuesta y satisfacción de la audiencia, no solo de la duración; utiliza señales como historial, clics, tiempo visto, valoraciones y encuestas de satisfacción. La propia plataforma sitúa el CTR de aproximadamente la mitad de canales y vídeos entre 2% y 10%, pero advierte que debe interpretarse según fuente de tráfico, volumen de impresiones y duración media, no como un objetivo universal.[^29][^30][^31][^32]

### Puerta 1: 20 octubre

Seleccionar un canal principal mediante una puntuación relativa, sin inventar un umbral universal:

- 35%: horas por cada 1.000 impresiones.
- 25%: suscriptores por cada 1.000 vistas.
- 20%: duración media vista y curva de retención.
- 10%: CTR estabilizado por fuente.
- 10%: coste y tiempo humano por hora pública conseguida.

Si ninguno muestra distribución creciente, no escalar la producción: rehacer promesa, miniatura, apertura y selección de temas. Si uno supera claramente al otro, dedicarle el 70%–80% de recursos y mantener el segundo con un episodio cada dos semanas.

### Fase de escala: 21 octubre–30 noviembre

- Canal principal: dos episodios largos por semana y entre seis y diez Shorts semanales.
- Canal secundario: un episodio semanal solo si mantiene trayectoria propia; en caso contrario, uno quincenal.
- Publicar secuelas de los temas que ya hayan demostrado impresiones, retención y suscripción.
- Encadenar cada episodio con pantalla final, comentario fijado y primera línea de descripción hacia una única siguiente pieza.
- Revisar semanalmente el ritmo necesario con datos de horas válidas, no con tiempo total de reproducción indiscriminado.

### Solicitud YPP: 30 noviembre–10 diciembre

Antes de solicitar, el canal debe tener AdSense preparado, verificación en dos pasos, acceso a funciones avanzadas, ausencia de faltas activas y cumplimiento integral de políticas. La revisión analiza el canal como conjunto, por lo que la calidad y procedencia de los vídeos marginales también importa.[^11][^33][^8][^1]

No conviene esperar al 15 de diciembre salvo que el canal aún no cumpla el umbral. Una primera denegación puede exigir esperar 30 días para volver a solicitar, y las posteriores 90 días; eso vuelve prácticamente imposible entrar antes del cambio de febrero si la primera solicitud se presenta tarde.[^34]

## Hitos de control

| Fecha | Canal principal | Decisión |
|---|---:|---|
| 20 octubre | Datos suficientes de cuatro pilotos totales | Elegir canal principal y propuesta ganadora |
| 2 noviembre | Trayectoria aproximada ≥ 50% del objetivo lineal | Mantener escala; si no, concentrar aún más recursos |
| 16 noviembre | Trayectoria aproximada ≥ 75% | Preparar auditoría YPP y AdSense |
| 30 noviembre | 1.000 suscriptores y 4.000 horas válidas | Solicitar inmediatamente |
| 10 diciembre | Última ventana razonable con margen | Solicitar si ya cumple; no añadir contenido dudoso |
| 15 enero 2027 | Objetivo de aceptación, no de solicitud | Si sigue en revisión, continuar publicando contenido original |

Los porcentajes de trayectoria son controles internos, no reglas de YouTube. Deben calcularse con previsión actualizada según la velocidad de los últimos siete y catorce días, porque el crecimiento de canales rara vez es lineal.

## Cambios por documento

### `docs/analisis-nichos.md`

- Añadir el cambio del 1 de febrero de 2027: 8.000 horas o 20 millones de Shorts para nuevos solicitantes, manteniendo 1.000 suscriptores.[^3][^2]
- Separar “acceso inicial YPP” de “reparto de anuncios”.
- Incorporar riesgo de revisión de aproximadamente un mes y de rechazo.
- Sustituir una probabilidad puntual por escenarios condicionados a métricas reales.

### `docs/plan-ejecucion.md`

- Cambiar la fecha objetivo operativa a solicitud entre el 30 de noviembre y el 10 de diciembre.
- Añadir la puerta del 20 de octubre y la concentración 70%–80% en el ganador.
- Incluir una semana de auditoría de canal, derechos y AdSense antes de solicitar.
- Separar calendario editorial de calendario de monetización.

### `docs/validacion-temas.md`

Para cada tema deben constar fecha, país o idioma, consulta exacta, URLs de los diez primeros resultados, visualizaciones, fecha de publicación, duración, tamaño del canal, frecuencia reciente, formato de miniatura, comentarios por 1.000 vistas y presencia de resultados recientes con tracción. La medición debe distinguir demanda de búsqueda, demanda de recomendación y evidencia de suscripción; contar únicamente visualizaciones históricas mezcla antigüedad con interés actual.

### `docs/canal-ciencia.md`

- Establecer 45–70 minutos como formato inicial y usar 80–90 cuando los datos lo justifiquen.
- Añadir registro por activo de fuente, titular, licencia, atribución y URL.
- Diferenciar visualización científica, reconstrucción artística e imagen generada por IA.
- Evitar que imágenes sintéticas realistas parezcan observaciones reales; declarar el contenido alterado cuando corresponda.[^9]

### `docs/grabacion.md`

- Añadir identificación verbal de cada toma, versión y episodio.
- Conservar audio bruto, proyecto y exportación final como prueba de autoría.
- Crear una muestra autorizada separada para el clon de voz y documentar consentimiento y proveedor.

### `guiones/`

Cada episodio debería contener:

- Promesa de audiencia y pregunta central.
- Matriz de hechos verificables con fuente primaria, fecha y revisor.
- Indicaciones de qué partes son reconstrucción, hipótesis o dramatización.
- Lista de activos visuales y licencia.
- Tres aperturas alternativas y entre cuatro y ocho ideas de Shorts.
- Declaración de voz humana o sintética y control final de pronunciación.

### `herramientas/montaje/`

- Generar automáticamente créditos y manifiesto de activos.
- Introducir variación real de planos, mapas, rótulos y ritmo; no una sucesión fija de imágenes.
- Incorporar capítulos, subtítulos revisados y pantalla final.
- Añadir un bloqueo si falta licencia, fuente, declaración IA o revisión humana.

### `herramientas/ritmo_ypp.py`

El programa debería aceptar `--fecha-objetivo`, `--dias-revision`, `--canales`, `--horas-validas`, `--subs`, `--minutos-por-visita` y `--vistas-shorts`. También debe:

- Calcular cada canal por separado.
- Excluir automáticamente las horas de Shorts, campañas, vídeos privados, ocultos o borrados.[^7]
- Mostrar fecha estimada de solicitud y de aceptación.
- Advertir del umbral de 8.000 horas desde el 1 de febrero de 2027.[^2]
- Alertar si un episodio supera 120 minutos y se pretende usar doblaje automático.[^17]
- Proyectar con velocidades de 7, 14 y 28 días, además del promedio total.

## Reglas revisadas

1. Ningún guion se publica sin revisión humana de hechos, pronunciación, derechos y contexto.
2. Las fuentes se incluyen en la descripción; cada activo visual conserva además su atribución y licencia.
3. Si se utiliza voz clonada, se declara en la descripción y se marca contenido alterado o sintético cuando corresponda.
4. Ningún personaje IA se presenta como experto; se excluyen salud, finanzas, derecho y política de formatos con personaje o voz IA.
5. Se prohíben sub4sub, bots, compra de visitas y tráfico incentivado engañoso.
6. No se borra ni privatiza contenido solo para manipular métricas; sí se retira o corrige contenido con riesgo de políticas, copyright o autenticidad, asumiendo que sus horas dejarán de contar.
7. No se publica ningún episodio si su estructura, imágenes y narración solo difieren superficialmente de otros episodios.
8. Todo episodio conserva expediente de producción: guion, fuentes, audio bruto, activos, licencias, proyecto y revisión final.

## Veredicto empresarial

**Sí puede funcionar**, especialmente si la automatización reduce costes sin eliminar las decisiones editoriales humanas. Sin embargo, el objetivo “dos canales nuevos, ambos aceptados antes del 15 de enero” debe clasificarse como **alto riesgo**, no como escenario base.

El escenario base recomendable es monetizar **un canal antes del cambio de febrero** y dejar el segundo validado, con catálogo y datos, para escalar después. Solo debe mantenerse el objetivo doble si, el 20 de octubre, ambos pilotos demuestran simultáneamente adquisición de suscriptores, horas por impresión y coste de producción compatibles con su propia trayectoria a 4.000/1.000.

La ventaja competitiva no será `ffmpeg`, la duración ni el clon de voz. Será la combinación de selección de temas demostrada, voz reconocible, investigación trazable, edición que pruebe autoría y una biblioteca de episodios que consiga que el usuario vea el siguiente vídeo.

---

## References

1. [Overview of the expanded YouTube Partner Program - iPhone & iPad](https://support.google.com/youtube/answer/13429240?hl=en-GB16758081&co=GENIE.Platform=iOS) - We’ve expanded the YouTube Partner Program (YPP) to more creators with earlier access to fan funding...

2. [Updates to the YouTube Partner Program - New earning ...](https://support.google.com/youtube/thread/451804019/updates-to-the-youtube-partner-program-new-earning-opportunities-changes-to-eligibility?hl=en) - Starting Feb. 1, 2027, YPP entry thresholds for new applicants are changing to 8,000 qualified watch...

3. [New opportunities to earn and changes to the YouTube ...](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/) - This update won't impact creators already in YPP. New creators applying for YPP will need 8,000 qual...

4. [The YouTube Partner Programme overview and eligibility - Computer](https://support.google.com/youtube/answer/72851?hl=en-GB&co=GENIE.Platform=Desktop)

5. [Overview of the expanded YouTube Partner Program](https://support.google.com/youtube/answer/13429240?hl=en&co=GENIE.Platform=Android) - Get 1,000 subscribers with 4,000 qualified watch hours in the last 12 months, or; Get 1,000 subscrib...

6. [Choose how you want to monetize - Computer - YouTube Help](https://support.google.com/youtube/answer/94522?hl=en&co=GENIE.Platform=Desktop) - We’re expanding the YouTube Partner Program (YPP) to more creators with earlier access to fan fundin...

7. [YouTube Partner Program overview & eligibility - Google Help](https://support.google.com/youtube/answer/72851?hl)

8. [YouTube Partner Program overview & eligibility - Android](https://support.google.com/youtube/answer/72851?hl=en&co=GENIE.Platform=Android) - The YouTube Partner Program (YPP) gives creators greater access to YouTube resources and monetizatio...

9. [Disclosing use of GenAI content - Android - YouTube Help](https://support.google.com/youtube/answer/14328491?hl=en&co=GENIE.Platform=Android) - Examples of content, edits, or video assistance that creators need to disclose: AI generated music; ...

10. [Disclosing use of altered or synthetic content - Computer](https://support.google.com/youtube/answer/14328491?hl=en-GB&co=GENIE.Platform=Desktop) - We encourage creators' innovative and responsible use of content editing or generation tools. At the...

11. [Políticas de monetización de canales de YouTube](https://support.google.com/youtube/answer/1311392?hl=es-419)

12. [Monetization is disabled for my channel - YouTube Help](https://support.google.com/youtube/answer/1727191?hl=en) - We'll email you to let you know when the process is complete (it takes about a month). You can also ...

13. [Response to creator questions about YPP policies (July ...](https://support.google.com/youtube/thread/356734251/response-to-creator-questions-about-ypp-policies-july-2025?hl=en) - To be clear, we're not introducing a new YPP policy. This is a minor update to our long-standing “re...

14. [Response to creator questions about YPP policies (July ...](https://support.google.com/youtube/thread/356734251?hl=en&msgid=364957912)

15. [FAQ: Reused Content & YouTube's Partner Program](https://support.google.com/youtube/community-guide/271248162/%F0%9F%94%8E-faq-reused-content-youtube%E2%80%99s-partner-program?hl=en) - Channels using AI can still be eligible for monetization, provided they follow YouTube's monetizatio...

16. [Use automatic dubbing - Android - YouTube Help](https://support.google.com/youtube/answer/15569972?hl=en) - Supported languages for automatic dubbing ; English. Arabic, Bengali, Dutch, French*, German*, Hebre...

17. [Usar el doblaje automático - Ordenador - Ayuda de YouTube](https://support.google.com/youtube/answer/15569972?hl=es&co=GENIE.Platform=Desktop) - El doblaje automático genera pistas de audio traducidas en distintos idiomas. Así, tus vídeos serán ...

18. [Add Multi-language features to your videos - YouTube Help](https://support.google.com/youtube/answer/13338784?hl=en) - You must record your dubbed audio tracks before uploading them. If an automatic dub already exists f...

19. [Guidelines for using NASA Images and Media Guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/) - NASA content - images, audio, video, and media files are generally are not subject to copyright in t...

20. [NASA Brand Center](https://www.nasa.gov/nasa-brand-center/) - NASA has established specific guidelines for the use of its brand, merchandise, and media. These gui...

21. [Disclaimers, Copyright Notice, Terms and Conditions of Use](https://sti.nasa.gov/disclaimers/) - Disclaimers, Copyright Notice, and Terms and Conditions of Use DISCLAIMERS Disclaimer of Liability: ...

22. [Terms and conditions of use of images and videos available ...](https://photolibrary.esa.int/terms-and-conditions/) - ... images and videos for education, editorial and/or information purposes only. All other uses (e.g...

23. [ESA copyright notice](https://www.esa.int/About_Us/Law_at_ESA/Intellectual_Property_Rights/ESA_copyright_notice) - You may use ESA images or videos for educational or informational purposes. The publicly released ES...

24. [Commons:Licensing](https://commons.wikimedia.org/wiki/Commons:Licensing) - It aims to help uploaders decide whether an image or other media file is acceptable on Wikimedia Com...

25. [Commons:Reusing content outside Wikimedia/licenses](https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia/licenses) - attribution – You must give appropriate credit, provide a link to the license, and indicate if chang...

26. [Your content & YouTube Premium](https://support.google.com/youtube/answer/6306276?hl=en) - If you have access to downloadable reports, the revenue report will show watch time and earnings bro...

27. [Choose how you want to monetize - Android - YouTube Help](https://support.google.com/youtube/answer/94522?hl=en&co=GENIE.Platform=Android) - We’re expanding the YouTube Partner Program (YPP) to more creators with earlier access to fan fundin...

28. [YouTube partner earnings overview](https://support.google.com/youtube/answer/72902?hl=en) - Due to the ongoing war in Ukraine, we will be temporarily pausing Google and YouTube ads from servin...

29. [How YouTube recommendations work](https://support.google.com/youtube/answer/16089387?hl=en) - Satisfaction surveys: User surveys that ask you to rate videos that you watched helps the system und...

30. [YouTube performance FAQ and troubleshooting - Google Help](https://support.google.com/youtube/answer/141805?hl=en-GB) - YouTube's search and discovery system helps viewers to find the videos that they're most likely to w...

31. [Impressions & click-through-rate FAQs - YouTube Help](https://support.google.com/youtube/answer/7628154?hl=en) - YouTube will recommend a video to viewers if the video is relevant to them and if the video's averag...

32. [On YouTube's recommendation system](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/) - How YouTube's recommendation system works: Understand how videos are suggested and how to optimize y...

33. [YouTube Partner Program overview & eligibility - Computer](https://support.google.com/youtube/answer/72851?hl=en&co=GENIE.Platform=Desktop)

34. [My channel was rejected for monetization FAQs](https://support.google.com/youtube/answer/9235730?hl=en) - Yes. If it's your first rejection, you can re-apply to the YouTube Partner Program 30 days after you...

