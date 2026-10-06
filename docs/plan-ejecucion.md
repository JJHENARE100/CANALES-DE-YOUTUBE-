# Plan de ejecución: del 2 de octubre de 2026 a la monetización

Plan para los dos canales con más tirón según [`analisis-nichos.md`](analisis-nichos.md):
**historia para dormir** y **ciencia y espacio**, en español, narrados con tu voz,
entre 10 y 20 h a la semana. Cada canal se mide por separado.

**Revisado el 2 de octubre tras la [auditoría externa](auditoria-externa-2026-10-02.md)
([respuesta](respuesta-auditoria.md)):**
- Los dos canales arrancan como **pilotos** y el **20 de octubre** se elige el
  canal principal, que se lleva el 70–80% del tiempo.
- La solicitud del YPP se hace **entre el 30 de noviembre y el 10 de diciembre**.
  El 15 de enero es la fecha de aceptación, no la de solicitud.
- Escenario base: **monetizar un canal antes del cambio de febrero**. Los dos a
  la vez es el escenario optimista, no el que se planifica.

## Hitos y puertas de decisión (calendario de monetización)

El calendario editorial (qué se publica cada semana) está más abajo y en
[`canal-ciencia.md`](canal-ciencia.md). Esta tabla es el calendario de
monetización: qué se mide y qué se decide.

| Fecha | Hito | Qué se mide | Decisión |
|---|---|---|---|
| 11 oct | Cuentas listas y 2 episodios por canal terminados | Verificación en dos pasos, funciones avanzadas, AdSense, identidad visual | Retrasar como máximo una semana; nunca publicar sin colchón |
| 12–22 oct | **Pilotos**: 2 episodios largos por canal (historia: 12 y 19; ciencia: 15 y 22), 4–6 Shorts por episodio y 2 familias de título y miniatura por canal | Por vídeo: impresiones, CTR, duración media vista, horas por 1.000 impresiones, suscriptores por 1.000 visualizaciones, fuente de tráfico, espectadores que vuelven | — |
| **20 oct** | **Puerta 1: elegir canal principal** | Puntuación relativa: 35% horas por 1.000 impresiones; 25% suscriptores por 1.000 visualizaciones; 20% duración media y curva de retención; 10% CTR por fuente; 10% horas de tu tiempo por cada hora pública conseguida | El ganador recibe el 70–80% del tiempo: 2 episodios por semana y 6–10 Shorts. El otro pasa a 1 episodio quincenal, o semanal si mantiene su propia trayectoria. Si ninguno arranca, no se escala: se rehacen promesa, miniatura, apertura y temas |
| 2 nov | Control | Trayectoria del principal ≥ 50% de la lineal hacia 4.000 h y 1.000 suscriptores, proyectada con la velocidad de los últimos 7 y 14 días | Si no llega, concentrar aún más |
| 16 nov | Control | Trayectoria ≥ 75% | Empezar la auditoría del canal (§5): derechos, AdSense y vídeos marginales |
| **30 nov** | **Solicitar el YPP** si ya se cumple | 4.000 h públicas válidas y 1.000 suscriptores | Solicitar ese mismo día |
| **10 dic** | **Última fecha razonable para solicitar** | — | Solicitar si ya se cumple. No añadir contenido dudoso para llegar |
| ~1–15 ene | Respuesta (alrededor de un mes, a veces más) | Aceptado | Si llega un rechazo, **apelar el mismo día** (hay 21 días y la respuesta tarda unos 14). Volver a solicitar exige esperar 30 días, que ya caerían después del 1 de febrero |
| 15 ene | Objetivo de **aceptación** | — | Si sigue en revisión, seguir publicando contenido original |
| 31 ene | Aceptar los nuevos términos del YPP en Studio | — | Sin aceptarlos se deja de cobrar desde el 1 de febrero |

Si no se llega a tiempo, el canal sigue hacia el nivel de *fan funding*: 500
suscriptores, 3 vídeos públicos en 90 días y 3.000 h. Ese nivel da membresías y
Super Thanks, pero no anuncios, y sus requisitos no cambian en febrero. Para los
anuncios, a partir de febrero harán falta 8.000 h.

Para medir el ritmo en cada revisión hay una calculadora:
[`../herramientas/ritmo_ypp.py`](../herramientas/ritmo_ypp.py).

## 1. Semana 0 (2–11 de octubre): preparación

1. **Comprobar que hay hueco.** Buscar en YouTube «historia para dormir»,
   «documental para dormir», «historia aburrida para dormir» y «mitología para
   dormir». Anotar los 10 primeros canales: suscriptores, fecha del primer vídeo,
   duración y visitas de los últimos vídeos.
   - Si hay más de 3 canales en español con más de 100.000 suscriptores
     publicando cada semana, el hueco es menor de lo estimado. En ese caso,
     diferenciar el ángulo (por ejemplo, historia de Hispanoamérica y la península)
     o pasar a ciencia y espacio.
2. **Cuenta.**
   - Cuenta de Google dedicada y canal de marca.
   - Verificación en dos pasos y verificación por teléfono (funciones avanzadas).
   - AdSense para YouTube abierto con el formulario W-8BEN (tratado
     España–EE. UU.).
3. **Nombre.** Ideas para comprobar que están libres en YouTube y en redes:
   «Noches de Historia», «La Historia Lenta», «Crónicas para Dormir».
4. **Identidad.** Logotipo, banner, plantilla de miniatura con margen para
   variarla, y una sección «Acerca de» que explique el método:
   > Guiones investigados a partir de fuentes citadas en cada vídeo. Narración con
   > mi voz, generada con IA. Revisión humana de cada episodio.
5. **Herramientas.**
   - **Clonar tu voz.**
     - Usar el clon profesional de ElevenLabs (planes Creator o Pro). El clon
       instantáneo pierde naturalidad en narraciones de 2 h.
     - Grabar 1–3 h de lectura limpia en el mismo tono que tendrán los episodios:
       pausado y grave, en una habitación sin eco, con un micrófono decente y
       siempre a la misma distancia.
     - ElevenLabs pide verificar que la voz es tuya.
     - Probar el clon con 5 minutos del primer guion antes de producir.
   - Fijar el estilo de imagen: un prompt base y una paleta.
   - Montar el proyecto plantilla en DaVinci Resolve.
6. **Producir los episodios 1 y 2**, y sacar 6 Shorts de ellos.

## 2. Ritmo semanal (a partir del 12 de octubre)

**Cada semana se publica:**

- **1 episodio de 90–119 minutos** (a partir de 120 no hay doblaje automático). Va como *estreno*, siempre el mismo día y a
  la misma hora, a primera hora de la noche en España, que es tarde en
  Latinoamérica.
- **3–5 Shorts de 30–60 s** sacados del episodio, cada uno con el enlace
  «vídeo relacionado» al episodio completo.
- **1 publicación de comunidad:** encuesta sobre el próximo tema.

**Horas por episodio** (unas 15 h; con 10 h/semana se sale a un episodio cada
10 días):

| Paso | Horas | Quién o qué |
|---|---|---|
| Elegir tema y reunir 3–5 fuentes | 1,5 | Persona + Claude |
| Guion de 12.000–17.000 palabras, por capítulos | 3 | Claude por capítulos, con las fuentes delante |
| **Revisión humana de hechos**, ritmo y variación respecto a episodios anteriores | 2,5 | Persona |
| Voz | 1 | Tu clon en ElevenLabs, por capítulos; volver a generar las frases con mala entonación |
| Imágenes (150–250) | 3 | Láminas de dominio público, mapas, ilustraciones IA con el estilo fijado |
| Montaje: movimiento lento, capítulos, música suave con licencia | 2 | DaVinci Resolve |
| Miniatura, título, descripción con fuentes, capítulos | 1 | Persona |
| 3–5 Shorts | 1 | DaVinci o CapCut |

**Reglas que no se saltan:**

1. No se publica ningún guion sin la revisión humana.
2. Ningún episodio reutiliza la estructura del anterior palabra por palabra.
3. Las fuentes van en la descripción.
4. Si la narración sale de tu clon, la descripción indica que está generada con IA.
5. Una escena realista inventada lleva la etiqueta de contenido sintético.
6. No se borra ni se pone en privado ningún vídeo con horas acumuladas.

### Bucle semanal de aprendizaje (cada lunes)

Exportar YouTube Studio y pasar `herramientas/analitica/motor.py` en tres modos:
- `diagnostico`: qué arreglar en cada vídeo;
- `siguiente`: qué temas van después;
- `puerta`: solo el 20 de octubre.

Detalle en [`recomendador.md`](recomendador.md).

### Primeros episodios propuestos

Revisados el 2 de octubre con datos de demanda y competencia en YouTube
([`validacion-temas.md`](validacion-temas.md)). El ángulo hispano es el hueco más
claro del nicho. Estrenos los lunes:

1. 12 oct · **El emperador que vino de Hispania: un día en la Roma de Trajano** ([guion](../guiones/ep01-un-dia-en-la-roma-de-trajano.md))
2. 19 oct · **Córdoba en tiempos de Almanzor: un día del año 1000** ([guion](../guiones/ep02-cordoba-en-el-ano-1000.md))
3. 26 oct · La vida a bordo de un galeón español (demanda alta, sin versiones para dormir)
4. 2 nov · ¿Cómo era un día completo en la Castilla medieval? (sustituye a la mitología nórdica)
5. 9 nov · Lo que vieron los españoles: Tenochtitlan en 1519, según Bernal Díaz
6. 16 nov · Egipto contado por los obreros de las pirámides de Guiza
7. 23 nov · Los caminos del Imperio inca: chasquis y Qhapaq Ñan
8. 30 nov · Los vikingos en la Península: Sevilla, año 844
9. 7 dic · Los mitos griegos de Hispania: Gerión, las Hespérides y Gadir (sustituye a «del Caos al Olimpo», que ya existe)
10. 14 dic · Corsarios y piratas en las noches del Atlántico (sustituye a Constantinopla)

## 3. Crecimiento sin trampas

- **Shorts para los suscriptores.**
  - Cada Short termina con una frase que invita al episodio completo.
  - Se fija un comentario con el enlace.
  - Hacen falta del orden de 0,5–2 M de vistas acumuladas en Shorts para cubrir
    los suscriptores que el vídeo largo no da.
- **Sesiones largas.**
  - Listas de reproducción por época («Roma», «Mitología»), pantalla final al
    siguiente episodio y capítulos en cada vídeo.
  - Los directos públicos de menos de 12 h cuentan para las horas. Los en bucle
    24/7 son arriesgados ante la revisión.
- **Doblaje automático.** Activar el doblaje automático al inglés y al portugués
  si Studio lo ofrece al canal. Si no, añadir pistas de audio propias cuando esté
  disponible. El tiempo que se ve doblado suma al mismo canal.
- **Colaboraciones.** Con la función *Collabs*, con canales pequeños de historia
  en español (de igual a igual, sin intercambio de suscripciones).
- **Prohibido:** sub4sub, comprar visitas, suscriptores u horas, y los bots.
  Llevan al cierre del canal. Las visitas de Google Ads no cuentan para las
  horas.

## 4. Presupuesto mensual (USD, aproximado)

| Partida | Normal | Ajustado |
|---|---|---|
| Claude Pro (guion) | 20 | 20 |
| Voz: unos 380.000 caracteres al mes con 4 episodios (con clon de tu voz) | ElevenLabs Pro, 99 | Fish Audio Plus, ~15 |
| Imágenes: ~800 al mes | Midjourney Standard, 30 | Midjourney Basic + dominio público, 10 |
| Montaje | DaVinci Resolve, 0 | 0 |
| Investigación de títulos | vidIQ Boost, 17 | 0 |
| **Total** | **~166** | **~45** |

Precios de octubre de 2026, que pueden cambiar:
[ElevenLabs](https://www.cloudzero.com/blog/elevenlabs-pricing/),
[Fish Audio](https://smallest.ai/blog/fish-audio-pricing-plans-api-billing-commercial-use-in-2026),
[Midjourney](https://costbench.com/software/ai-image-generators/midjourney/),
[vidIQ](https://1of10.com/blog/vidiq-pricing/). Antes de pagar hay que comprobar
la licencia comercial de cada herramienta: el plan gratuito de ElevenLabs no la
incluye.

## 5. Auditoría del canal antes de solicitar (desde el 16 de noviembre)

- [ ] 1.000 suscriptores y 4.000 h públicas en los últimos 365 días (Studio → Ingresos)
- [ ] Verificación en dos pasos activa, funciones avanzadas activas y ningún aviso de Normas de la Comunidad
- [ ] AdSense para YouTube vinculado y W-8BEN enviado
- [ ] Revisar como lo haría un revisor: los 5 vídeos más vistos, los 5 más recientes y los que más tiempo de visualización aportan
  - [ ] Cada uno tiene guion propio y fuentes en la descripción. La voz es humana o, si es tu clon, está declarada
  - [ ] Cada vídeo tiene su manifiesto de imágenes (`creditos.txt`), con fuente y licencia de cada imagen real
  - [ ] Ningún contenido reutilizado sin comentario o transformación propia
  - [ ] Ninguno es intercambiable con otro
  - [ ] Ninguno lleva escenas realistas inventadas sin etiquetar
- [ ] «Acerca de» con el método
- [ ] Títulos y miniaturas sin promesas falsas
- [ ] Ningún vídeo con horas puesto en privado o borrado para manipular métricas. Sí se retira o corrige lo que tenga riesgo de política, de copyright o de autenticidad, aunque sus horas dejen de contar
- [ ] Anotar la fecha de solicitud en el calendario para poder apelar en 21 días si llega un rechazo

## 6. Modelo de negocio

El proyecto se plantea como una **cartera de propiedad intelectual editorial**
(guiones, voz, catálogo), no como arbitraje de anuncios con vídeos automáticos.

- **Anuncios:** a partir de 8 minutos se pueden poner anuncios a mitad del vídeo.
  YouTube da al creador el 55% de los ingresos netos de los anuncios de la página
  del vídeo.
- **YouTube Premium:** se reparte según el tiempo que los miembros pasan viendo
  tu contenido, incluida la reproducción en segundo plano, que es frecuente en
  vídeos para dormir.
- **Las cuentas de cada canal** se hacen con datos reales, no con estimaciones:
  - Ingresos al mes = visualizaciones monetizadas / 1.000 × RPM real del canal.
  - Margen = ingresos − (guion + voz + imágenes + software + horas de revisión).
  - Recuperación = inversión acumulada / margen mensual.
- **Segunda fuente de ingresos**, solo cuando haya audiencia demostrada y nunca
  dentro de las previsiones anteriores al YPP:
  - Ciencia: afiliación de astronomía (telescopios, libros) y patrocinios.
  - Historia: membresías y un catálogo de audio.

## 7. Lo que queda fuera de este plan

- **Canal de ciencia y espacio:** formato, calendario e imágenes en [`canal-ciencia.md`](canal-ciencia.md).
- **IRPF, IVA y alta de autónomo en España** por los ingresos de YouTube: hay que
  consultarlo con un asesor fiscal antes del primer pago.
- **Confirmar con un jurista si el artículo 50 del Reglamento europeo de IA se
  aplica a tu voz clonada.** Mientras tanto, la declaramos siempre.
