#!/usr/bin/env python3
import os

B = "wiki-docs/regions/villages"
os.makedirs(B, exist_ok=True)

def w(p, c):
    with open(p, "w", encoding="utf-8") as f:
        f.write(c)

def box(img_file, name, ep, fields, prefix='../../img/'):
    r = '<div class="wiki-infobox" markdown>\n\n'
    if img_file:
        r += '![' + name + '](' + prefix + img_file + '){ .wiki-infobox-img }\n\n'
    r += '<div class="wiki-infobox-name">' + name + '</div>\n'
    r += '<div class="wiki-infobox-epithet">' + ep + '</div>\n\n<dl>\n'
    for k, v in fields:
        r += '<dt>' + k + '</dt><dd>' + v + '</dd>\n'
    r += '</dl>\n\n</div>\n\n'
    return r

def page(title, desc, infobox, body):
    return '---\ndescription: ' + desc + '\n---\n\n# ' + title + '\n\n' + infobox + body + '\n'

# ── Index EN ──
w(B + '/index.md', '''---
description: The towns and villages of Galluvinchia, from the Jewel of Evergrowth and Pharoes to Lakobordo, Rivabordo and the hamlets in between.
---

# Villages and Towns

Beyond the four great cities, Galluvinchia is dotted with towns and villages, each with its own character, its own patron, and its own secrets.

<div class="grid cards" markdown>

-   **[Jewel of Evergrowth](jewel-of-evergrowth.md)**

    ---

    Island hamlet growing under the First Tree, home of the goddess Leeve. A new silver mine is changing everything.

-   **[Doormi](doormi.md)**

    ---

    Liberal cliff-top town by waterfalls, home of the Academy of Magic Waves and Dreams.

-   **[Pharoes](pharoes.md)**

    ---

    Southern port named for its great lighthouse. The largest Abbey of Brenadette in all Galluvinchia.

-   **[Lakobordo](lakobordo.md)**

    ---

    Commerce hub at the crossroads of Galluvinchia, connecting north, south, east, and west.

-   **[An\'Zulejosh](anzulejosh.md)**

    ---

    Northern coastal port decorated with colorful mosaic tiles, nexus of trade and travel.

-   **[Montebordo](montebordo.md)**

    ---

    A shrinking village inside Carbohyrr\'s walls, finding new faith after the burning of its abbey.

-   **[Rivabordo](rivabordo.md)**

    ---

    Exporter of wood and cheese to the North, home to people notoriously difficult to get along with.

-   **[Whisk of Lumin](whisk-of-lumin.md)**

    ---

    Eastern gateway founded by Lumin Oldreekia, its towers watching for ghouls from the desert.

-   **[The Neverender](neverender.md)**

    ---

    The realm below, final destination for the souls of the living, watched over by Brenadette.

</div>
''')

# ── Index ES ──
w(B + '/index.es.md', '''---
description: Los pueblos y aldeas de Galluvinchia, desde la Joya Siemprecreciente y Pharoes hasta Lakobordo, Rivabordo y los caseríos intermedios.
---

# Aldeas y Pueblos

Más allá de las cuatro grandes ciudades, Galluvinchia está salpicada de pueblos y aldeas, cada uno con su propio carácter, su propio patrón y sus propios secretos.

<div class="grid cards" markdown>

-   **[Joya Siemprecreciente](jewel-of-evergrowth.md)**

    ---

    Aldea isleña que crece bajo el Primer Árbol, hogar de la diosa Leeve. Una nueva mina de plata está cambiándolo todo.

-   **[Doormi](doormi.md)**

    ---

    Pueblo liberal en acantilados junto a cascadas, sede de la Academia de las Ondas Étereas y los Sueños.

-   **[Pharoes](pharoes.md)**

    ---

    Puerto del sur bautizado por su gran faro. La mayor Abadía de Brenadette de toda Galluvinchia.

-   **[Lakobordo](lakobordo.md)**

    ---

    Centro comercial en el cruce de caminos de Galluvinchia, conectando norte, sur, este y oeste.

-   **[An\'Zulejosh](anzulejosh.md)**

    ---

    Puerto costero del norte decorado con coloridos mosaicos, nexo de comercio y viajes.

-   **[Montebordo](montebordo.md)**

    ---

    Una aldea menguante dentro de las murallas de Carbohyrr, que encuentra nueva fe tras el incendio de su abadía.

-   **[Rivabordo](rivabordo.md)**

    ---

    Exportador de madera y queso al Norte, hogar de gente notoriamente difícil de tratar.

-   **[Whisk de Lumin](whisk-of-lumin.md)**

    ---

    Puerta oriental fundada por Lumin Oldreekia, con torres vigilando a los necrófagos del desierto.

-   **[El Rencarnatorno](neverender.md)**

    ---

    El reino de abajo, destino final de las almas de los vivos, vigilado por Brenadette.

</div>
''')

# ── Individual village pages ──

w(B + '/jewel-of-evergrowth.md', page(
    'Jewel of Evergrowth',
    'The Jewel of Evergrowth, an island hamlet growing under the First Tree and home of the goddess Leeve, transformed by a new silver mine.',
    box(None, 'Jewel of Evergrowth', 'Island Hamlet · Blessed by Leeve',
        [('Type', 'Island hamlet'), ('Patron', 'Leeve'), ('Location', 'Southern island'), ('Status', 'Growing')]),
    '''A hamlet growing under the shadow of the **First Tree**, the Jewel of Evergrowth is home to the goddess [Leeve](../../gods/leeve.md). It is a place where people can live free and simple lives, blessed with beautiful flowers and the gentlest nature.

Recently, a new silver mine opened on the island, and with it came growth: new families, new merchants, new visitors. The market is abundant and lively, and the island feels full of possibility.

But not all stories here are simple ones. The walls of the mine are not entirely silent.
'''))

w(B + '/jewel-of-evergrowth.es.md', page(
    'Joya Siemprecreciente',
    'La Joya Siemprecreciente, una aldea isleña que crece bajo el Primer Árbol y hogar de la diosa Leeve, transformada por una nueva mina de plata.',
    box(None, 'Joya Siemprecreciente', 'Aldea Isleña · Bendecida por Leeve',
        [('Tipo', 'Aldea isleña'), ('Patrón', 'Leeve'), ('Ubicación', 'Isla del sur'), ('Estado', 'En crecimiento')]),
    '''Una aldea que crece bajo la sombra del **Primer Árbol**, la Joya Siemprecreciente es el hogar de la diosa [Leeve](../../gods/leeve.md). Es un lugar donde la gente puede llevar una vida libre y sencilla, bendecida con hermosas flores y la naturaleza más gentil.

Recientemente, se abrió una nueva mina de plata en la isla, y con ella llegó el crecimiento: nuevas familias, nuevos mercaderes, nuevos visitantes.

Pero no todas las historias aquí son sencillas. Las paredes de la mina no están del todo en silencio.
'''))

w(B + '/doormi.md', page(
    'Doormi',
    'Doormi, the liberal cliff-top village by the waterfalls, home of the Academy of Magic Waves and Dreams.',
    box(None, 'Doormi', 'The Village by the Waterfalls · Blessed by Morphia',
        [('Type', 'Town'), ('Patron', 'Morphia'), ('Location', 'Coastal cliffs'), ('Known for', 'Academy · Magical garments · Mushrooms')]),
    '''Doormi is a liberal and relaxed town situated on cliffs beside waterfalls, home to the **[Academy of Magic Waves and Dreams](../../characters/merrion-meyer.md)**, led by [Merrion Meyer](../../characters/merrion-meyer.md). The academy offers the first year of study free for brilliant students, making magic more accessible than anywhere else in Galluvinchia.

The town is the biggest producer of **magical garments** and, notably, **mushrooms of every kind**. Its easygoing population attracts artists, healers, and anyone seeking knowledge or inner peace.
'''))

w(B + '/doormi.es.md', page(
    'Doormi',
    'Doormi, el pueblo liberal en los acantilados junto a cascadas, sede de la Academia de las Ondas Étereas y los Sueños.',
    box(None, 'Doormi', 'El Pueblo junto a las Cascadas · Bendecido por Morphia',
        [('Tipo', 'Pueblo'), ('Patrón', 'Morphia'), ('Ubicación', 'Acantilados costeros'), ('Conocido por', 'Academia · Prendas mágicas · Setas')]),
    '''Doormi es un pueblo liberal y relajado situado en acantilados junto a cascadas, sede de la **Academia de las Ondas Étereas y los Sueños**, dirigida por [Merrion Meyer](../../characters/merrion-meyer.md). La academia ofrece el primer año de estudio gratuito para los estudiantes más brillantes.

El pueblo es el mayor productor de **prendas mágicas** y, notablemente, **setas de todo tipo**.
'''))

w(B + '/pharoes.md', page(
    'Pharoes',
    'Pharoes, the southern port town named for its great lighthouse, home of the largest Abbey of Brenadette in Galluvinchia.',
    box(None, 'Pharoes', 'The Port of the South · Home of the Abbey of Brenadette',
        [('Type', 'Port town'), ('Patron', 'Brenadette'), ('Location', 'Southern coast')]),
    '''Named for the great lighthouse that guides ships through stormy southern waters. Pharoes connects Lorda Gorda with the south of Galluvinchia, and many merchants use this port to bring their goods ashore.

The city is battered by constant storms, which has made [Brenadette](../../gods/brenadette.md) an even more immediate presence here. The locals revere her not only as goddess of death but as the **Goddess of the Tempest**. The largest Abbey of Brenadette in all of Galluvinchia stands in Pharoes.

*As many fish in the sea as prayers in the air.*
'''))

w(B + '/pharoes.es.md', page(
    'Pharoes',
    'Pharoes, el puerto del sur bautizado por su gran faro, hogar de la mayor Abadía de Brenadette de Galluvinchia.',
    box(None, 'Pharoes', 'El Puerto del Sur · Sede de la Abadía de Brenadette',
        [('Tipo', 'Puerto'), ('Patrón', 'Brenadette'), ('Ubicación', 'Costa sur')]),
    '''Bautizado por el gran faro que guía a los barcos a través de las tormentosas aguas del sur. Pharoes conecta Lorda Gorda con el sur de Galluvinchia.

La ciudad está azotada por tormentas constantes, lo que ha hecho de [Brenadette](../../gods/brenadette.md) una presencia aún más inmediata aquí. Los locales la veneran no solo como diosa de la muerte sino como la **Diosa de la Tempestad**. La mayor Abadía de Brenadette de toda Galluvinchia se encuentra en Pharoes.

*Tantos peces en el mar como oraciones en el aire.*
'''))

w(B + '/lakobordo.md', page(
    'Lakobordo',
    'Lakobordo, the commerce hub at the crossroads of Galluvinchia, connecting north, south, east and west.',
    box(None, 'Lakobordo', 'The Commerce Hub · Heart of Galluvinchia\'s Roads',
        [('Type', 'City'), ('Location', 'Valley of the Lush Basin'), ('Known for', 'Gastronomy · Trade · Crossroads')]),
    '''South from Doormi, in the valley of the Lush Basin, lies Lakobordo, a city known for its gastronomy and its position at the crossroads of Galluvinchia. It connects Pharoes, Doormi, and the Lord of Carbohyrr with the North, making it the hub of overland trade across the continent.

Among its citizens, one baker named **[Agustin of Carzagus](../../characters/agustin.md)** has become locally famous, not just for his extraordinary croissants, but for the mysterious silver pendant he carries, whose origin no one can explain.
'''))

w(B + '/lakobordo.es.md', page(
    'Lakobordo',
    'Lakobordo, el centro comercial en el cruce de caminos de Galluvinchia, que conecta el norte, el sur, el este y el oeste.',
    box(None, 'Lakobordo', 'El Centro Comercial · Corazón de las Rutas de Galluvinchia',
        [('Tipo', 'Ciudad'), ('Ubicación', 'Valle de la Cuenca Exuberante'), ('Conocido por', 'Gastronomía · Comercio · Cruce de caminos')]),
    '''Al sur de Doormi, en el valle de la Cuenca Exuberante, se encuentra Lakobordo, una ciudad conocida por su gastronomía y su posición en el cruce de caminos de Galluvinchia. Conecta Pharoes, Doormi y el Señor de Carbohyrr con el Norte.

Entre sus ciudadanos, un panadero llamado **[Agustín de Carzagus](../../characters/agustin.md)** se ha hecho localmente famoso, no solo por sus extraordinarios cruasanes, sino por el misterioso colgante de plata que lleva consigo.
'''))

w(B + '/anzulejosh.md', page(
    "An'Zulejosh",
    "An'Zulejosh, the northern coastal port decorated with colorful mosaic tiles, nexus of trade and travel.",
    box(None, "An'Zulejosh", 'The Tile City · Northern Coastal Port',
        [('Type', 'Port town'), ('Location', 'Northern coast, west of Lady of Marmaros'), ('Known for', 'Mosaic tiles · Trade hub')]),
    '''West from the Lady of Marmaros, surrounded by clay hills, An\'Zulejosh is the main coastal port of the north. Its houses are decorated with colorful mosaic tiles, and the city is perpetually crowded with temporary visitors.

A nexus between the Jewel of Evergrowth, An\'Ramoda, and the Lady of Marmaros, merchants, sailors, and travelers all pass through. The stories told in its taverns span the breadth of Galluvinchia.
'''))

w(B + '/anzulejosh.es.md', page(
    "An'Zulejosh",
    "An'Zulejosh, el puerto costero del norte decorado con coloridos mosaicos, nexo de comercio y viajes.",
    box(None, "An'Zulejosh", 'La Ciudad de los Mosaicos · Puerto Costero del Norte',
        [('Tipo', 'Puerto'), ('Ubicación', 'Costa norte, al oeste de la Dama de Mármaros'), ('Conocido por', 'Mosaicos de colores · Hub comercial')]),
    '''Al oeste de la Dama de Mármaros, rodeada de colinas de arcilla, An\'Zulejosh es el principal puerto costero del norte. Sus casas están decoradas con coloridos mosaicos, y la ciudad está perpetuamente llena de visitantes temporales.

Nexo entre la Joya Siemprecreciente, An\'Ramoda y la Dama de Mármaros, mercaderes, marineros y viajeros pasan por aquí.
'''))

w(B + '/montebordo.md', page(
    'Montebordo',
    'Montebordo, a shrinking village inside the walls of Carbohyrr, finding new faith in a local deity after its abbey burned.',
    box(None, 'Montebordo', 'The Hidden Village · Followers of the Mountain',
        [('Type', 'Village'), ('Location', 'Inside Lord of Carbohyrr walls'), ('Status', 'Declining')]),
    '''Inside the walls of Carbohyrr, this small village strives to survive as its population slowly declines. After the Abbey of Brenadette was torn apart by flames, the locals found new hope in their own local deity: the goddess of the mountain.

Montebordo is remote and full of pagans, the kind of place one stumbles into rather than plans to visit.
'''))

w(B + '/montebordo.es.md', page(
    'Montebordo',
    'Montebordo, una aldea menguante dentro de las murallas de Carbohyrr, que encuentra nueva fe en una deidad local tras el incendio de su abadía.',
    box(None, 'Montebordo', 'El Pueblo Oculto · Seguidores de la Montaña',
        [('Tipo', 'Aldea'), ('Ubicación', 'Dentro de las murallas del Señor de Carbohyrr'), ('Estado', 'En declive')]),
    '''Dentro de las murallas de Carbohyrr, este pequeño pueblo lucha por sobrevivir mientras su población disminuye lentamente. Tras el incendio de la Abadía de Brenadette, los locales encontraron nueva esperanza en su propia deidad local: la diosa de la montaña.

Montebordo es remoto y está lleno de paganos, el tipo de lugar en el que uno tropieza en lugar de visitar por elección.
'''))

w(B + '/rivabordo.md', page(
    'Rivabordo',
    'Rivabordo, a small town exporting wood and cheese to the North, home to notoriously difficult people.',
    box(None, 'Rivabordo', 'The Wood and Cheese Town',
        [('Type', 'Town'), ('Location', 'Central Galluvinchia'), ('Exports', 'Wood, cheese')]),
    '''In a peculiar corner of Galluvinchia, this small town is the main exporter of wood and cheese to the North. The surrounding forests are lush, the dairy farms are prolific, and the people, it is said, are among the most difficult to get along with in the land.
'''))

w(B + '/rivabordo.es.md', page(
    'Rivabordo',
    'Rivabordo, un pequeño pueblo que exporta madera y queso al Norte, hogar de gente notoriamente difícil de tratar.',
    box(None, 'Rivabordo', 'El Pueblo de la Madera y el Queso',
        [('Tipo', 'Pueblo'), ('Ubicación', 'Galluvinchia Central'), ('Exportaciones', 'Madera, queso')]),
    '''En un peculiar rincón de Galluvinchia, este pequeño pueblo es el principal exportador de madera y queso al Norte. Los bosques circundantes son exuberantes, las granjas lecheras son prolíficas, y la gente, según se dice, es de las más difíciles de tratar de toda la tierra.
'''))

w(B + '/whisk-of-lumin.md', page(
    'Whisk of Lumin',
    'The Whisk of Lumin, eastern gateway founded by the legendary Lumin Oldreekia, its towers watching for ghouls from the desert.',
    box(None, 'Whisk of Lumin', 'Gateway to the East · Tower of Vigil',
        [('Type', 'Town · Fortress'), ('Founder', 'Lumin Oldreekia'), ('Location', 'Eastern Galluvinchia'), ('Role', 'Eastern watchtower · Trade gate to Lorda Gorda')]),
    '''Founded by the legendary felinfolk hero **[Lumin Oldreekia](../../characters/lumin-oldreekia.md)**, the first king of Lorda Gorda, the Whisk of Lumin stands as the main inland connection to the fortress island. Its towers watch the eastern horizon night and day, signaling when ghouls surge from the desert.

Recent tensions have arisen: Lorda Gorda is growing in power, and the ghoul attacks from the East are not stopping. The Whisk holds, for now.
'''))

w(B + '/whisk-of-lumin.es.md', page(
    'Whisk de Lumin',
    'El Whisk de Lumin, puerta oriental fundada por el legendario Lumin Oldreekia, con torres que vigilan a los necrófagos del desierto.',
    box(None, 'Whisk de Lumin', 'Puerta al Este · Torre de Vigía',
        [('Tipo', 'Pueblo · Fortaleza'), ('Fundador', 'Lumin Oldreekia'), ('Ubicación', 'Este de Galluvinchia'), ('Rol', 'Torre de vigilancia oriental · Puerta de comercio a Lorda Gorda')]),
    '''Fundado por el legendario héroe felicio **[Lumin Oldreekia](../../characters/lumin-oldreekia.md)**, el primer rey de Lorda Gorda, el Whisk de Lumin es la principal conexión terrestre con la fortaleza-isla. Sus torres vigilan el horizonte oriental noche y día.

Las tensiones recientes han aumentado: Lorda Gorda está creciendo en poder, y los ataques de necrófagos desde el Este no se detienen. El Whisk aguanta, por ahora.
'''))

w(B + '/neverender.md', page(
    'The Neverender',
    'The Neverender, the realm below Galluvinchia, final resting place for the souls of the living, watched over by Brenadette.',
    box('artwork-neverender.webp', 'The Neverender', 'The Realm Below · Final Rest of Souls',
        [('Type', 'Afterlife realm'), ('Ruler', 'Brenadette'), ('Access', 'Death · Rare passage for the living')]),
    '''Deep below the entrails of Galluvinchia lies the Neverender, the last destination for the souls of the living. Here, the river of souls meets its fate, joining the **Renewal** to become new souls, born again into bodies on the surface.

Tales tell of cities of echoes deep within, where shades share meals with the living who wander in searching for lost ones. Whether such stories are true, or merely consolation, is a question each traveler must answer for themselves.

[Brenadette](../../gods/brenadette.md) watches over this place, and has been bound to it since the Age of Gods. The perpetual sight of its light left her blind. She has never slept again.
'''))

w(B + '/neverender.es.md', page(
    'El Rencarnatorno',
    'El Rencarnatorno, el reino bajo Galluvinchia, destino final de las almas de los vivos, vigilado por Brenadette.',
    box('artwork-neverender.webp', 'El Rencarnatorno', 'El Reino de Abajo · Descanso Final de las Almas',
        [('Tipo', 'Reino del más allá'), ('Gobernante', 'Brenadette'), ('Acceso', 'Muerte · Paso raro para los vivos')]),
    '''En las profundidades de las entrañas de Galluvinchia se encuentra el Rencarnatorno, el último destino de las almas de los vivos. Aquí, el río de almas encuentra su destino, uniéndose al **Resurgimiento** para convertirse en nuevas almas, nacidas de nuevo en cuerpos en la superficie.

Los relatos hablan de ciudades de ecos en su interior, donde las sombras comparten comidas con los vivos que vagan buscando a sus seres queridos perdidos.

[Brenadette](../../gods/brenadette.md) vigila este lugar, y ha estado ligada a él desde la Era de los Dioses. La visión perpetua de su luz la dejó ciega. Nunca ha vuelto a dormir.
'''))

print("Done villages.")
