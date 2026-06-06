#!/usr/bin/env python3
import os

B = "wiki-docs/regions/cities"
os.makedirs(B, exist_ok=True)

def w(p, c):
    with open(p, "w", encoding="utf-8") as f:
        f.write(c)

def box(img_file, name, ep, fields, img_prefix='../../img/'):
    r = '<div class="wiki-infobox" markdown>\n\n'
    if img_file:
        r += '![' + name + '](' + img_prefix + img_file + '){ .wiki-infobox-img }\n\n'
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
description: The great cities of Galluvinchia, An\'Ramoda, the Lady of Marmaros, the Lord of Carbohyrr and Lorda Gorda, their people, power and history.
---

# Cities of Galluvinchia

The cities of Galluvinchia are more than centers of trade, they are statements. Every wall, every gate, every tower declares who built it, who rules it now, and what gods they keep.

Three great cities are protected by the Keepers of Galluvinchia. A fourth stands apart, proud and independent.

<div class="grid cards" markdown>

-   **[An\'Ramoda](anramoda.md)**

    ---

    The walled northern city, seat of Aremedia and home of the greatest army in Galluvinchia.

-   **[The Lady of Marmaros](lady-of-marmaros.md)**

    ---

    The marble island city of mages, scholars and ambitious power struggles.

-   **[The Lord of Carbohyrr](lord-of-carbohyrr.md)**

    ---

    The mountain fortress of smiths and miners, industrial heart of Galluvinchia.

-   **[Lorda Gorda](lorda-gorda.md)**

    ---

    The felinfolk fortress island, lit by pink crystal light, proud and independent.

</div>
''')

# ── Index ES ──
w(B + '/index.es.md', '''---
description: Las grandes ciudades de Galluvinchia, An\'Ramoda, la Dama de Mármaros, el Señor de Carbohyrr y Lorda Gorda, sus gentes, poder e historia.
---

# Ciudades de Galluvinchia

Las ciudades de Galluvinchia son más que centros de comercio, son declaraciones. Cada muro, cada puerta, cada torre declara quién la construyó, quién la gobierna ahora y a qué dioses sirve.

<div class="grid cards" markdown>

-   **[An\'Ramoda](anramoda.md)**

    ---

    La ciudad amurallada del norte, sede de Aremedia y hogar del mayor ejército de Galluvinchia.

-   **[La Dama de Mármaros](lady-of-marmaros.md)**

    ---

    La ciudad-isla de mármol de magos, eruditos y ambiciosas luchas de poder.

-   **[El Señor de Carbohyrr](lord-of-carbohyrr.md)**

    ---

    La fortaleza montañosa de herreros y mineros, corazón industrial de Galluvinchia.

-   **[Lorda Gorda](lorda-gorda.md)**

    ---

    La fortaleza-isla de los felicios, iluminada por la luz de los cristales rosas, orgullosa e independiente.

</div>
''')

# ── An'Ramoda ──
w(B + '/anramoda.md', page(
    "An'Ramoda",
    "An'Ramoda, the great walled northern city, seat of the goddess Aremedia and home of Galluvinchia's most powerful army.",
    box('artwork-colosseum.webp', "An'Ramoda", "The Walled City of the North · Seat of Aremedia",
        [('Ruler', 'Aremedia (divine) · Three Consuls'), ('Location', 'Northern Galluvinchia'),
         ('Army', '7,000+ trained fighters'), ('Patron', 'Aremedia')]),
    '''Built as a sanctuary by Salgu, the King of the Beasts, An\'Ramoda has stood as the greatest fortress city in Galluvinchia since the Age of the Giants. Its enormous walls enclose a thriving population whose love for the fight and the pursuit of a strong body is second to none.

The people worship Aremedia above all others. Many citizens dream of competing and winning in the **Colosseum**, where gladiatorial matches crown champions yearly. The current champion, **[Armada](../../characters/armada.md)**, a towering black minotaur, has held the title for more than ten years. None has ever forced him to draw his sword.

## Power Structure

| Authority | Description |
|-----------|-------------|
| **Aremedia** | Ultimate power by divine right. Her will is law |
| **Three Consuls** | [Lewis Pendeltag](../../characters/lewis-pendeltag.md) (wisdom), [Armada](../../characters/armada.md) (valor), [Martin Goldberg](../../characters/martin-goldberg.md) (commerce) |
| **Six Senators** | Chosen by the consuls with Aremedia\'s approval |

## The Army

Made up of more than 7,000 trained fighters, the An\'Ramodian army is second to none. The **Keepers of Galluvinchia** patrol trade routes across the continent, protecting merchant caravans and keeping order.

## Surrounding Towns

- **Picarosh**, the gastronomy village
- **Craikov**, the port of An\'Ramoda
- **Saint Erensburg**, famous for its underground gardens
- **Tanishia**, village of vineyards producing Galluvinchia\'s finest wines
- **Gretscznievlycov**, golden hills and windmills

![The Colosseum of An\'Ramoda, arena of champions](../../img/artwork-colosseum.webp){ .wiki-full }

!!! tip "Rumour"
    Fighters defeated at the Colosseum are yet to be seen again. Their families accept that whatever happens is glory or death, but not everyone is so certain.
'''))

w(B + '/anramoda.es.md', page(
    "An'Ramoda",
    "An'Ramoda, la gran ciudad amurallada del norte, sede de la diosa Aremedia y hogar del ejército más poderoso de Galluvinchia.",
    box('artwork-colosseum.webp', "An'Ramoda", "La Ciudad Amurallada del Norte · Sede de Aremedia",
        [('Gobernante', 'Aremedia (divina) · Tres Cónsules'), ('Ubicación', 'Norte de Galluvinchia'),
         ('Ejército', 'Más de 7.000 luchadores entrenados'), ('Patrón', 'Aremedia')]),
    '''Construida como santuario por Salgu, el Rey de las Bestias, An\'Ramoda ha permanecido como la mayor ciudad fortaleza de Galluvinchia desde la Era de los Gigantes. Sus enormes murallas encierran a una próspera población cuyo amor por la lucha no tiene igual.

El pueblo venera a Aremedia por encima de todos los demás. Muchos ciudadanos sueñan con competir y ganar en el **Coliseo**, donde los combates gladiatorios coronan campeones anualmente. El campeón actual, **[Armada](../../characters/armada.md)**, un enorme minotauro negro, lleva más de diez años con el título.

## Estructura de Poder

| Autoridad | Descripción |
|-----------|-------------|
| **Aremedia** | Poder supremo por derecho divino. Su voluntad es ley |
| **Tres Cónsules** | [Lewis Pendeltag](../../characters/lewis-pendeltag.md) (sabiduría), [Armada](../../characters/armada.md) (valor), [Martin Goldberg](../../characters/martin-goldberg.md) (comercio) |
| **Seis Senadores** | Elegidos por los cónsules con aprobación de Aremedia |

## El Ejército

Con más de 7.000 luchadores entrenados, el ejército de An\'Ramoda no tiene igual. Los **Guardianes de Galluvinchia** patrullan las rutas comerciales de todo el continente.

## Pueblos Circundantes

- **Picarosh**, el pueblo de la gastronomía
- **Craikov**, el puerto de An\'Ramoda
- **Saint Erensburg**, famoso por sus jardines subterráneos
- **Tanishia**, pueblo de viñedos productores de los mejores vinos de Galluvinchia
- **Gretscznievlycov**, colinas doradas y molinos de viento

!!! tip "Rumor"
    Los luchadores derrotados en el Coliseo aún no han vuelto a ser vistos.
'''))

# ── Lady of Marmaros ──
w(B + '/lady-of-marmaros.md', page(
    'The Lady of Marmaros',
    'The Lady of Marmaros, the marble island city of mages and scholars, home of the Academy of Magic Wonders.',
    box('character-monica-mars.webp', 'Lady of Marmaros', 'The Marble City · Home of the Academy of Magic Wonders',
        [('Ruler', 'King Fernando Oldreekia · Academy · Guild'), ('Location', 'Island, Central Galluvinchia'),
         ('Known for', 'Magic, scholarship, vanity'), ('Patron', 'None official')]),
    '''The Lady of Marmaros was sculpted from a great marble mountain, born from the impact of the asteroid that ended the Age of Primordials. The city is immensely proud of its mages and scholars, housing the most prestigious arcane institution in Galluvinchia: the **Academy of Magic Wonders**, presided over by **[Magister Monica Mars](../../characters/monica-mars.md)**.

Marmarians are known for their vanity and pride in appearances. The city is full of hair salons, massage parlors, and a hospital catering to its citizens\' insecurities. It is also home to **Old Rick\'s Herald**, Galluvinchia\'s foremost news company.

## Power Structure

| Authority | Description |
|-----------|-------------|
| **[King Fernando Oldreekia](../../characters/fernando-oldreekia.md)** | Royal by blood, owner of the Royal Guards, land, and marble mines |
| **The Academy of Magic Wonders** | Led by [Magister Monica Mars](../../characters/monica-mars.md); surging influence through branded products |
| **The Guild** | Merchant Guild controlling trade registries throughout Galluvinchia |
| **The Fist** | A shadow network whose leader is known to no one |

![Magistrate Monica Mars, head of the Academy of Magic Wonders](../../img/character-monica-mars.webp){ .wiki-full }

!!! tip "Rumour"
    The miners of Marmaros have been growing progressively sick. From deep within the marble veins, whispers of something darker have been heard.
'''))

w(B + '/lady-of-marmaros.es.md', page(
    'La Dama de Mármaros',
    'La Dama de Mármaros, la ciudad-isla de mármol de magos y eruditos, sede de la Academia de Magias Maravillosas.',
    box('character-monica-mars.webp', 'Dama de Mármaros', 'La Ciudad de Mármol · Sede de la Academia de Magias Maravillosas',
        [('Gobernante', 'Rey Fernando Oldreekia · Academia · Gremio'), ('Ubicación', 'Isla, Galluvinchia Central'),
         ('Conocida por', 'Magia, erudición, vanidad'), ('Patrón', 'Ninguno oficial')]),
    '''La Dama de Mármaros fue esculpida de una gran montaña de mármol, formada por el impacto del asteroide que puso fin a la Era de los Primordiales. La ciudad es inmensamente orgullosa de sus magos y eruditos, albergando la institución arcana más prestigiosa de Galluvinchia: la **Academia de Magias Maravillosas**, presidida por **[la Magistrada Monica Mars](../../characters/monica-mars.md)**.

Los marmarianos son conocidos por su vanidad y orgullo en las apariencias.

## Estructura de Poder

| Autoridad | Descripción |
|-----------|-------------|
| **[Rey Fernando Oldreekia](../../characters/fernando-oldreekia.md)** | Real por sangre, propietario de la Guardia Real, la tierra y las minas de mármol |
| **Academia de Magias Maravillosas** | Dirigida por [la Magistrada Monica Mars](../../characters/monica-mars.md) |
| **El Gremio** | Gremio de mercaderes que controla los registros comerciales de toda Galluvinchia |
| **El Puño** | Una red de sombras cuyo líder nadie conoce |

!!! tip "Rumor"
    Los mineros de Mármaros están enfermando progresivamente. Desde las profundidades de las venas de mármol, se han escuchado susurros de algo más oscuro.
'''))

# ── Lord of Carbohyrr ──
w(B + '/lord-of-carbohyrr.md', page(
    'The Lord of Carbohyrr',
    'The Lord of Carbohyrr, the mountain fortress city of smiths and miners, industrial heart of Galluvinchia.',
    box('character-sara-bastu.webp', 'Lord of Carbohyrr', 'The Black City · Mountain Fortress of the Forge',
        [('Ruler', 'The Duke (elected) · Battlemages'), ('Location', 'Mountain, Eastern Galluvinchia'),
         ('Known for', 'Forges, hot springs, craftsmanship'), ('Patron', 'Moroes')]),
    '''Hidden inside a mountain, the Lord of Carbohyrr is a city of long chimneys, the stench of embers, and unparalleled craftsmanship. Famous for its hot springs and deep mines, it is the industrial heart of Galluvinchia, the place where the finest weapons and armor are forged.

Every person who visits is required to carry a **copper pass** crafted by the Battlemages, used to track tax contributions and grant access to the city\'s central lifts.

## Power Structure

| Authority | Description |
|-----------|-------------|
| **The Duke** | Elected by taxpayer vote every two years |
| **The Battlemages** | Trained magic police who maintain order and keep tax accounts |

## The Depths

The economy rests almost entirely on its forges. An\'Ramoda is the main buyer of weapons and armor, and tensions between the working class and the ruling structure are beginning to boil.

Space inside the mountain is precious. Citizens have learned to improvise: vertical gardens, communal public baths, and the **Proper Growth Institution**, where children are sent at age six and guided toward a career by age nine.

!!! tip "Rumour"
    Prices in the Lord keep rising, and opportunities for young Carbohyrrans are shrinking to the mine and the forge. Something has to give.
'''))

w(B + '/lord-of-carbohyrr.es.md', page(
    'El Señor de Carbohyrr',
    'El Señor de Carbohyrr, la ciudad fortaleza montañosa de herreros y mineros, corazón industrial de Galluvinchia.',
    box('character-sara-bastu.webp', 'Señor de Carbohyrr', 'La Ciudad Negra · Fortaleza Montañosa de la Fragua',
        [('Gobernante', 'El Duque (electo) · Mago-Guerreros'), ('Ubicación', 'Montaña, Este de Galluvinchia'),
         ('Conocido por', 'Fraguas, aguas termales, artesanía'), ('Patrón', 'Moroes')]),
    '''Escondido dentro de una montaña, el Señor de Carbohyrr es una ciudad de largas chimeneas, el olor a brasas y artesanía sin igual. Famoso por sus aguas termales y sus profundas minas, es el corazón industrial de Galluvinchia, el lugar donde se forjan las mejores armas y armaduras.

Cada persona que visita la ciudad debe llevar un **pase de cobre** fabricado por los Mago-Guerreros, usado para rastrear las contribuciones fiscales y conceder acceso a los elevadores centrales.

## Estructura de Poder

| Autoridad | Descripción |
|-----------|-------------|
| **El Duque** | Elegido por voto de contribuyentes cada dos años |
| **Los Mago-Guerreros** | Policía mágica entrenada que mantiene el orden |

!!! tip "Rumor"
    Los precios en el Señor siguen subiendo, y las oportunidades para los jóvenes carbohyrrianos se reducen a la mina y la fragua. Algo tiene que ceder.
'''))

# ── Lorda Gorda ──
w(B + '/lorda-gorda.md', page(
    'Lorda Gorda',
    'Lorda Gorda, the felinfolk fortress island lit by pink crystal light, proud and independent from the Keepers of Galluvinchia.',
    box('character-maneless-king.webp', 'Lorda Gorda', 'The Fortress Island · Stronghold of the Felinfolk',
        [('Ruler', 'The Maneless King · Assembly'), ('Location', 'Island, Eastern Galluvinchia'),
         ('Known for', 'Pink crystals, shipwrighting, felinfolk'), ('Patron', 'The Light')]),
    '''Far from the patrol zones of the Keepers of Galluvinchia lies Lorda Gorda, the proudest city in the East. Inhabited mainly by hard-working felinfolk, it shuns the blessings of the gods and prays instead to the Light.

The city is illuminated at night by **pink crystals** mined deep underground. These crystals are the cornerstone of Lorda Gorda\'s culture, powering their streets, propelling their ships, and holding something far more personal inside them.

## Power Structure

Governed by an assembly where five votes are needed to pass any decision:

| Group | Votes |
|-------|-------|
| **[The Maneless King](../../characters/maneless-king.md)** | 4 votes |
| **Order and Defence** | 1 vote |
| **The Shipwrights** | 1 vote |
| **Union of the Fishermen** | 1 vote |
| **Crystal Miners** | 1 vote |
| **Popular Vote** | 2 votes |

## The Pink Crystals

At age eighteen, every citizen jumps into the Fountain of Renewal, a ritual that, upon their death, will bind their lingering soul-energy to the pink crystals mined from deep below. The crystals glow with this energy before the souls continue to the Renewal.

## Shipwrighting

The shipwrights of Lorda Gorda are legendary. Living surrounded by treacherous waves and sea monsters, their technology has evolved to levels that leave mainland harbormasters speechless.

## The Library of Eternal Enlightenment

Close to the castle of the [Maneless King](../../characters/maneless-king.md) lies a library housing hundreds of texts, some over 500 years old and written in unknown languages, with a notable section dedicated to medical research.
'''))

w(B + '/lorda-gorda.es.md', page(
    'Lorda Gorda',
    'Lorda Gorda, la fortaleza-isla de los felicios iluminada por cristales rosas, orgullosa e independiente de los Guardianes de Galluvinchia.',
    box('character-maneless-king.webp', 'Lorda Gorda', 'La Fortaleza-Isla · Bastión de los Felicios',
        [('Gobernante', 'El Rey sin Melena · Asamblea'), ('Ubicación', 'Isla, Este de Galluvinchia'),
         ('Conocida por', 'Cristales rosas, construcción naval, felicios'), ('Patrón', 'La Luz')]),
    '''Lejos de las zonas de patrulla de los Guardianes de Galluvinchia se encuentra Lorda Gorda, la ciudad más orgullosa del Este. Habitada principalmente por felicios trabajadores, rechaza las bendiciones de los dioses y reza en cambio a la Luz.

La ciudad está iluminada por la noche por **cristales rosas** extraídos de las profundidades de la tierra.

## Estructura de Poder

Gobernada por una asamblea donde se necesitan cinco votos para tomar cualquier decisión:

| Grupo | Votos |
|-------|-------|
| **[El Rey sin Melena](../../characters/maneless-king.md)** | 4 votos |
| **Orden y Defensa** | 1 voto |
| **Los Constructores de Barcos** | 1 voto |
| **Unión de Pescadores** | 1 voto |
| **Mineros de Cristal** | 1 voto |
| **Voto Popular** | 2 votos |

## Los Cristales Rosas

A los dieciocho años, cada ciudadano salta a la Fuente del Rencarnatorno, un ritual que, al morir, vinculará su energía anímica a los cristales rosas extraídos de las profundidades. Los cristales brillan con esta energía antes de que las almas continúen hacia el Resurgimiento.

## La Biblioteca de la Iluminación Eterna

Cerca del castillo del [Rey sin Melena](../../characters/maneless-king.md) hay una biblioteca con cientos de textos, algunos de más de 500 años, escritos en lenguas desconocidas, con una notable sección dedicada a la investigación médica.
'''))

print("Done cities.")
