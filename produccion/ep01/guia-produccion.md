# Guía de producción — Episodio 1 — Un día cualquiera en la Roma de Trajano

133 planos · 45 clips de vídeo (27 de prioridad A) · unos 90 min de narración.

Hay tres trabajos que se pueden hacer a la vez: **grabar**, **generar imágenes** y **generar clips**.
Todo se coordina por el código de plano (`01-08`): la imagen es `01-08.jpg` y el clip `01-08.mp4`, y los dos
van en `imagenes/`. El montaje coloca cada plano mientras se narra su texto.

## 1. Grabación

Lee de [`lectura.md`](lectura.md) y sigue [`docs/grabacion.md`](../../docs/grabacion.md): claqueta, palmada si
te equivocas, un archivo por capítulo. Sesiones propuestas (descansa la voz entre una y otra):

- **Sesión 1** (~25 min de lectura, ~41 min con repeticiones): `cap00` Bienvenida, `cap01` Antes del amanecer, `cap02` La insula se despierta, `cap03` El primer bocado y los dioses de la casa, `cap04` La salutación
- **Sesión 2** (~29 min de lectura, ~46 min con repeticiones): `cap05` Las calles por la mañana, `cap06` El agua de Roma, `cap07` El río y el puerto, `cap08` El foro nuevo de Trajano
- **Sesión 3** (~35 min de lectura, ~57 min con repeticiones): `cap09` La hora sexta, `cap10` Las mujeres de Roma, `cap11` El Circo Máximo en silencio, `cap12` Las termas, `cap13` La cena, `cap14` La noche vuelve a Roma

**Antes de grabar todo:** graba `cap00` y `cap01` y pásalos por `audio.py` (o súbelos al chat para que
los revise). Así se ajustan la palmada, las pausas y el volumen a tu voz y a tu habitación antes de invertir horas.

## 2. Biblia visual (para que todo parezca del mismo canal)

**Estilo, al final de cada descripción de imagen:**

```
, painterly digital illustration, soft warm light, muted ochre and dusk-blue palette, gentle atmosphere, historical accuracy, no text, no watermark, 16:9
```

- **Midjourney:** añade `--ar 16:9`. Cuando tengas 3–4 imágenes que te gusten, usa una como referencia de estilo
  (`--sref <url>`) en todas las demás.
- **ChatGPT, Gemini o Ideogram:** pide formato horizontal 16:9 y adjunta una imagen aprobada como referencia de estilo.
- **Personajes que se repiten** (usa siempre la misma descripción y, si la herramienta lo permite, una imagen de referencia del personaje):
  - la mujer de la insula: *a woman in a simple undyed wool tunic and brown shawl* (casi siempre de espaldas o de lejos);
  - su marido: *a husband in a plain brown tunic*; la abuela: *a grandmother in a dark grey mantle*;
  - el senador: *a grey-haired senator in a white toga*; su mujer: *a matron in a long pale blue stola*;
  - la viuda de la tienda: *a middle-aged widow in a dark stola*.
- **Caras:** de lejos, de espaldas o de perfil suave. Los primeros planos de caras delatan la IA y se deforman en los clips.
- **Lugares reales de hoy** (Fontana de Trevi `06-04`, puerto de Trajano `07-04`, Monte Testaccio `08-08`, obelisco
  `11-03`): mejor una **foto real** con licencia libre (Wikimedia Commons, anotando fuente, licencia y atribución en
  `planos.csv`). Si se hace con IA, que se note pictórica, nunca una falsa fotografía.
- **Resolución:** 1920×1080 o mayor. Guarda en `imagenes/` con el nombre exacto del plano.

## 3. Clips de vídeo (máximo 10 s)

- **Cómo se generan:** en tu herramienta de vídeo (Kling, Runway, Veo, Hailuo o Luma), en modo *imagen a vídeo*, a partir
  de la imagen del plano. Así el clip encaja con ella.
- **Prioridad:** **A** primero (la mayoría son agua, luz, río o carros, que se generan bien); **B** si sobran créditos.
- **Cómo se montan:** el plano empieza con el clip y funde a la imagen con movimiento. Para más calma, monta con
  `--clip-lentitud 1.25`. Si un clip sale raro, no lo uses: el plano funciona igual solo con la imagen.
- **Texto común, al final de cada descripción de clip:**

```
Image-to-video from the attached image, 5–10 seconds. Slow, calm, steady camera; only natural, subtle motion; keep the exact composition, characters and painterly style of the image; no new people or objects, no text, no camera shake, no fast movement, no morphing faces.
```

## 4. Plano a plano

### `cap00` · Bienvenida (~2 min)

**00-01** · entra con «Hola. Ponte cómodo. Si estás en la cama, deja…» → `00-01.jpg`
- Imagen: A vast night view over ancient Rome from a hilltop, dark tiled rooftops of insulae and temples under a starry sky, a few warm oil-lamp glows in distant windows, mist drifting along the Tiber.
- 🎬 Clip **A** `00-01.mp4`: Very slow forward aerial drift over the dark rooftops; tiny oil-lamp lights flicker gently in distant windows; thin mist drifts along the river; stars twinkle faintly.

**00-02** · entra con «Las tienes todas en la descripción. Vamos a pasar…» → `00-02.jpg`
- Imagen: A marble bust of Emperor Trajan with short hair combed forward, resting on a stone pedestal in a quiet atrium, a small laurel wreath at its base, soft morning light falling across the marble.

**00-03** · entra con «Las fronteras quedan muy lejos. Aquí, en el corazón…» → `00-03.jpg`
- Imagen: A narrow paved Roman street just before dawn, tall brick insulae on both sides with closed wooden shutters, a stone public fountain softly flowing at the corner, deep blue sky above the rooftops.

### `cap01` · Antes del amanecer (~6 min)

**01-01** · entra con «Todavía es de noche, pero Roma no está en…» → `01-01.jpg`
- Imagen: Close view of a heavy wooden cart wheel with an iron rim rolling over dark basalt paving stones at night, the legs and harness of a mule beside it, lit faintly by a hanging oil lantern.
- 🎬 Clip **A** `01-01.mp4`: Low static camera at wheel height; the iron-rimmed wheel rolls slowly past, turning steadily over the paving stones; the hanging lantern sways softly; the mule's legs step calmly.

**01-02** · entra con «Es una norma antigua, de los tiempos de Julio…» → `01-02.jpg`
- Imagen: A line of mule-drawn carts entering Rome through an arched stone city gate at night, loaded with wine amphorae, stacked timber and baskets of vegetables, carters walking alongside with small lanterns.
- 🎬 Clip **B** `01-02.mp4`: Slow push-in toward the arched gate; the carts move forward at a walking pace; mules nod their heads; torchlight flickers on the stone.

**01-03** · entra con «Un poeta de esta misma época, Juvenal, se quejaba…» → `01-03.jpg`
- Imagen: A sleepy Roman man lying in a simple wooden bed in a cramped upper room, gazing toward a small shuttered window, a faint lantern glow from passing carts flickering on the ceiling, quiet night.

**01-04** · entra con «Puedes escuchar las ruedas como quien escucha la lluvia:…» → `01-04.jpg`
- Imagen: Looking up a narrow Roman street between tall insulae of brick and timber, five and six stories high, wooden balconies and small shuttered windows, pre-dawn blue light, a distant cart lantern at the far end.

**01-05** · entra con «En la planta baja, las puertas de las tiendas…» → `01-05.jpg`
- Imagen: Ground-floor Roman shop front closed for the night with vertical wooden planks slotted into a stone threshold groove, small windows above with wooden shutters and a cloth curtain, violet dawn sky glowing.

**01-06** · entra con «Al fondo de la calle se ve el resplandor…» → `01-06.jpg`
- Imagen: A small group of Roman vigiles in plain tunics walking calmly down a dark narrow street, one holding a burning torch, all looking up at the windows of the insulae, unhurried and seen at a distance.
- 🎬 Clip **B** `01-06.mp4`: Static camera; the group walks slowly away down the street; the torch flame flickers and throws moving light on the walls; no faces in close-up.

**01-07** · entra con «Su trabajo principal es el fuego. En una ciudad…» → `01-07.jpg`
- Imagen: Equipment of the Roman vigiles leaning against a brick wall: esparto buckets sealed with pitch, an axe, a wooden ladder, folded blankets and a clay jar of vinegar, lit by warm torchlight.

**01-08** · entra con «Esta noche no hay humo. Los vigilantes pasan a…» → `01-08.jpg`
- Imagen: A rectangular stone public fountain at a Roman street corner at night, water pouring steadily from a bronze spout into the basin and overflowing onto the paving, a torch glow fading far down the street.
- 🎬 Clip **A** `01-08.mp4`: Static close shot; water pours steadily from the bronze spout, the basin surface ripples and overflows in a thin sheet onto the paving; moonlight glints on the water.

**01-09** · entra con «El agua llega desde las montañas, a muchos kilómetros,…» → `01-09.jpg`
- Imagen: Aerial view of the Roman countryside at dawn, a long aqueduct of stone arches crossing green fields toward the distant city of Rome, gentle hills and a small lake on the northwestern horizon.
- 🎬 Clip **A** `01-09.mp4`: Slow aerial glide along the line of aqueduct arches toward the city; morning mist drifts over the fields; soft dawn light grows slightly brighter.

**01-10** · entra con «Es un sonido bonito para quedarse dormido. Ruedas que…» → `01-10.jpg`
- Imagen: Tiled rooftops of Roman insulae at first light, a rooster perched on a courtyard wall below, one wooden shutter swinging open in an upper window, pale blue sky slowly brightening.
- 🎬 Clip **B** `01-10.mp4`: Static view; a wooden shutter slowly swings open; the rooster lifts its head; the pale sky brightens almost imperceptibly.

### `cap02` · La insula se despierta (~7 min)

**02-01** · entra con «Entremos en uno de esos edificios. Subamos despacio por…» → `02-01.jpg`
- Imagen: Inside a Roman insula, a narrow steep staircase climbing upward, stone steps below and worn wooden steps higher up, soot-stained plaster walls, a small clay oil lamp in a wall niche, dim morning light.
- 🎬 Clip **A** `02-01.mp4`: Slow steady camera climb up the narrow staircase; the small oil-lamp flame flickers; dust motes float in a thin beam of light.

**02-02** · entra con «En el primer piso, el más cómodo, a veces…» → `02-02.jpg`
- Imagen: Cutaway view of a Roman insula showing its floors: shops at street level, a spacious first-floor apartment with painted walls, smaller rooms above, and a cramped attic room with a bed, chest and brazier.

**02-03** · entra con «Y desde donde, si hay un incendio, es más…» → `02-03.jpg`
- Imagen: A Roman street lined with insulae of slightly different heights in soft morning light, a bronze plaque with an engraved building regulation fixed to a brick wall in the foreground, wooden scaffolding on one facade.

**02-04** · entra con «Juvenal, el poeta de los carros, decía que en…» → `02-04.jpg`
- Imagen: Close detail of a cracked plaster wall inside an insula held by a wooden prop beam, morning sunlight slipping through the gaps of closed wooden shutters and drawing thin lines across the floor.

**02-05** · entra con «En una de las habitaciones del tercer piso, una…» → `02-05.jpg`
- Imagen: In a small third-floor insula room at dawn, a woman in a simple undyed wool tunic and brown shawl picks up a clay water jug by the window, her family still asleep on wooden beds behind her in the soft grey light.

**02-06** · entra con «En la fuente ya hay otras personas. Una niña…» → `02-06.jpg`
- Imagen: Neighbors gathered around a stone corner fountain in early morning: a little girl with a small bucket, a young slave filling two amphorae, an old man slowly washing his face with his hands.

**02-07** · entra con «Es una conversación sin importancia. Como la de cualquier…» → `02-07.jpg`
- Imagen: Seen from behind, a woman in a simple undyed wool tunic and brown shawl climbs an outdoor stair carrying a full clay jug on her shoulder, the sun rising golden behind distant Roman hills and rooftops.
- 🎬 Clip **B** `02-07.mp4`: Camera static behind the woman as she climbs a few steps slowly with the jug on her shoulder; the shawl moves slightly; warm sunrise light; her face is never shown.

**02-08** · entra con «Esto tiene una consecuencia curiosa: como en verano el…» → `02-08.jpg`
- Imagen: A stone sundial on a pedestal in a quiet Roman square, its bronze gnomon casting a long shadow across twelve carved hour lines, soft October morning light and an empty street beyond.
- 🎬 Clip **A** `02-08.mp4`: Locked-off shot; the gnomon's shadow moves slowly across the carved hour lines like a gentle time-lapse; light shifts softly; leaves stir in the corner.

**02-09** · entra con «La hora duodécima es la última, la que termina…» → `02-09.jpg`
- Imagen: Close view of a Roman water clock in a wealthy home: a bronze vessel dripping water into a lower basin with an engraved hour scale and a small float, set on a marble table.
- 🎬 Clip **B** `02-09.mp4`: Close static shot; a drop of water falls from the bronze vessel into the lower basin every second, making small ripples; the float rises imperceptibly.

**02-10** · entra con «Así que la mayoría de la gente no vive…» → `02-10.jpg`
- Imagen: A calm Roman street in morning light with people walking slowly, the entrance of a bath house in the distance with a small bronze bell hanging beside its door, sunlight slanting across the paving.

### `cap03` · El primer bocado y los dioses de la casa (~5 min)

**03-01** · entra con «En la habitación del tercer piso se despiertan los…» → `03-01.jpg`
- Imagen: The third-floor insula room in the morning: a husband in a plain brown tunic, two small children and a grandmother in a dark grey mantle waking on wooden beds and straw mattresses, a woman in a simple undyed wool tunic and brown shawl nearby.

**03-02** · entra con «Se come de pie o sentado en el borde…» → `03-02.jpg`
- Imagen: Close-up of a simple Roman breakfast on a wooden board: a round loaf of bread, a small cup of wine, a piece of cheese, black olives, an onion and dried figs, soft window light.
- 🎬 Clip **B** `03-02.mp4`: Very slow push-in across the breakfast board; dust motes drift in a sunbeam; a faint wisp of steam rises from the cup.

**03-03** · entra con «Como mucho, se calienta algo en un pequeño brasero…» → `03-03.jpg`
- Imagen: A small wooden lararium shelf in the corner of a humble room, two little bronze lar figurines dancing and holding drinking horns, a few clay figures beside them and a tiny oil lamp.

**03-04** · entra con «Junto a ellos, los penates, que cuidan la despensa…» → `03-04.jpg`
- Imagen: Close view of a man's hands in a plain brown tunic sleeve placing a crumb of bread and a pinch of salt before small bronze household gods on a wooden shelf, a cup of wine beside them.

**03-05** · entra con «Es un gesto pequeño, como quien da los buenos…» → `03-05.jpg`
- Imagen: View from a modest insula window across Roman rooftops toward a nearby hill, where a large walled house with a tiled roof and tall cypress trees catches the morning light.

**03-06** · entra con «Es una domus, la vivienda de una familia rica.…» → `03-06.jpg`
- Imagen: Street view of the senator's domus on a hillside: plain plastered walls with almost no windows, a narrow doorway with a thick wooden door, small rented shops on either side, morning light.

**03-07** · entra con «El agua refleja el cielo. Las paredes están pintadas…» → `03-07.jpg`
- Imagen: Inside the senator's domus, an impluvium pool reflecting the sky, walls painted deep red, ochre and black with imaginary landscapes and painted columns, a colonnaded garden with a fountain beyond.
- 🎬 Clip **A** `03-07.mp4`: Slow tilt down from the roof opening to the impluvium pool; the water surface ripples gently, reflecting moving clouds; light plays on the painted walls.

**03-08** · entra con «Barren los suelos de mosaico, abren las puertas, encienden…» → `03-08.jpg`
- Imagen: Household slaves in plain tunics quietly sweeping a black-and-white mosaic floor, lighting bronze oil lamps and shaking cushions in the senator's domus at dawn, soft light from the atrium opening.

### `cap04` · La salutación (~5 min)

**04-01** · entra con «Afuera, frente a la puerta de la domus, ya…» → `04-01.jpg`
- Imagen: Roman clients in heavy white wool togas waiting outside the closed wooden door of the senator's domus at first light, folds draped over their left arms, one quietly yawning, a calm street.
- 🎬 Clip **B** `04-01.mp4`: Slow lateral dolly along the waiting clients seen from a distance; toga folds stir slightly in a light breeze; morning light warms the wall.

**04-02** · entra con «Estos hombres son clientes. En Roma, casi todo el…» → `04-02.jpg`
- Imagen: Close detail of a Roman man arranging the heavy folds of a white wool toga over his left arm, the texture of the thick wool and a simple iron ring on his finger visible.

**04-03** · entra con «Los romanos la llaman la salutatio, la salutación. Cuando…» → `04-03.jpg`
- Imagen: A doorkeeper slave at the open door of the domus letting clients into the atrium one by one, the senator, a grey-haired man in a white toga, standing calmly at the far end beside the impluvium.

**04-04** · entra con «Saluda a unos por su nombre, a otros con…» → `04-04.jpg`
- Imagen: In the atrium, the grey-haired senator in a white toga listens to a client's request while a slave whispers names at his shoulder, and another slave hands small coins to humble clients in worn togas.

**04-05** · entra con «Se llama sportula, la espórtula, que en su origen…» → `04-05.jpg`
- Imagen: Close-up of a small woven basket holding a pile of tiny bronze quadrans coins and a loaf of bread, held out by a slave's hand in the dim atrium of a Roman domus.

**04-06** · entra con «Contaba cómo tenía que subir y bajar las colinas…» → `04-06.jpg`
- Imagen: A lone Roman client in a mud-splashed white toga walking up a steep paved street on one of Rome's hills in the morning, small and seen from behind, houses climbing the slope ahead.

**04-07** · entra con «Terminada la salutación, el senador sale a la calle.…» → `04-07.jpg`
- Imagen: Wide view of a small procession descending a hillside street toward the Forum: a slave clearing the way in front, the grey-haired senator in a white toga, and a line of clients in white togas following.
- 🎬 Clip **B** `04-07.mp4`: Wide static shot; the small procession descends the street slowly and moves away from camera; banners and togas sway slightly; figures stay small.

**04-08** · entra con «Nosotros nos quedamos atrás un momento, en la puerta.…» → `04-08.jpg`
- Imagen: The doorway of the senator's domus seen from the threshold as the procession disappears down the street, and a narrower side street sloping down toward a busy quarter of workshops and awnings.

### `cap05` · Las calles por la mañana (~7 min)

**05-01** · entra con «A esta hora, la segunda o tercera de la…» → `05-01.jpg`
- Imagen: A busy Roman street of open tabernae in mid-morning, wooden shutter planks stacked beside each doorway, masonry counters with goods hanging from ceilings, a cobbler on a low stool stitching a sandal.
- 🎬 Clip **A** `05-01.mp4`: Wide shot with a very slow push-in; small figures walk calmly along the street; awnings ripple in the breeze; hanging goods sway; no close-up faces.

**05-02** · entra con «Más allá, un herrero golpea un hierro al rojo,…» → `05-02.jpg`
- Imagen: A Roman barber shaving a seated customer outdoors with a gleaming razor, others waiting on a bench and chatting, behind them a stall of dyed wool cloth and a board lined with rows of clay lamps.

**05-03** · entra con «Las tiendas invaden la acera. Los dueños ponen fuera…» → `05-03.jpg`
- Imagen: High-angle view of a crowded narrow Roman street where shop tables, baskets and awnings spill onto the pavement, people walking down the middle among small puddles and a laden pack mule.

**05-04** · entra con «Huele a pan. En muchas esquinas hay panaderías con…» → `05-04.jpg`
- Imagen: Interior of a Roman bakery: a large domed brick oven, a stone hourglass-shaped mill turned by a blindfolded donkey, and round loaves scored into eight wedges stacked on the counter.
- 🎬 Clip **A** `05-04.mp4`: Static shot; the blindfolded donkey walks slowly in a circle turning the stone mill; the oven mouth glows and flickers orange; a little flour dust floats.

**05-05** · entra con «Y a veces, cuando el viento cambia, a cosas…» → `05-05.jpg`
- Imagen: A small open-air Roman school under a portico, a curtain hung to separate it from the street, a teacher seated on a chair and a group of children on stools reciting together.

**05-06** · entra con «Los niños se sientan en taburetes, con una tablilla…» → `05-06.jpg`
- Imagen: Close-up of a child's hands holding a wooden wax tablet on the knees, writing Latin letters with a bronze stylus whose flat end is ready to smooth the wax, warm morning light.
- 🎬 Clip **B** `05-06.mp4`: Close static shot of the hands; the stylus slowly traces a letter in the wax, then the hand turns it and smooths the wax with the flat end.

**05-07** · entra con «Le pregunta, medio en broma, cuánto quiere cobrar por…» → `05-07.jpg`
- Imagen: A dog sleeping in the sun beside a cobbler's counter in a Roman street, while in the background a distracted schoolboy on a stool looks toward it and the teacher raises a gentle hand.

**05-08** · entra con «En un lado hay un local con un mostrador…» → `05-08.jpg`
- Imagen: A Roman thermopolium with a marble counter set with large embedded clay jars, a woman ladling hot stew into a bowl, bread and cheese on a shelf, customers standing and eating at the counter.

**05-09** · entra con «Pero para la mayoría de los romanos, que no…» → `05-09.jpg`
- Imagen: A Roman street scene: a free man in a simple tunic carrying a sack on his shoulder, a woman with a basket of vegetables holding a child's hand, and two slaves carrying a curtained litter.

**05-10** · entra con «Un soldado de permiso, con su cinturón militar bien…» → `05-10.jpg`
- Imagen: A varied crowd in a sunny Roman street: a soldier on leave with a studded military belt, a Greek merchant bargaining, a North African man, a Syrian trader and a Gaul in trousers walking past.

### `cap06` · El agua de Roma (~8 min)

**06-01** · entra con «Dejamos atrás el ruido de las tiendas y seguimos…» → `06-01.jpg`
- Imagen: A long Roman aqueduct of stacked stone arches stretching across the sky above the tiled rooftops of Rome, seen from the top of a gently rising street, soft morning haze.
- 🎬 Clip **A** `06-01.mp4`: Slow tilt up from the rooftops to the aqueduct arches; clouds drift slowly across the sky behind the arches; birds cross in the distance.

**06-02** · entra con «No se ve el agua, pero está ahí. Viene…» → `06-02.jpg`
- Imagen: Map-like aerial view of the hills around Rome, thin aqueduct lines running from mountain springs and rivers toward the city, mostly underground, then emerging onto arches across the plain.

**06-03** · entra con «Los acueductos van casi siempre bajo tierra, siguiendo las…» → `06-03.jpg`
- Imagen: A traveler on a road east of Rome watching long aqueduct arches appear on the horizon across a flat green plain, the city still far away, cypress trees along the road, gentle morning light.

**06-04** · entra con «En este año ciento doce, Roma recibe agua de…» → `06-04.jpg`
- Imagen: The Trevi Fountain in Rome today at dusk, calm and nearly empty, soft lights glowing on the marble statues and the turquoise water still fed by the ancient Aqua Virgo.
- 🎬 Clip **A** `06-04.mp4`: Slow push-in toward the fountain at dusk; the water flows and cascades continuously over the rocks; the lights shimmer on the turquoise pool.

**06-05** · entra con «Sabemos mucho sobre estos acueductos gracias a un hombre…» → `06-05.jpg`
- Imagen: A small distant figure of a Roman water commissioner in a toga walking along an aqueduct channel with two assistants measuring the flow, a wide landscape of arches and hills in morning light.

**06-06** · entra con «En una de sus páginas, Frontino se deja llevar…» → `06-06.jpg`
- Imagen: A papyrus scroll unrolled on a wooden table beside an oil lamp, showing a simple ink drawing of aqueduct arches next to a small sketch of pyramids, a reed pen and an inkpot nearby.

**06-07** · entra con «Allí se calma, deja caer las impurezas al fondo…» → `06-07.jpg`
- Imagen: Inside a Roman water distribution tank, clear water settling in a stone basin and flowing out through several lead pipes of different sizes, soft light from a high opening, calm reflections.
- 🎬 Clip **B** `06-07.mp4`: Static shot; clear water settles and flows out smoothly through the lead pipes; soft light reflections ripple on the stone walls.

**06-08** · entra con «El segundo, los edificios públicos: las termas, los estanques…» → `06-08.jpg`
- Imagen: Close detail of lead water pipes stamped with raised Latin letters of the owner's name, running along the base of a wall into a wealthy house, a bronze stopcock fitted to one of them.

**06-09** · entra con «Mientras pensamos en todo esto, llegamos a otra fuente…» → `06-09.jpg`
- Imagen: Close view of a bronze lion-head spout pouring a steady stream into a stone basin in a small Roman square, a water carrier filling amphorae beside it to sell on the upper floors.

**06-10** · entra con «Un niño mete las manos en el agua y…» → `06-10.jpg`
- Imagen: Two women in tunics chatting beside a public fountain with clay jugs resting on their hips, a child splashing water on his face and a dog drinking from the basin edge, late morning light.

**06-11** · entra con «Es una forma de entender la ciudad. Una ciudad…» → `06-11.jpg`
- Imagen: Workers in tunics maintaining an aqueduct channel inside a stone tunnel by lamplight, calmly laying stones and checking the gentle slope with a long wooden level, water flowing quietly beside them.

**06-12** · entra con «Funcionarios que vigilan las tomas. Y, todo el tiempo,…» → `06-12.jpg`
- Imagen: A gently sloping Roman aqueduct channel seen from above, clear water flowing smoothly along it toward the distant city, green hills behind, quiet late-morning light.
- 🎬 Clip **A** `06-12.mp4`: Slow aerial follow along the channel; the water flows smoothly and steadily toward the distant city; late-afternoon light on the hills.

### `cap07` · El río y el puerto (~6 min)

**07-01** · entra con «El Tíber pasa por Roma dibujando una gran curva.…» → `07-01.jpg`
- Imagen: Aerial view of the Tiber's great yellowish curve through ancient Rome, the Aventine Hill rising beside long stone wharves and warehouses of the Emporium river port, morning light.

**07-02** · entra con «Es una larga orilla de piedra, con escalones que…» → `07-02.jpg`
- Imagen: A stone quay on the Tiber with steps down to the water and iron mooring rings, flat-bottomed barges loaded with sacks and amphorae towed upstream by pairs of oxen and men along a towpath.
- 🎬 Clip **A** `07-02.mp4`: Slow lateral tracking shot along the quay; the barges glide upstream at walking pace; tow ropes tighten; the yellowish water ripples.

**07-03** · entra con «A veces se oye el chapoteo del agua contra…» → `07-03.jpg`
- Imagen: Close view of the wooden side of a laden Tiber barge, a taut tow rope, yellowish water lapping against the planks, a boatman on deck calling out the rhythm with a raised hand.
- 🎬 Clip **B** `07-03.mp4`: Close static shot; the river laps gently against the wooden planks; the tow rope trembles under tension; the boatman's arm gestures slowly, face not visible.

**07-04** · entra con «Ese puerto, sin embargo, tenía un problema: era demasiado…» → `07-04.jpg`
- Imagen: Aerial view at dusk of the hexagonal basin of Trajan's harbor at Portus near Fiumicino today, the calm six-sided lake surrounded by green fields and trees, distant airport lights glowing.

**07-05** · entra con «Grandes naves de carga de Alejandría, en Egipto, llenas…» → `07-05.jpg`
- Imagen: Large Roman cargo ships from Alexandria moored in the harbor of Portus, porters carrying grain sacks on their backs along wooden gangplanks onto river barges, a lighthouse in the distance.

**07-06** · entra con «Otros, los mensores, miden el grano con un recipiente…» → `07-06.jpg`
- Imagen: Close detail of Roman grain measurers filling a wooden modius with golden wheat, a scribe beside them recording on a wax tablet, sacks piled high in the background.

**07-07** · entra con «Algunas guardan trigo. Otras, aceite, vino, legumbres, telas, mármol,…» → `07-07.jpg`
- Imagen: Wide view of the courtyard of a brick Roman horreum, rows of identical long storerooms with thick walls and solid wooden doors, scribes taking notes while porters carry amphorae and sacks.

**07-08** · entra con «Quizá cuenta a quien quiera escucharle cómo es el…» → `07-08.jpg`
- Imagen: An old Roman sailor with a weathered face sitting on a stone step of the Tiber quay, gazing at the river, a coil of rope beside him, telling stories to a young porter resting nearby.

**07-09** · entra con «Por eso en otoño, en días como este de…» → `07-09.jpg`
- Imagen: Autumn sunlight glittering on the yellowish Tiber as a line of barges is towed upstream one after another, porters unloading sacks on the stone quay, trees along the banks.
- 🎬 Clip **A** `07-09.mp4`: Wide static shot; sunlight glitters and sparkles on the river; the line of barges moves slowly upstream; porters carry sacks on the quay in the distance.

**07-10** · entra con «La ciudad entera depende de este movimiento tranquilo y…» → `07-10.jpg`
- Imagen: A map of the Mediterranean painted on a plaster wall, small ships sailing from Egypt, Africa and Hispania toward Ostia and up the Tiber to Rome, an oil lamp on a shelf below it.

### `cap08` · El foro nuevo de Trajano (~7 min)

**08-01** · entra con «Si seguimos bajando, la calle se ensancha y desemboca…» → `08-01.jpg`
- Imagen: Wide view of the newly finished Forum of Trajan between the Capitoline and Quirinal hills, a vast white marble square framed by colonnades, visitors arriving and looking around in wonder, morning sun.
- 🎬 Clip **A** `08-01.mp4`: Very slow push-in across the white marble square; small figures walk calmly; long morning shadows of the colonnades; a light breeze moves a few banners.

**08-02** · entra con «Para construirlo, los arquitectos del emperador recortaron parte de…» → `08-02.jpg`
- Imagen: A gilded bronze equestrian statue of Emperor Trajan in the center of a white marble square surrounded by colonnaded porticoes, small figures of citizens walking around its base in morning sunlight.

**08-03** · entra con «El sol de la mañana brilla sobre ella. Al…» → `08-03.jpg`
- Imagen: Interior of the Basilica Ulpia, a vast hall with rows of colored marble columns and a very high timber roof, small groups of lawyers, merchants and citizens talking on the polished marble floor.

**08-04** · entra con «Detrás de la basílica, entre dos bibliotecas, una griega…» → `08-04.jpg`
- Imagen: Trajan's Column under construction between two library buildings, wooden scaffolding around the tall marble shaft, workers carving the lower spiral frieze, a treadwheel crane nearby, calm morning light.
- 🎬 Clip **B** `08-04.mp4`: Slow tilt up the column wrapped in scaffolding; tiny workers move calmly on the planks; clouds drift behind.

**08-05** · entra con «Son varios pisos de tiendas y oficinas organizados en…» → `08-05.jpg`
- Imagen: The semicircular red brick facade of Trajan's Markets set against the cut slope of the Quirinal hill, several stories of arched shop openings, an interior street with stairs and shoppers.

**08-06** · entra con «Una parte de ese grano se reparte gratis. Desde…» → `08-06.jpg`
- Imagen: Roman citizens queuing calmly under a portico to receive their monthly grain ration, an official pouring wheat from large sacks into a wooden modius, small bronze tokens in their hands.

**08-07** · entra con «Y una gran parte de ese aceite viene de…» → `08-07.jpg`
- Imagen: Close-up of large globular olive oil amphorae from Baetica with two handles and stamped clay surfaces, stacked in a warehouse near the Tiber, warm light on the terracotta.
- 🎬 Clip **B** `08-07.mp4`: Slow dolly along the stacked amphorae; dust motes float in warm shafts of light from a high window.

**08-08** · entra con «Ese montón de pedazos de ánforas, acumulado siglo tras…» → `08-08.jpg`
- Imagen: Monte Testaccio in Rome today at dusk, a grassy artificial hill whose exposed slopes reveal countless broken terracotta amphora shards, a few cypress trees and soft city lights around it.

**08-09** · entra con «Trajano nació en Itálica, una ciudad fundada por los…» → `08-09.jpg`
- Imagen: Wide view of the Roman city of Italica in Hispania near the Guadalquivir river, pale buildings, an amphitheater and olive groves under a warm southern sky, seen from a gentle hill.
- 🎬 Clip **A** `08-09.mp4`: Slow aerial approach over olive groves toward the Roman city of Italica; warm southern light; a faint haze over the Guadalquivir.

**08-10** · entra con «El Senado le ha dado el título de optimus…» → `08-10.jpg`
- Imagen: Close-up of bronze and silver Roman coins bearing the laurelled profile of Emperor Trajan lying on a wooden shop counter, a carved stone inscription with his name behind them, warm light.

**08-11** · entra con «El sol ha subido. Las sombras de las columnas…» → `08-11.jpg`
- Imagen: Midday in the Forum of Trajan: short shadows beneath the marble colonnades, the square filled with lawyers and clients, merchants, slaves on errands and wide-eyed visitors from the provinces.

### `cap09` · La hora sexta (~3 min)

**09-01** · entra con «A la hora sexta, Roma baja el ritmo. Los…» → `09-01.jpg`
- Imagen: A shaded Roman portico at midday, people eating a light meal of bread, cheese and fruit, some seated on stone steps, shop shutters half closed, the sunny street beyond quiet.

**09-02** · entra con «No es la comida importante del día. Esa llegará…» → `09-02.jpg`
- Imagen: A Roman man resting on a wooden bench in the shade of a garden pergola at midday, eyes closed, a half-eaten fig beside him, dappled sunlight and complete stillness.
- 🎬 Clip **A** `09-02.mp4`: Static shot; dappled sunlight shifts gently as pergola leaves move in a breeze; the resting man breathes slowly; nothing else moves.

**09-03** · entra con «Como esto ocurría alrededor de la hora sexta, la…» → `09-03.jpg`
- Imagen: Close detail of a Roman sundial at noon, the short shadow of the bronze gnomon resting on the carved sixth hour line, a cat sleeping curled at the base of the stone pedestal.
- 🎬 Clip **B** `09-03.mp4`: Close static shot; the cat's side rises and falls with slow breathing; the gnomon's short shadow barely moves; a leaf drifts past.

**09-04** · entra con «Se despertaba hacia la primera hora, a veces antes,…» → `09-04.jpg`
- Imagen: A dim shuttered room in a Roman country villa at dawn, a small distant figure of a wealthy writer dictating to a secretary who writes on a wax tablet, thin light through the shutters.

**09-05** · entra con «Era, claro, la vida de un hombre muy rico.…» → `09-05.jpg`
- Imagen: A colonnaded garden walk of a Roman villa in the afternoon, a gravel path between box hedges and plane trees, a stone bench with a scroll left on it, quiet and unhurried.

### `cap10` · Las mujeres de Roma (~7 min)

**10-01** · entra con «Volvamos a la insula del tercer piso. A la…» → `10-01.jpg`
- Imagen: A woman in a simple undyed wool tunic and brown shawl sitting by the window of her third-floor insula room spinning wool with a distaff, a basket of vegetables and a broom nearby, soft midday light.
- 🎬 Clip **A** `10-01.mp4`: Static medium-wide shot from behind and to the side of the woman; the spindle turns slowly and the wool thread lengthens; a curtain at the window stirs; her face stays out of focus.

**10-02** · entra con «Hilar lana es, para los romanos, el símbolo de…» → `10-02.jpg`
- Imagen: Close-up of a Roman tombstone carved with a short Latin epitaph for a woman named Claudia, a distaff and spindle carved in relief beneath the text, moss and soft light on the stone.

**10-03** · entra con «Pero la realidad de Roma era más variada que…» → `10-03.jpg`
- Imagen: A row of Roman tabernae run by women: a fish seller at her counter, a perfume seller arranging small bottles, a seamstress sewing, and a hairdresser arranging a client's hair.

**10-04** · entra con «Su marido murió hace años y ella siguió con…» → `10-04.jpg`
- Imagen: Inside a cloth shop on the ground floor of an insula, a middle-aged widow in a dark stola bargaining firmly with a supplier over bolts of dyed wool, shelves of fabric behind her.

**10-05** · entra con «Una mujer puede tener sus propios bienes, heredar, comprar,…» → `10-05.jpg`
- Imagen: A marble statue of a Roman benefactress in a draped stola on an inscribed pedestal in front of a portico she paid for, citizens walking past in afternoon light.

**10-06** · entra con «Dirige a los esclavos de la casa, lleva las…» → `10-06.jpg`
- Imagen: The senator's wife, a matron in a long pale blue stola, seated in the peristyle of the domus reviewing household accounts on wax tablets while slaves stand nearby awaiting instructions.

**10-07** · entra con «Cuenta también que pone música a sus versos y…» → `10-07.jpg`
- Imagen: A young Roman woman in a light stola playing a cithara in a quiet garden, a papyrus scroll of verses on her lap, seen from a distance between columns, gentle afternoon light.
- 🎬 Clip **B** `10-07.mp4`: Wide shot through the columns; leaves sway gently; the woman's hand moves slowly over the cithara strings; she remains small and distant.

**10-08** · entra con «Y hay un grupo pequeño de mujeres con un…» → `10-08.jpg`
- Imagen: The House of the Vestal Virgins beside the Roman Forum, a colonnaded courtyard with long pools and marble statues, the small round Temple of Vesta nearby with a thin wisp of smoke.

**10-09** · entra con «Mira por la ventana. Abajo, en la calle, la…» → `10-09.jpg`
- Imagen: Looking down from an insula window onto a lively Roman street after the midday rest, a neighbor hanging a tunic from the window opposite, the widow's cloth shop below with a laughing customer.

### `cap11` · El Circo Máximo en silencio (~7 min)

**11-01** · entra con «Hoy no hay carreras. Pero vamos a ir de…» → `11-01.jpg`
- Imagen: Wide view of the empty Circus Maximus in afternoon light, a long sandy track in the valley between the Palatine and Aventine hills, tiered stands on both sides and starting gates at one end.

**11-02** · entra con «Las gradas pueden acoger a decenas de miles de…» → `11-02.jpg`
- Imagen: The tiered seating of the Circus Maximus seen from within the stands, endless rows of empty stone seats stretching into the distance, a modest imperial seating area among them.

**11-03** · entra con «En el centro de la pista corre una barrera…» → `11-03.jpg`
- Imagen: The red granite Flaminio obelisk with its hieroglyphs in Piazza del Popolo in Rome today, at dusk, the square calm and almost empty, soft lamplight on the stone lion fountains at its base.

**11-04** · entra con «En cada vuelta de la carrera, se baja un…» → `11-04.jpg`
- Imagen: Close detail of the lap counters on the circus barrier, seven large stone eggs and seven bronze dolphins, with slaves watering the smooth raked sand of the empty track with buckets below.

**11-05** · entra con «El caballo resopla y sacude la crin. Debajo de…» → `11-05.jpg`
- Imagen: A stable boy leading a single unharnessed horse at a walk along the empty sandy track of the Circus Maximus, the horse shaking its mane, shops and taverns under the outer arcades behind.
- 🎬 Clip **A** `11-05.mp4`: Wide static shot; the stable boy leads the horse at a calm walk along the sandy track; the horse shakes its mane once; fine dust drifts.

**11-06** · entra con «Los aurigas compiten por cuatro equipos, las facciones, cada…» → `11-06.jpg`
- Imagen: Close-up of four wool scarves in white, red, green and blue, the colors of the circus factions, hanging from a peg in a Roman tavern beside a faded wall painting of a distant chariot race.

**11-07** · entra con «Murió muy joven, antes de cumplir los treinta años,…» → `11-07.jpg`
- Imagen: A quiet marble funerary relief of a young charioteer standing beside a palm branch and victory wreaths, set into a roadside tomb among cypress trees in soft afternoon light.

**11-08** · entra con «Le asombraba, escribe, que tantos miles de hombres adultos…» → `11-08.jpg`
- Imagen: A peaceful study in a Roman villa, a small distant figure of a writer reading a scroll at a table by an open shutter, the garden outside calm and green, far from any crowd.

**11-09** · entra con «Plinio escribe todo esto con una sonrisa. Y añade…» → `11-09.jpg`
- Imagen: View from a sun-warmed stone step high in the Circus Maximus, looking up toward the walls and arches of the imperial palace on the Palatine hill, golden afternoon light.

**11-10** · entra con «Y hacia abajo, la pista larga y vacía, que…» → `11-10.jpg`
- Imagen: The long empty track of the Circus Maximus fading into golden late-afternoon haze, the shadow of the Aventine hill stretching slowly across the raked sand, a lone figure with a bucket far away.
- 🎬 Clip **A** `11-10.mp4`: Locked-off wide shot; the shadow of the hill creeps slowly across the raked sand like a gentle time-lapse; the golden haze deepens.

### `cap12` · Las termas (~7 min)

**12-01** · entra con «Para los romanos, ir a las termas por la…» → `12-01.jpg`
- Imagen: Aerial view of the Baths of Trajan on the Esquiline hill, a vast symmetrical complex of vaulted halls, domes, gardens and porticoes, smaller neighborhood baths scattered in the surrounding streets.

**12-02** · entra con «Vamos allí. La entrada es casi gratis. En muchos…» → `12-02.jpg`
- Imagen: The grand entrance portal of the Baths of Trajan in the afternoon, people of every kind walking in together, a senator, a shoemaker, slaves and children, a small bronze coin handed over at the door.

**12-03** · entra con «Lo primero es el vestuario, el apodyterium. Es una…» → `12-03.jpg`
- Imagen: Interior of a Roman apodyterium: stone benches along the walls and a row of niches above holding folded tunics and sandals, a slave sitting quietly on guard beside his master's clothes.

**12-04** · entra con «Te pones unas zapatillas de suela gruesa de madera,…» → `12-04.jpg`
- Imagen: Close-up of Roman bathing items on a stone bench: thick wooden-soled bath clogs, a small round oil flask on a cord and a curved bronze strigil, soft light from a high window.

**12-05** · entra con «Otros simplemente pasean y conversan a la sombra de…» → `12-05.jpg`
- Imagen: The palaestra of a Roman bath, an open courtyard surrounded by porticoes, men tossing a ball by hand, others lifting lead weights, and pairs strolling and talking in the shade of the columns.

**12-06** · entra con «Después, el caldarium, la sala caliente. Al entrar, el…» → `12-06.jpg`
- Imagen: Cutaway view of a Roman caldarium, bathers relaxing in a large hot pool under a steamy vaulted ceiling, and beneath the floor rows of small brick pillars of the hypocaust carrying warm air.
- 🎬 Clip **B** `12-06.mp4`: Slow push-in; steam rises and swirls under the vaulted ceiling; the hot water surface ripples softly; figures stay relaxed and still.

**12-07** · entra con «Las voces resuenan contra las bóvedas. Por las ventanas…» → `12-07.jpg`
- Imagen: Inside a steamy caldarium lit by golden afternoon light through high windows, a bath attendant scraping oil from a seated man's back with a curved bronze strigil in long careful strokes.
- 🎬 Clip **A** `12-07.mp4`: Static shot; golden light beams through the high windows and the steam drifts slowly through them; the strigil moves in one slow stroke.

**12-08** · entra con «Y luego, con el cuerpo limpio y caliente, llega…» → `12-08.jpg`
- Imagen: A large cool frigidarium pool in a high vaulted hall of colored marble, a bather slowly stepping down into the clear water, another sitting wrapped in a linen towel on a bench nearby.
- 🎬 Clip **A** `12-08.mp4`: Static shot; the bather steps slowly into the pool and gentle ripples spread across the clear water, reflecting the marble and light.

**12-09** · entra con «Los gemidos de los que levantaban pesas, resoplando con…» → `12-09.jpg`
- Imagen: View from a small upper-floor window looking down into a lively bath courtyard below: weightlifters, a masseur at work, a ball game and a splash in a pool, all small and seen from far above.

**12-10** · entra con «Y los vendedores de pasteles, de salchichas y de…» → `12-10.jpg`
- Imagen: Food vendors with trays of honey cakes, sausages and sweets walking through the colonnaded gardens of the Baths of Trajan, people resting on benches and reading near a library doorway.

**12-11** · entra con «Hay gente que viene solo a conversar, a ver…» → `12-11.jpg`
- Imagen: Two Roman friends in tunics chatting on a marble bench under a portico of the Baths of Trajan in late afternoon, the sun slanting low, the garden calm behind them.

### `cap13` · La cena (~5 min)

**13-01** · entra con «La cena romana empieza pronto, a media tarde, cuando…» → `13-01.jpg`
- Imagen: The triclinium of the senator's domus: three couches in a U-shape around a low table, guests reclining on their left elbows on cushions, red painted walls and bronze lamps, late afternoon light.

**13-02** · entra con «Cada lugar tiene su importancia. El anfitrión y sus…» → `13-02.jpg`
- Imagen: Close-up of the first course of a Roman dinner on a low table: boiled eggs, olives, mushrooms, lettuce, oysters on a platter and small sausages in silver and terracotta dishes.

**13-03** · entra con «Después, el plato principal: carne asada o guisada, pescado,…» → `13-03.jpg`
- Imagen: A Roman main course on a bronze tray: roast fowl, grilled fish and a stew beside a small jug of garum, with a dessert bowl of figs, grapes, nuts and honey cakes waiting nearby.

**13-04** · entra con «Y durante toda la cena, vino. Casi siempre mezclado…» → `13-04.jpg`
- Imagen: A slave mixing wine and water in a large bronze krater with a ladle, while beyond him a few friends recline in calm conversation as the first oil lamps are lit in the triclinium.
- 🎬 Clip **B** `13-04.mp4`: Static shot; wine and water pour slowly from the ladle into the bronze krater; behind, oil-lamp flames flicker; the guests barely move.

**13-05** · entra con «Marcial, en algunos epigramas, invita a un amigo a…» → `13-05.jpg`
- Imagen: A modest table set for two friends in a simple Roman dining room: garden vegetables, eggs, a piece of cheese, olives, a little meat and fruit, lit by a single oil lamp.

**13-06** · entra con «Hay puls, una papilla espesa de cereal, una especie…» → `13-06.jpg`
- Imagen: Close-up of a humble Roman supper on a small wooden table: a clay bowl of thick puls porridge, beans, cabbage and onion, a round loaf of bread, salted sardines and a cup of watered wine.

**13-07** · entra con «El hombre habla de su trabajo, del precio del…» → `13-07.jpg`
- Imagen: The insula family sharing supper around a small table by the window: the husband in a plain brown tunic, a woman in a simple undyed wool tunic and brown shawl serving food, two children and the grandmother, an orange sunset sky outside.

### `cap14` · La noche vuelve a Roma (~6 min)

**14-01** · entra con «Cuando el sol se pone, Roma cambia otra vez.…» → `14-01.jpg`
- Imagen: A Roman shopkeeper sliding wooden planks back into the grooves of his shop front at sunset, a barber folding up his stool nearby, the street emptying under an orange and violet sky.
- 🎬 Clip **A** `14-01.mp4`: Static shot at sunset; the shopkeeper slowly slides one wooden plank into its groove; long orange shadows; the street empties in the background.

**14-02** · entra con «Dan una luz pequeña, amarilla, temblorosa. En las casas…» → `14-02.jpg`
- Imagen: Close-up of a small oval clay oil lamp with a central filling hole and a burning wick in its nozzle, casting a small trembling yellow light, a tall bronze candelabrum faintly visible behind.
- 🎬 Clip **A** `14-02.mp4`: Extreme close static shot; the small lamp flame flickers and trembles gently, casting moving warm light on the wall; nothing else moves.

**14-03** · entra con «Quien sale de noche, lleva su propia luz: una…» → `14-03.jpg`
- Imagen: A wealthy Roman walking home along a dark quiet street at night, a slave ahead of him holding a bronze hand lantern, the moon above the tall insulae, every shutter closed.

**14-04** · entra con «Dice que eres un descuidado si sales a cenar…» → `14-04.jpg`
- Imagen: Wide view of a quiet night street: vigiles passing with torches and looking up at the windows, a mule-drawn cart entering slowly behind them, iron-rimmed wheels on the basalt stones, soft moonlight.

**14-05** · entra con «Y debajo de todo, como siempre, el agua de…» → `14-05.jpg`
- Imagen: The darkened atrium of the senator's domus at night, the shallow impluvium pool reflecting a square of starry sky from the roof opening, a slave extinguishing the last bronze lamp.
- 🎬 Clip **A** `14-05.mp4`: Slow tilt down from the roof opening to the dark impluvium pool; the reflected stars tremble on the water; a lamp is gently extinguished in the background.

**14-06** · entra con «En la insula, la familia del tercer piso se…» → `14-06.jpg`
- Imagen: The third-floor insula room at night lit by one small clay oil lamp, the family settling into wooden beds, the grandmother already asleep, a woman in a simple undyed wool tunic and brown shawl checking that the brazier is cold.

**14-07** · entra con «En la oscuridad, la habitación se llena de los…» → `14-07.jpg`
- Imagen: Dark silhouettes of Roman insulae and rooftops under a deep blue night sky full of stars, a single distant cart lantern moving along a street far below, quiet and still.
- 🎬 Clip **B** `14-07.mp4`: Locked-off night shot; stars twinkle; a single tiny lantern moves slowly along a distant street far below.

**14-08** · entra con «Hace casi dos mil años de esto. Y, sin…» → `14-08.jpg`
- Imagen: A high, wide view over sleeping ancient Rome at night, moonlight on the Tiber, the Forum of Trajan and the aqueduct arches, only a few tiny lamp lights still glowing in windows.
- 🎬 Clip **A** `14-08.mp4`: Very slow aerial drift over the sleeping city; moonlight shimmers on the Tiber; one or two tiny lamp lights go out.

**14-09** · entra con «Escucha el agua que cae, despacio, sin prisa, en…» → `14-09.jpg`
- Imagen: Close view of the corner stone fountain at night, a calm stream of water falling from the bronze spout into the brimming basin, moonlight shimmering on the ripples, the empty street behind.
- 🎬 Clip **A** `14-09.mp4`: Static close shot; the calm stream falls into the brimming basin; moonlight shimmers on the ripples; slowly fade toward darkness.
