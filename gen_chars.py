#!/usr/bin/env python3
import os

B = "wiki-docs/characters"
os.makedirs(B, exist_ok=True)

def w(p, c):
    with open(p, "w", encoding="utf-8") as f:
        f.write(c)

def box(img_file, name, ep, fields):
    r = '<div class="wiki-infobox" markdown>\n\n'
    if img_file:
        r += '![' + name + '](../img/' + img_file + '){ .wiki-infobox-img }\n\n'
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
description: The notable characters of Galluvinchia, heroes, villains and legends whose ambitions shape the fate of the world.
---

# Characters of Galluvinchia

Galluvinchia is shaped as much by individuals as by gods or geography. This is a record of those who left a mark.

<div class="grid cards" markdown>

-   **[Armada](armada.md)**

    ---

    Undefeated Colosseum champion for over ten years. Brave Consul of An\'Ramoda.

-   **[The Maneless King](maneless-king.md)**

    ---

    Beloved ruler of Lorda Gorda, holder of four assembly votes and the genuine love of his people.

-   **[Monica Mars](monica-mars.md)**

    ---

    Head of the Academy of Magic Wonders. One of the most powerful figures in Marmaros.

-   **[Raquel Crepusculiento](raquel.md)**

    ---

    The last inventor of a forgotten Carbohyrr academy, whose blueprints survive in hidden places.

-   **[Archlich Kogarashi](kogarashi.md)**

    ---

    The necromancer who waged the Arcane War against the gods. Body never found.

-   **[Agustin of Carzagus](agustin.md)**

    ---

    A baker famous for extraordinary croissants and an unexplained silver pendant.

-   **[Silvino](silvino.md)**

    ---

    High Paladin of Panos, recovering relics his absentminded god has lost.

-   **[Lewis Pendeltag](lewis-pendeltag.md)**

    ---

    Wise Consul of An\'Ramoda, collector of magic items and historian of Galluvinchia.

-   **[Martin Goldberg](martin-goldberg.md)**

    ---

    Mighty Consul of An\'Ramoda and owner of the city\'s gold mine.

-   **[Fernando Oldreekia](fernando-oldreekia.md)**

    ---

    King of the Lady of Marmaros, royal by blood, ruling alongside the Academy and the Guild.

-   **[Merrion Meyer](merrion-meyer.md)**

    ---

    Regent of the Academy of Magic Waves and Dreams in Doormi.

-   **[Salgu](salgu.md)**

    ---

    King of the Beasts in the First Age, founder of An\'Ramoda.

-   **[Lumin Oldreekia](lumin-oldreekia.md)**

    ---

    Legendary leokin, greatest felinfolk hero and founder of Lorda Gorda.

-   **[Alice Rockwool](alice-rockwool.md)**

    ---

    Adventurer and legend of the timeless library beneath Lakobordo.

</div>
''')

# ── Index ES ──
w(B + '/index.es.md', '''---
description: Los personajes notables de Galluvinchia, héroes, villanos y leyendas cuyas ambiciones moldean el destino del mundo.
---

# Personajes de Galluvinchia

Galluvinchia está moldeada tanto por individuos como por dioses o geografía. Este es el registro de quienes dejaron huella.

<div class="grid cards" markdown>

-   **[Armada](armada.md)**

    ---

    Campeón invicto del Coliseo durante más de diez años. Cónsul Valiente de An\'Ramoda.

-   **[El Rey sin Melena](maneless-king.md)**

    ---

    Amado gobernante de Lorda Gorda, con cuatro votos en la asamblea y el amor genuino de su pueblo.

-   **[Monica Mars](monica-mars.md)**

    ---

    Directora de la Academia de Magias Maravillosas. Una de las personas más poderosas de Mármaros.

-   **[Raquel Crepusculiento](raquel.md)**

    ---

    La última inventora de una academia olvidada de Carbohyrr, cuyos planos sobreviven en lugares ocultos.

-   **[Archliche Kogarashi](kogarashi.md)**

    ---

    El nigromante que libró la Guerra Arcana contra los dioses. Su cuerpo nunca fue encontrado.

-   **[Agustín de Carzagus](agustin.md)**

    ---

    Un panadero famoso por sus cruasanes y un colgante de plata inexplicable.

-   **[Silvino](silvino.md)**

    ---

    Alto Paladín de Panos, recuperando reliquias que su distraído dios ha perdido.

-   **[Lewis Pendeltag](lewis-pendeltag.md)**

    ---

    Cónsul Sabio de An\'Ramoda, coleccionista de objetos mágicos e historiador de Galluvinchia.

-   **[Martin Goldberg](martin-goldberg.md)**

    ---

    Cónsul Poderoso de An\'Ramoda y propietario de la mina de oro de la ciudad.

-   **[Fernando Oldreekia](fernando-oldreekia.md)**

    ---

    Rey de la Dama de Mármaros, de sangre real, gobernando junto a la Academia y el Gremio.

-   **[Merrion Meyer](merrion-meyer.md)**

    ---

    Regente de la Academia de las Ondas Étereas y los Sueños en Doormi.

-   **[Salgu](salgu.md)**

    ---

    Rey de las Bestias en la Primera Era, fundador de An\'Ramoda.

-   **[Lumin Oldreekia](lumin-oldreekia.md)**

    ---

    El legendario leokin, mayor héroe felicios y fundador de Lorda Gorda.

-   **[Alice Rockwool](alice-rockwool.md)**

    ---

    Aventurera y leyenda de la biblioteca atemporal bajo Lakobordo.

</div>
''')

# ── Individual character pages ──

w(B + '/armada.md', page(
    'Zack "The Blade" Armada',
    'Armada, undefeated Colosseum champion for over ten years and Brave Consul of An\'Ramoda.',
    box('artwork-minotaur.webp', 'Armada', 'Champion of the Colosseum · Brave Consul of An\'Ramoda',
        [('Role', 'Brave Consul of An\'Ramoda · Colosseum Champion'), ('Location', "An'Ramoda"), ('Status', 'Active')]),
    '''A towering black minotaur with sharp horns and a massive blade worn across his back, a blade no one has ever seen him draw. Reigning Colosseum champion for more than ten years, and one of the three consuls of An\'Ramoda, chosen personally by the goddess Aremedia.

## The Colosseum

Challengers come from across Galluvinchia seeking glory. None has forced him to draw his sword. Whether this is patience, mercy, or something else entirely is a matter of ongoing debate.

## Politics

As Brave Consul, Armada represents martial valor in An\'Ramoda\'s governance. Alongside Lewis Pendeltag and Martin Goldberg, he forms the triumvirate that implements Aremedia\'s will.

!!! tip "Rumour"
    Fighters defeated at the Colosseum are yet to be seen again. Their families accept that whatever happens is glory or death, but not everyone is so certain.
'''))

w(B + '/armada.es.md', page(
    'Zack "La Espada" Armada',
    'Armada, campeón invicto del Coliseo durante más de diez años y Cónsul Valiente de An\'Ramoda.',
    box('artwork-minotaur.webp', 'Armada', 'Campeón del Coliseo · Cónsul Valiente de An\'Ramoda',
        [('Rol', 'Cónsul Valiente de An\'Ramoda · Campeón del Coliseo'), ('Ubicación', "An'Ramoda"), ('Estado', 'Activo')]),
    '''Un enorme minotauro negro con cuernos afilados y una enorme espada cargada a la espalda, una espada que nadie le ha visto desenfundar jamás. Campeón reinante del Coliseo durante más de diez años, y uno de los tres cónsules de An\'Ramoda, elegido personalmente por la diosa Aremedia.

## El Coliseo

Los aspirantes vienen de toda Galluvinchia en busca de gloria. Ninguno le ha obligado a desenfundar su espada.

## Política

Como Cónsul Valiente, Armada representa el valor marcial en el gobierno de An\'Ramoda. Junto a Lewis Pendeltag y Martin Goldberg, forma el triunvirato que implementa la voluntad de Aremedia.

!!! tip "Rumor"
    Los luchadores derrotados en el Coliseo aún no han vuelto a ser vistos. Sus familias aceptan que lo que ocurra es gloria o muerte, pero no todos están tan seguros.
'''))

w(B + '/maneless-king.md', page(
    'The Maneless King',
    'The Maneless King, beloved ruler of Lorda Gorda who holds four assembly votes and the genuine love of his people.',
    box('character-maneless-king.webp', 'The Maneless King', 'Beloved Ruler of Lorda Gorda',
        [('Role', 'King of Lorda Gorda'), ('Location', 'Lorda Gorda'), ('Assembly Votes', '4 of 10'), ('Status', 'Active')]),
    '''The Maneless King has always been a kind ruler who looks forward to his people\'s wellbeing. In a world of ambitious rulers, the genuine love of an entire city is rarer than it sounds.

## Governance

Lorda Gorda is governed by an assembly where five votes are needed to pass any decision. The Maneless King holds four votes, giving him significant but not unchecked authority. He has consistently used this power in service of the people.

## The Pink Crystals

The crystals that light Lorda Gorda\'s streets hold the soul-energy of its citizens. The Maneless King participates in this tradition like every citizen, having jumped into the Fountain of Renewal at eighteen.
'''))

w(B + '/maneless-king.es.md', page(
    'El Rey sin Melena',
    'El Rey sin Melena, amado gobernante de Lorda Gorda con cuatro votos en la asamblea y el amor genuino de su pueblo.',
    box('character-maneless-king.webp', 'El Rey sin Melena', 'Amado Gobernante de Lorda Gorda',
        [('Rol', 'Rey de Lorda Gorda'), ('Ubicación', 'Lorda Gorda'), ('Votos en Asamblea', '4 de 10'), ('Estado', 'Activo')]),
    '''El Rey sin Melena siempre ha sido un gobernante amable que vela por el bienestar de su pueblo. En un mundo de gobernantes ambiciosos, el amor genuino de una ciudad entera es más raro de lo que parece.

## Gobierno

Lorda Gorda está gobernada por una asamblea donde se necesitan cinco votos para tomar cualquier decisión. El Rey sin Melena tiene cuatro votos, lo que le da una autoridad significativa pero no absoluta.

## Los Cristales Rosas

Los cristales que iluminan las calles de Lorda Gorda contienen la energía anímica de sus ciudadanos. El Rey sin Melena participa en esta tradición como todos los demás, habiendo saltado a la Fuente del Rencarnatorno a los dieciocho años.
'''))

w(B + '/monica-mars.md', page(
    'Magister Monica Mars',
    'Magister Monica Mars, head of the Academy of Magic Wonders and one of the most powerful figures in the Lady of Marmaros.',
    box('character-monica-mars.webp', 'Monica Mars', 'Head of the Academy of Magic Wonders',
        [('Role', 'Head of the Academy of Magic Wonders'), ('Location', 'Lady of Marmaros'), ('Status', 'Active')]),
    '''One of the most skilled and intelligent mages in Galluvinchia. Under her leadership, the Academy of Magic Wonders has grown from an institution into a continent-wide brand, its potions, lotions, and magical garments seen in every city.

## The Academy

The most exclusive scholarship in Galluvinchia. Wizard apprentices here become multidisciplinary mages, studying all schools of magic. The Academy\'s branded products generate enormous political and commercial influence.

Whether this makes her a visionary or simply very good at commerce depends on who you ask.

!!! tip "Rumour"
    The miners of Marmaros have been growing progressively sick. From deep within the marble veins, whispers of something darker have been heard.
'''))

w(B + '/monica-mars.es.md', page(
    'Magistrada Monica Mars',
    'Magistrada Monica Mars, directora de la Academia de Magias Maravillosas y una de las personas más poderosas de la Dama de Mármaros.',
    box('character-monica-mars.webp', 'Monica Mars', 'Directora de la Academia de Magias Maravillosas',
        [('Rol', 'Directora de la Academia de Magias Maravillosas'), ('Ubicación', 'Dama de Mármaros'), ('Estado', 'Activa')]),
    '''Una de las magas más hábiles e inteligentes de Galluvinchia. Bajo su liderazgo, la Academia de Magias Maravillosas ha crecido hasta convertirse en una marca continental, con pociones, lociones y prendas mágicas en todas las ciudades.

## La Academia

La beca más exclusiva de Galluvinchia. Los aprendices formados aquí se convierten en magos multidisciplinares.

!!! tip "Rumor"
    Los mineros de Mármaros están enfermando progresivamente. Desde las profundidades de las venas de mármol, se han escuchado susurros de algo más oscuro.
'''))

w(B + '/raquel.md', page(
    'Raquel Crepusculiento',
    'Raquel Crepusculiento, last known inventor of a forgotten academy connected to the Lord of Carbohyrr, whose blueprints survive in hidden places.',
    box('character-raquel.webp', 'Raquel Crepusculiento', 'The Last Inventor · Lost Academy of Carbohyrr',
        [('Role', 'Inventor'), ('Location', 'Lord of Carbohyrr (historical)'), ('Status', 'Unknown')]),
    '''The last known inventor of a long-forgotten academy connected to the Lord of Carbohyrr. Her blueprints and notes survive in hidden places, detailing designs and knowledge that the current age has yet to match.

## Legacy

Her most notable creation is spoken of in legends among the smiths and battlemages of Carbohyrr, but the truth of it remains buried. Scholars who have found fragments of her notes speak of machines that should not exist and formulas that defy current understanding of the Ripple.
'''))

w(B + '/raquel.es.md', page(
    'Raquel Crepusculiento',
    'Raquel Crepusculiento, la última inventora conocida de una academia olvidada vinculada al Señor de Carbohyrr.',
    box('character-raquel.webp', 'Raquel Crepusculiento', 'La Última Inventora · Academia Perdida de Carbohyrr',
        [('Rol', 'Inventora'), ('Ubicación', 'Señor de Carbohyrr (histórica)'), ('Estado', 'Desconocido')]),
    '''La última inventora conocida de una academia olvidada vinculada al Señor de Carbohyrr. Sus planos y notas sobreviven en lugares ocultos, con diseños y conocimientos que la era actual aún no ha podido igualar.

## Legado

Su creación más notable es objeto de leyendas entre los herreros y Mago-Guerreros de Carbohyrr, pero la verdad permanece enterrada. Los eruditos que han encontrado fragmentos de sus notas hablan de máquinas que no deberían existir.
'''))

w(B + '/kogarashi.md', page(
    'Archlich Kogarashi',
    'Archlich Kogarashi, the archmage who waged the Arcane War against the gods of Galluvinchia. His body was never found.',
    box('character-kogarashi.webp', 'Archlich Kogarashi', 'The Necromancer · Enemy of the Gods',
        [('Role', 'Archmage · Necromancer'), ('Last known location', 'Ancho Groncho'), ('Status', 'Unknown — body never found'), ('Conflict', 'Arcane War')]),
    '''Once an archmage of unparalleled fury and ambition, Kogarashi rose after the gods\' ascension and denounced them as usurpers, ignorant of the true arcane arts. He forged an unholy pact with a conclave of powerful mages and waged the **Arcane War** against the new divine order.

## The Arcane War

The war shook Galluvinchia to its core. Its final clash erupted in the forsaken abyss of **Ancho Groncho**, a labyrinth Kogarashi himself crafted. [Panos](../gods/panos.md) triumphed, yet Kogarashi\'s body was never found.

## Present Day

His necromantic legacy continues to unsettle the living. The undead armies that have raged since the end of the Arcane War are believed to be tied to his lingering will.

!!! warning "Danger"
    The Third Wars of the Skeleton ended three years ago with a successful incursion into Ancho Groncho. But the necromancer\'s body was never found, and the undead continue to stir.
'''))

w(B + '/kogarashi.es.md', page(
    'Archliche Kogarashi',
    'Archliche Kogarashi, el archimago que libró la Guerra Arcana contra los dioses de Galluvinchia. Su cuerpo nunca fue encontrado.',
    box('character-kogarashi.webp', 'Archliche Kogarashi', 'El Nigromante · Enemigo de los Dioses',
        [('Rol', 'Archimago · Nigromante'), ('Última ubicación conocida', 'Ancho Groncho'), ('Estado', 'Desconocido — cuerpo nunca encontrado'), ('Conflicto', 'Guerra Arcana')]),
    '''En su día un archimago de furia y ambición sin par, Kogarashi emergió tras el ascenso de los dioses y los denunció como usurpadores. Forjó un pacto prohibido con un cónclave de poderosos magos y libró la **Guerra Arcana** contra el nuevo orden divino.

## La Guerra Arcana

La guerra sacudió Galluvinchia. Su enfrentamiento final estalló en **Ancho Groncho**, un laberinto que el propio Kogarashi había creado. [Panos](../gods/panos.md) triunfó, pero el cuerpo de Kogarashi nunca fue encontrado.

!!! warning "Peligro"
    Las Terceras Guerras de los Esqueletos terminaron hace tres años. Pero el cuerpo del nigromante nunca fue encontrado, y los no-muertos siguen inquietos.
'''))

w(B + '/agustin.md', page(
    'Agustin of Carzagus',
    'Agustin of Carzagus, a baker in Lakobordo famous for extraordinary croissants and a mysterious silver pendant no one can explain.',
    box('artwork-virtuous.webp', 'Agustin of Carzagus', 'Baker · Lakobordo',
        [('Role', 'Baker'), ('Location', 'Lakobordo'), ('Status', 'Active')]),
    '''Famous throughout Lakobordo for his extraordinary croissants. Also, for an old silver pendant shaped like a fist that he carries everywhere, a pendant he cannot explain, and whose origin even he does not know.

He is a kind, unassuming man who seems entirely unlikely to be important.

## The Pendant

The pendant is silver, old, and shaped like a closed fist. It shows no maker\'s mark that any smith in Lakobordo has been able to identify. Those with knowledge of rare magical artifacts have taken an unusual interest in it.
'''))

w(B + '/agustin.es.md', page(
    'Agustín de Carzagus',
    'Agustín de Carzagus, un panadero de Lakobordo famoso por sus extraordinarios cruasanes y un misterioso colgante de plata que nadie puede explicar.',
    box('artwork-virtuous.webp', 'Agustín de Carzagus', 'Panadero · Lakobordo',
        [('Rol', 'Panadero'), ('Ubicación', 'Lakobordo'), ('Estado', 'Activo')]),
    '''Famoso en todo Lakobordo por sus extraordinarios cruasanes. También, por un viejo colgante de plata con forma de puño que lleva siempre consigo, un colgante que no puede explicar, y cuyo origen ni él mismo conoce.

Es un hombre amable y discreto que no parece tener ninguna importancia especial.

## El Colgante

El colgante es de plata, antiguo, con forma de puño cerrado. No muestra ninguna marca de fabricante que ningún herrero de Lakobordo haya podido identificar.
'''))

w(B + '/silvino.md', page(
    'Silvino',
    'Silvino, High Paladin of Panos, on a quest to recover the relics his absentminded god has lost across Galluvinchia.',
    box('artwork-panos-cleric.webp', 'Silvino', 'High Paladin of Panos',
        [('Role', 'High Paladin of Panos'), ('Location', 'Wandering'), ('Status', 'Active · On a quest')]),
    '''One of Panos\'s most devoted champions, Silvino serves the god of magic and order with absolute dedication. His current quest involves the recovery of relics lost by his absentminded deity, objects that Panos believes are important but can no longer remember exactly why.

## The Quest

[Panos](../gods/panos.md) is known for his capricious nature and faltering memory. Relics of divine significance have been misplaced across Galluvinchia over the centuries. Silvino travels the land recovering them, believing each one restored strengthens Panos\'s divine memory.
'''))

w(B + '/silvino.es.md', page(
    'Silvino',
    'Silvino, Alto Paladín de Panos, en busca de las reliquias que su distraído dios ha perdido por toda Galluvinchia.',
    box('artwork-panos-cleric.webp', 'Silvino', 'Alto Paladín de Panos',
        [('Rol', 'Alto Paladín de Panos'), ('Ubicación', 'Itinerante'), ('Estado', 'Activo · En misión')]),
    '''Uno de los campeones más devotos de Panos, Silvino sirve al dios de la magia y el orden con dedicación absoluta. Su misión actual consiste en recuperar reliquias perdidas por su distraído deidad, objetos que [Panos](../gods/panos.md) cree que son importantes pero que ya no recuerda exactamente por qué.
'''))

w(B + '/lewis-pendeltag.md', page(
    'Lewis "The Collector" Pendeltag',
    'Lewis Pendeltag, Wise Consul of An\'Ramoda, known for his vast collection of magic items and encyclopedic knowledge of Galluvinchia.',
    box(None, 'Lewis Pendeltag', 'Wise Consul of An\'Ramoda',
        [('Role', 'Wise Consul of An\'Ramoda'), ('Location', "An'Ramoda"), ('Status', 'Active')]),
    '''One of the three consuls chosen by Aremedia herself. Known throughout Galluvinchia for his vast collection of magic items and encyclopedic knowledge of the land\'s history.

As Wise Consul, Lewis serves as historian and strategist of An\'Ramoda\'s government. He also manages the city\'s tax collection, a combination that makes him one of the most influential people in Galluvinchia. His title "The Collector" refers as much to his political leverage as to his famous artifact collection.
'''))

w(B + '/lewis-pendeltag.es.md', page(
    'Lewis "El Coleccionista" Pendeltag',
    'Lewis Pendeltag, Cónsul Sabio de An\'Ramoda, conocido por su vasta colección de objetos mágicos y su conocimiento enciclopédico de Galluvinchia.',
    box(None, 'Lewis Pendeltag', 'Cónsul Sabio de An\'Ramoda',
        [('Rol', 'Cónsul Sabio de An\'Ramoda'), ('Ubicación', "An'Ramoda"), ('Estado', 'Activo')]),
    '''Uno de los tres cónsules elegidos por la propia Aremedia. Conocido en toda Galluvinchia por su vasta colección de objetos mágicos y su conocimiento enciclopédico de la historia de la tierra.

Como Cónsul Sabio, Lewis actúa como historiador y estratega del gobierno de An\'Ramoda. También gestiona la recaudación de impuestos, lo que le convierte en una de las personas más influyentes de Galluvinchia.
'''))

w(B + '/martin-goldberg.md', page(
    'Martin "The Coin" Goldberg',
    'Martin Goldberg, Mighty Consul of An\'Ramoda and owner of the city\'s gold mine.',
    box(None, 'Martin Goldberg', 'Mighty Consul of An\'Ramoda',
        [('Role', 'Mighty Consul of An\'Ramoda'), ('Location', "An'Ramoda"), ('Status', 'Active')]),
    '''Owner of An\'Ramoda\'s gold mine, and the third of the goddess\'s chosen consuls. Commerce and coin are his domain, and in a city where the mine fuels everything, his power is considerable.

As Mighty Consul, Martin controls the economic engine of An\'Ramoda. The gold mine is the foundation of the city\'s military power and trade relationships. Whoever controls the coin controls the city.
'''))

w(B + '/martin-goldberg.es.md', page(
    'Martin "La Moneda" Goldberg',
    'Martin Goldberg, Cónsul Poderoso de An\'Ramoda y propietario de la mina de oro de la ciudad.',
    box(None, 'Martin Goldberg', 'Cónsul Poderoso de An\'Ramoda',
        [('Rol', 'Cónsul Poderoso de An\'Ramoda'), ('Ubicación', "An'Ramoda"), ('Estado', 'Activo')]),
    '''Propietario de la mina de oro de An\'Ramoda y el tercero de los cónsules elegidos por la diosa. El comercio y las monedas son su dominio, y en una ciudad donde la mina lo impulsa todo, su poder es considerable.

Como Cónsul Poderoso, Martin controla el motor económico de An\'Ramoda. La mina de oro es el cimiento del poder militar de la ciudad.
'''))

w(B + '/fernando-oldreekia.md', page(
    'King Fernando Oldreekia',
    'King Fernando Oldreekia, royal ruler of the Lady of Marmaros, whose family has held power since before the gods walked the land.',
    box(None, 'Fernando Oldreekia', 'King of the Lady of Marmaros',
        [('Role', 'King of the Lady of Marmaros'), ('Location', 'Lady of Marmaros'), ('Status', 'Active'), ('House', 'Oldreekia')]),
    '''Royal by blood, the Oldreekia family has held power in the Lady of Marmaros since before the gods walked the land. Fernando rules alongside the Academy and the Guild, though the balance of that triangle is never entirely stable.

## The Power Triangle

| Authority | Description |
|-----------|-------------|
| **King Fernando Oldreekia** | Royal by blood, owner of the Royal Guards, land, and marble mines |
| **The Academy of Magic Wonders** | Led by Magister Monica Mars; growing influence through branded products |
| **The Guild** | Merchant Guild controlling trade registries across Galluvinchia |

And in the shadows: **The Fist**, a network whose leader is known to no one.
'''))

w(B + '/fernando-oldreekia.es.md', page(
    'Rey Fernando Oldreekia',
    'El Rey Fernando Oldreekia, gobernante real de la Dama de Mármaros, cuya familia ha mantenido el poder desde antes de que los dioses pisaran la tierra.',
    box(None, 'Fernando Oldreekia', 'Rey de la Dama de Mármaros',
        [('Rol', 'Rey de la Dama de Mármaros'), ('Ubicación', 'Dama de Mármaros'), ('Estado', 'Activo'), ('Casa', 'Oldreekia')]),
    '''De sangre real, la familia Oldreekia ha mantenido el poder en la Dama de Mármaros desde antes de que los dioses pisaran la tierra. Fernando gobierna junto a la Academia y el Gremio, aunque el equilibrio de ese triángulo nunca es del todo estable.

## El Triángulo del Poder

| Autoridad | Descripción |
|-----------|-------------|
| **Rey Fernando Oldreekia** | Real por sangre, propietario de la Guardia Real, la tierra y las minas de mármol |
| **Academia de Magias Maravillosas** | Dirigida por la Magistrada Monica Mars; poder creciente |
| **El Gremio** | Gremio de mercaderes que controla los registros comerciales de toda Galluvinchia |

Y en las sombras: **El Puño**, cuyo líder nadie conoce.
'''))

w(B + '/merrion-meyer.md', page(
    'Merrion Meyer',
    'Merrion Meyer, Regent of the Academy of Magic Waves and Dreams in Doormi, known for offering the first year of study free.',
    box(None, 'Merrion Meyer', 'Regent of the Academy of Magic Waves and Dreams',
        [('Role', 'Regent of the Academy of Magic Waves and Dreams'), ('Location', 'Doormi'), ('Status', 'Active')]),
    '''Merrion Meyer leads the more humble but generously spirited Academy of Magic Waves and Dreams at Doormi. Where Monica Mars builds empires, Merrion builds opportunities.

The first year of study is free for brilliant students, regardless of background. This policy has made magic more accessible in Doormi than anywhere else in Galluvinchia. The academy\'s specialty is the **Loom of Dreams** and the craft of magical garments.
'''))

w(B + '/merrion-meyer.es.md', page(
    'Merrion Meyer',
    'Merrion Meyer, Regente de la Academia de las Ondas Étereas y los Sueños en Doormi, conocida por ofrecer el primer año de estudio gratis.',
    box(None, 'Merrion Meyer', 'Regente de la Academia de las Ondas Étereas y los Sueños',
        [('Rol', 'Regente de la Academia de las Ondas Étereas y los Sueños'), ('Ubicación', 'Doormi'), ('Estado', 'Activa')]),
    '''Merrion Meyer dirige la Academia de las Ondas Étereas y los Sueños en Doormi. Donde Monica Mars construye imperios, Merrion construye oportunidades.

El primer año de estudio es gratuito para los estudiantes más brillantes, independientemente de su origen. La especialidad de la academia es el **Telar de los Sueños** y la confección de prendas mágicas.
'''))

w(B + '/salgu.md', page(
    'Salgu, King of the Beasts',
    'Salgu, the legendary King of the Beasts who built An\'Ramoda as a sanctuary in the Age of Giants.',
    box(None, 'Salgu', 'King of the Beasts · Founder of An\'Ramoda',
        [('Era', 'First Age · Age of Giants'), ('Role', "Founder of An'Ramoda"), ('Status', 'Historical')]),
    '''In the Age of the Giants, Salgu built the city of An\'Ramoda as a sanctuary where humans, centaurs, and minotaurs could live safely within its tall walls. He is the founding legend of the greatest city in Galluvinchia.

He is also the namesake origin of the minotaur race — the first minotaur was said to be the son of Salgu himself. His memory is revered in An\'Ramoda, and his name is invoked in oaths of valor.
'''))

w(B + '/salgu.es.md', page(
    'Salgu, Rey de las Bestias',
    'Salgu, el legendario Rey de las Bestias que construyó An\'Ramoda como santuario en la Era de los Gigantes.',
    box(None, 'Salgu', 'Rey de las Bestias · Fundador de An\'Ramoda',
        [('Era', 'Primera Era · Era de los Gigantes'), ('Rol', "Fundador de An'Ramoda"), ('Estado', 'Histórico')]),
    '''En la Era de los Gigantes, Salgu construyó An\'Ramoda como un santuario donde humanos, centauros y minotauros pudieran vivir seguros. Es la leyenda fundacional de la mayor ciudad de Galluvinchia.

También es el origen del nombre de la raza minotauro: se dice que el primer minotauro fue el hijo del propio Salgu.
'''))

w(B + '/lumin-oldreekia.md', page(
    'Lumin Oldreekia',
    'Lumin Oldreekia, legendary leokin, greatest felinfolk hero and founder of both the Whisk of Lumin and Lorda Gorda.',
    box(None, 'Lumin Oldreekia', 'The Great Leokin · Founder of Lorda Gorda',
        [('Era', 'Historical'), ('Role', 'Founder of Lorda Gorda · First King'), ('Status', 'Historical · Legacy endures')]),
    '''The greatest hero of the felinfolk, Lumin Oldreekia was the legendary leokin who created the first felinfolk city, now called the Whisk of Lumin, along the southern coast, as a bastion against sandstorms, pirates, and ghouls.

He later became the first king of Lorda Gorda. Centuries later, the Whisk of Lumin still stands, its towers guarding the eastern horizon night and day.

The [Maneless King](maneless-king.md) is seen as his spiritual heir. His legend is told in full in the [Tales of Galluvinchia](../tales/index.md).
'''))

w(B + '/lumin-oldreekia.es.md', page(
    'Lumin Oldreekia',
    'Lumin Oldreekia, el legendario leokin, mayor héroe felicios y fundador del Whisk de Lumin y Lorda Gorda.',
    box(None, 'Lumin Oldreekia', 'El Gran Leokin · Fundador de Lorda Gorda',
        [('Era', 'Histórica'), ('Rol', 'Fundador de Lorda Gorda · Primer Rey'), ('Estado', 'Histórico · Legado perdura')]),
    '''El mayor héroe de los felicios, Lumin Oldreekia fue el legendario leokin que creó la primera ciudad felicia, ahora llamada el Whisk de Lumin, en la costa sur, como bastión contra tormentas de arena, piratas y necrófagos.

Más tarde se convirtió en el primer rey de Lorda Gorda. Siglos después, el Whisk de Lumin sigue en pie.

El [Rey sin Melena](maneless-king.md) es visto como su heredero espiritual.
'''))

w(B + '/alice-rockwool.md', page(
    'Alice Rockwool',
    'Alice Rockwool, adventurer and legend of the timeless library discovered beneath Lakobordo.',
    box(None, 'Alice Rockwool', 'Adventurer · Legend of the Library of Lakobordo',
        [('Role', 'Adventurer'), ('Last known location', 'Lakobordo'), ('Status', 'Unknown')]),
    '''Traveling the depths beneath Lakobordo, Alice Rockwool and her companions discovered a timeless library long lost to the world, amid marble pillars and pale tourmaline dust.

A cyclopean construct stood waiting for them. Before the battle could begin, Alice Rockwool stepped forward and said:

> *"Yield to the sword of your masters! Look upon it!"*

And the construct kneeled.

Whether this is history or a tall tale depends on who is doing the telling.
'''))

w(B + '/alice-rockwool.es.md', page(
    'Alice Rockwool',
    'Alice Rockwool, aventurera y leyenda de la biblioteca atemporal descubierta bajo Lakobordo.',
    box(None, 'Alice Rockwool', 'Aventurera · Leyenda de la Biblioteca de Lakobordo',
        [('Rol', 'Aventurera'), ('Última ubicación conocida', 'Lakobordo'), ('Estado', 'Desconocido')]),
    '''Viajando por las profundidades bajo Lakobordo, Alice Rockwool y sus compañeros descubrieron una biblioteca atemporal perdida para el mundo, entre pilares de mármol y pálido polvo de turmalina.

Un autómata de inmensas proporciones los aguardaba. Antes de que la batalla pudiera comenzar, Alice Rockwool dio un paso al frente y dijo:

> *"¡Ríndete ante la espada de tus maestros! ¡Mírala!"*

Y el autómata se arrodilló.
'''))

print("Done: " + str(len(os.listdir(B))) + " files in " + B)
