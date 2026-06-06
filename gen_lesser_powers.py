#!/usr/bin/env python3
import os

B = "wiki-docs/gods/lesser-powers"
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
description: Beyond the six gods, Galluvinchia is shaped by ancient and hidden powers, the Light, the Will of the Wild, the Tarnished Star, the Nameless One and more.
---

# Lesser Powers & Legends

Not all powerful entities in Galluvinchia are among the six gods. Some are ancient, some are hidden, and some are best not spoken of too loudly.

<div class="grid cards" markdown>

-   **[The Light](the-light.md)**

    ---

    Many Galluvinchians pray to the Light rather than any specific god, bound by oaths of clarity and honesty.

-   **[The Will of the Wild](will-of-the-wild.md)**

    ---

    The eternal warden of Aurora Densasilva, whose veins are the roots of every tree in Galluvinchia.

-   **[The Long-Lost Paladins](long-lost-paladins.md)**

    ---

    Echoes of ancient paladins wandering the ruins, seeking a new champion to wield freedom and justice.

-   **[The Tarnished Star](tarnished-star.md)**

    ---

    An empress from a distant land who watches, waits, and sends abyss walkers ahead of her arrival.

-   **[The Nameless One](nameless-one.md)**

    ---

    A cosmic force swimming through the universe, seeking the collapse of all existence.

-   **[The Lady of Horns](lady-of-horns.md)**

    ---

    A voice rising from the depths beneath the Lord of Carbohyrr, of unknown origin and uncertain intentions.

-   **[The Long-Lost Dragons](dragons.md)**

    ---

    Part of everyone\'s collective memory: a time when dragons inhabited Galluvinchia. Or so they say.

-   **[Archlich Kogarashi](../../characters/kogarashi.md)**

    ---

    The necromancer who waged the Arcane War against the gods. His body was never found.

</div>
''')

# ── Index ES ──
w(B + '/index.es.md', '''---
description: Más allá de los seis dioses, Galluvinchia está moldeada por poderes antiguos y ocultos: la Luz, la Voluntad de lo Salvaje, la Estrella Deslustrada, el Innombrable y más.
---

# Poderes Menores y Leyendas

No todos los seres poderosos de Galluvinchia están entre los seis dioses. Algunos son antiguos, algunos están ocultos y de algunos es mejor no hablar demasiado alto.

<div class="grid cards" markdown>

-   **[La Luz](the-light.md)**

    ---

    Muchos galluvinchianos rezan a la Luz en lugar de a un dios concreto, ligados por juramentos de claridad y honestidad.

-   **[La Voluntad de lo Salvaje](will-of-the-wild.md)**

    ---

    La guardiana eterna de Aurora Densasilva, cuyas venas son las raíces de todos los árboles de Galluvinchia.

-   **[Los Paladines Olvidados](long-lost-paladins.md)**

    ---

    Ecos de paladines antiguos que deambulan por las ruinas, buscando un nuevo campeón para empuñar la libertad y la justicia.

-   **[La Estrella Deslustrada](tarnished-star.md)**

    ---

    Una emperatriz de tierras lejanas que observa, espera y envía caminantes del abismo por delante de su llegada.

-   **[El Innombrable](nameless-one.md)**

    ---

    Una fuerza cósmica que nada por el universo buscando el colapso de toda la existencia.

-   **[La Dama de Astas](lady-of-horns.md)**

    ---

    Una voz que asciende desde las profundidades bajo el Señor de Carbohyrr, de origen e intenciones desconocidas.

-   **[Los Dragones Perdidos](dragons.md)**

    ---

    Parte de la fantasía colectiva de todos: hubo un tiempo en que los dragones habitaban Galluvinchia. O eso dicen.

-   **[Archliche Kogarashi](../../characters/kogarashi.md)**

    ---

    El nigromante que libró la Guerra Arcana contra los dioses. Su cuerpo nunca fue encontrado.

</div>
''')

# ── The Light ──
w(B + '/the-light.md', page(
    'The Light',
    'The Light, the nameless divine force many Galluvinchians pray to instead of a specific god, bound by oaths of clarity and honesty.',
    box(None, 'The Light', 'The Nameless Divine · Faith of the Common People',
        [('Nature', 'Divine force · Not a deity'), ('Followers', 'Common people · Felinfolk of Lorda Gorda'),
         ('Tenets', 'Clarity · Honesty · Noble oaths')]),
    '''Many Galluvinchians pray to the Light rather than any specific god. Followers of the Light tend to be noble, naive, and optimistic, bound by oaths of clarity and honesty.

The Light has no temple, no clergy, and no myth of origin. It simply exists, and those who choose it find in it a moral framework that asks more of them than the gods do.

> *"The Light finds the way."*
> *"The Light doesn\'t shine in darkness."*

## Lorda Gorda

The felinfolk of Lorda Gorda pray to the Light above all others, shunning the six gods entirely. The pink crystals that light their city are a physical expression of the soul-light they believe resides in every living being.
'''))

w(B + '/the-light.es.md', page(
    'La Luz',
    'La Luz, la fuerza divina sin nombre a la que muchos galluvinchianos rezan en lugar de a un dios concreto, ligados por juramentos de claridad y honestidad.',
    box(None, 'La Luz', 'Lo Divino Sin Nombre · Fe del Pueblo',
        [('Naturaleza', 'Fuerza divina · No una deidad'), ('Seguidores', 'Pueblo común · Felicios de Lorda Gorda'),
         ('Principios', 'Claridad · Honestidad · Juramentos nobles')]),
    '''Muchos galluvinchianos rezan a la Luz en lugar de a un dios concreto. Los seguidores de la Luz tienden a ser nobles, ingenuos y optimistas, ligados por juramentos de claridad y honestidad.

La Luz no tiene templo, ni clérigos, ni mito de origen. Simplemente existe, y quienes la eligen encuentran en ella un marco moral que les exige más de lo que los dioses exigen.

> *"La Luz revela el camino."*
> *"La Luz no brilla en la oscuridad."*

## Lorda Gorda

Los felicios de Lorda Gorda rezan a la Luz por encima de todos los demás, rechazando por completo a los seis dioses. Los cristales rosas que iluminan su ciudad son una expresión física de la luz anímica que creen que reside en cada ser vivo.
'''))

# ── Will of the Wild ──
w(B + '/will-of-the-wild.md', page(
    'The Will of the Wild',
    'The Will of the Wild, the eternal power of nature and warden of Aurora Densasilva, whose veins are the roots of every tree in Galluvinchia.',
    box('artwork-will-of-wild.webp', 'Will of the Wild', 'The Eternal Warden · Power of Nature',
        [('Nature', 'Primordial force · Not a deity'), ('Domain', 'All of nature · Aurora Densasilva'),
         ('Herald', 'The Queen of Branches'), ('Attitude', 'Protective · Capricious · Ancient')]),
    '''From times untold, the power of nature has been held by the Will of the Wild. Its veins are the roots of all the trees of Galluvinchia, and it is the forever warden of **[Aurora Densasilva](../../regions/points-of-interest/aurora-densasilva.md)**, the eternal forest. Its ways may be eerie or twisted, but it will forever protect nature, one way or another.

## The Queen of Branches

The Will of the Wild does not speak in words most mortals understand. In grave matters, it acts through its herald: the **Queen of Branches**, a figure who embodies the forest\'s judgment and carries its authority.

Only friends of the forest are welcome in Aurora Densasilva. Those who enter without invitation are turned away, lost, or never seen again.

## Conflict with An\'Ramoda

An\'Ramoda continues to expand eastward into the forest. The Will of the Wild burns with resentment. The pact that [Aremedia](../aremedia.md) brokered long ago is maintained more by memory than by trust.
'''))

w(B + '/will-of-the-wild.es.md', page(
    'La Voluntad de lo Salvaje',
    'La Voluntad de lo Salvaje, el poder eterno de la naturaleza y guardiana de Aurora Densasilva, cuyas venas son las raíces de todos los árboles de Galluvinchia.',
    box('artwork-will-of-wild.webp', 'Voluntad de lo Salvaje', 'La Guardiana Eterna · Poder de la Naturaleza',
        [('Naturaleza', 'Fuerza primordial · No una deidad'), ('Dominio', 'Toda la naturaleza · Aurora Densasilva'),
         ('Heraldo', 'La Reina de las Ramas'), ('Actitud', 'Protectora · Caprichosa · Antigua')]),
    '''Desde tiempos inmemoriales, el poder de la naturaleza ha sido custodiado por la Voluntad de lo Salvaje. Sus venas son las raíces de todos los árboles de Galluvinchia, y es la guardiana eterna de **[Aurora Densasilva](../../regions/points-of-interest/aurora-densasilva.md)**, el bosque perpetuo.

## La Reina de las Ramas

La Voluntad de lo Salvaje no habla con palabras que la mayoría de los mortales entiendan. En asuntos graves, actúa a través de su heraldo: la **Reina de las Ramas**, una figura que encarna el juicio del bosque.

## Conflicto con An\'Ramoda

An\'Ramoda continúa expandiéndose hacia el este. La Voluntad de lo Salvaje arde de resentimiento. El pacto que [Aremedia](../aremedia.md) negoció hace mucho tiempo se mantiene más por la memoria que por la confianza.
'''))

# ── Long-Lost Paladins ──
w(B + '/long-lost-paladins.md', page(
    'The Long-Lost Paladins',
    'The Long-Lost Paladins, echoes of ancient warriors wandering the ruins of Galluvinchia, seeking a new champion to carry the torch of freedom and justice.',
    box('artwork-order.webp', 'The Long-Lost Paladins', 'The Order · Echoes of Ancient Warriors',
        [('Nature', 'Spiritual echoes · Ancient order'), ('Purpose', 'Seeking a new champion'),
         ('Location', 'Wandering the ruins of Galluvinchia')]),
    '''Wandering the ruins of Galluvinchia, the echoes of ancient paladins drift like angels serving justice. They seek to raise a new champion, one who will make freedom their shield and justice their sword.

Who these paladins were in life, what order they served, and what destroyed them is knowledge mostly lost. Only their purpose persists, carried in the echo of their armor and the dim light of their convictions.

Those who encounter them describe a sense of being tested, as if the paladins are looking through the person rather than at them.
'''))

w(B + '/long-lost-paladins.es.md', page(
    'Los Paladines Olvidados',
    'Los Paladines Olvidados, ecos de guerreros antiguos que deambulan por las ruinas de Galluvinchia buscando un nuevo campeón para portar la antorcha de la libertad y la justicia.',
    box('artwork-order.webp', 'Los Paladines Olvidados', 'La Orden · Ecos de Guerreros Antiguos',
        [('Naturaleza', 'Ecos espirituales · Orden antigua'), ('Propósito', 'Buscar un nuevo campeón'),
         ('Ubicación', 'Vagando por las ruinas de Galluvinchia')]),
    '''Deambulando por las ruinas de Galluvinchia, los ecos de paladines perdidos en el tiempo flotan como ángeles al servicio de la justicia. Buscan un nuevo campeón que pueda hacer de la libertad su escudo y de la justicia su espada.

Quiénes fueron estos paladines en vida, a qué orden servían y qué los destruyó es un conocimiento casi perdido. Solo su propósito persiste, llevado en el eco de su armadura y la tenue luz de sus convicciones.

Quienes los encuentran describen una sensación de ser evaluados, como si los paladines miraran a través de la persona y no hacia ella.
'''))

# ── Tarnished Star ──
w(B + '/tarnished-star.md', page(
    'The Tarnished Star',
    'The Tarnished Star, an empress from a distant land who sends abyss walkers ahead of her, watching and waiting for the right herald to open the way.',
    box('artwork-tarnished-star.webp', 'The Tarnished Star', 'Empress from Beyond · The Patient Conqueror',
        [('Nature', 'Empress · Extra-planar power'), ('Domain', 'Many worlds'),
         ('Heralds', 'Abyss walkers (half shark, half person)'), ('Status', 'Watching · Waiting')]),
    '''In a distant land, abyss walkers, half shark, half person, lure souls from afar and invade realms with mighty power. Their empress, the Tarnished Star, holds the power of many worlds.

She watches. She waits. She looks for heralds who will allow her to visit and rule.

## Abyss Walkers

The advance agents of the Tarnished Star are unsettling creatures, part predator, part envoy. They do not invade openly. They gather information, test defenses, and recruit the willing. Those who bargain with them rarely understand the full terms of what they have agreed to.

## The Threat

The Tarnished Star has not yet turned her full attention to Galluvinchia. Whether this is because she is occupied elsewhere, because she finds it unworthy, or because she is still preparing, is a question no scholar has managed to answer.
'''))

w(B + '/tarnished-star.es.md', page(
    'La Estrella Deslustrada',
    'La Estrella Deslustrada, una emperatriz de tierras lejanas que envía caminantes del abismo por delante de ella, observando y esperando al heraldo adecuado que le abra el camino.',
    box('artwork-tarnished-star.webp', 'La Estrella Deslustrada', 'Emperatriz de Más Allá · La Conquistadora Paciente',
        [('Naturaleza', 'Emperatriz · Poder extra-planar'), ('Dominio', 'Muchos mundos'),
         ('Heraldos', 'Caminantes del abismo (mitad tiburón, mitad persona)'), ('Estado', 'Observando · Esperando')]),
    '''En tierras lejanas, caminantes del abismo, mitad tiburón, mitad persona, atraen almas de lugares remotos e invaden reinos con un poder descomunal. Su emperatriz, la Estrella Deslustrada, ostenta el poder de muchos mundos.

Observa. Espera. Busca heraldos que le permitan visitar y gobernar.

## Los Caminantes del Abismo

Los agentes de avanzada de la Estrella Deslustrada son criaturas inquietantes. No invaden abiertamente. Recopilan información, prueban defensas y reclutan voluntarios. Quienes pactan con ellos raramente comprenden los términos completos de lo que han acordado.
'''))

# ── Nameless One ──
w(B + '/nameless-one.md', page(
    'The Nameless One',
    'The Nameless One, a cosmic force swimming through the universe seeking the collapse of all existence, creator of the void and wielder of sadness.',
    box('artwork-nameless-one.webp', 'The Nameless One', 'Creator of the Void · Wielder of Sadness',
        [('Nature', 'Cosmic force · Ancient beyond measure'), ('Goal', 'Collapse of all existence'),
         ('Domain', 'The void · Sadness'), ('Status', 'Travelling through space and time')]),
    '''Swimming through the universe, the Nameless One wants the collapse of all existence, to consume all life, perhaps out of hatred, perhaps seeking peace when all light has gone out. The creator of the void and the wielder of sadness, it travels relentlessly through space and time.

It has no followers. It does not seek them. It does not communicate. It simply moves, and where it has passed, things are quieter.

Whether it is aware of Galluvinchia, and whether it matters, is a question the scholars of the Academy prefer not to investigate too deeply.
'''))

w(B + '/nameless-one.es.md', page(
    'El Innombrable',
    'El Innombrable, una fuerza cósmica que nada por el universo buscando el colapso de toda la existencia, creador del vacío y portador de la tristeza.',
    box('artwork-nameless-one.webp', 'El Innombrable', 'Creador del Vacío · Portador de la Tristeza',
        [('Naturaleza', 'Fuerza cósmica · Antiguo más allá de toda medida'), ('Objetivo', 'Colapso de toda la existencia'),
         ('Dominio', 'El vacío · La tristeza'), ('Estado', 'Viajando por el espacio y el tiempo')]),
    '''Nadando por el universo, el Innombrable desea el colapso de toda la existencia, consumir toda vida, quizás por odio, quizás buscando la paz cuando toda la luz se haya apagado. El creador del vacío y portador de la tristeza, viaja incansable por el espacio y el tiempo.

No tiene seguidores. No los busca. No se comunica. Simplemente se mueve, y donde ha pasado, las cosas son más silenciosas.

Si es consciente de Galluvinchia, y si eso importa, es una pregunta que los eruditos de la Academia prefieren no investigar demasiado.
'''))

# ── Lady of Horns ──
w(B + '/lady-of-horns.md', page(
    'The Lady of Horns',
    'The Lady of Horns, a voice rising from the depths beneath the Lord of Carbohyrr, of unknown origin and uncertain intentions, who whispers to Moroes.',
    box(None, 'The Lady of Horns', 'Voice from the Deep · The Unknown Bargainer',
        [('Nature', 'Unknown'), ('Location', 'Deep below the Lord of Carbohyrr'),
         ('Known contact', 'Moroes'), ('Intentions', 'Unknown')]),
    '''Deep below the Lord of Carbohyrr, a voice reaches upward. Of unknown origin and uncertain intentions, her whispers find the ears of [Moroes](../moroes.md), and those brave or foolish enough to bargain with her.

What she wants, what she offers, and what she takes in return is not widely known. What is known is that those who have dealt with her describe a cold clarity, like a bargain struck in a language one only half understands.

[Moroes](../moroes.md) hears her still.
'''))

w(B + '/lady-of-horns.es.md', page(
    'La Dama de Astas',
    'La Dama de Astas, una voz que asciende desde las profundidades bajo el Señor de Carbohyrr, de origen e intenciones desconocidas, que susurra a Moroes.',
    box(None, 'La Dama de Astas', 'Voz desde las Profundidades · La Negociadora Desconocida',
        [('Naturaleza', 'Desconocida'), ('Ubicación', 'Profundidades bajo el Señor de Carbohyrr'),
         ('Contacto conocido', 'Moroes'), ('Intenciones', 'Desconocidas')]),
    '''En las profundidades bajo el Señor de Carbohyrr, la voz que enloqueció a [Moroes](../moroes.md) provenía de una mujer, la Dama de Astas. De origen e intenciones desconocidas, sus oscuros planes solo pueden ser escuchados por Moroes y seguidos por quienes sean lo suficientemente valientes, o locos, para firmar un pacto con ella.

Qué quiere, qué ofrece y qué toma a cambio no es ampliamente conocido. Lo que se sabe es que quienes han tratado con ella describen una claridad fría, como un trato cerrado en un idioma que solo se entiende a medias.

[Moroes](../moroes.md) aún la escucha.
'''))

# ── Dragons ──
w(B + '/dragons.md', page(
    'The Long-Lost Dragons',
    'The Long-Lost Dragons of Galluvinchia, part of collective memory, hunted by gods or fought by giants, perhaps sleeping somewhere still.',
    box('artwork-dragon.webp', 'The Long-Lost Dragons', 'Creatures of the Old Age · Sleeping or Gone',
        [('Status', 'Unknown — last seen in living memory: never'), ('Era', 'Age of Primordials and before'),
         ('Known individual', 'Krusninglömda, Elder Dragon from the Marble Veins')]),
    '''Part of everyone\'s collective memory: there was a time when dragons inhabited Galluvinchia, or so they say. Slain by gods or fought by giants, do they still hold treasures in forgotten caves, or are they sleeping somewhere, waiting?

## Krusninglömda

One name surfaces in the oldest texts recovered from the Lady of Marmaros: **Krusninglömda**, an Elder Dragon said to have made its home in the marble veins deep below what is now the city. Whether it was slain during the founding of Marmaros, or simply retreated deeper, no scholar has confirmed.

## The Collective Memory

No one alive has seen a dragon. But the word for dragon exists in every language in Galluvinchia, including ones so old they are no longer spoken. Something named them. Something remembered them long enough for the word to survive.
'''))

w(B + '/dragons.es.md', page(
    'Los Dragones Perdidos',
    'Los Dragones Perdidos de Galluvinchia, parte de la memoria colectiva, cazados por dioses o combatidos por gigantes, quizás durmiendo aún en algún lugar.',
    box('artwork-dragon.webp', 'Los Dragones Perdidos', 'Criaturas de la Era Antigua · Dormidos o Extintos',
        [('Estado', 'Desconocido — último avistamiento en memoria viva: nunca'), ('Era', 'Era de los Primordiales y antes'),
         ('Individuo conocido', 'Krusninglömda, Dragón Anciano de las Venas de Mármol')]),
    '''Parte de la fantasía colectiva de todos: hubo un tiempo en que los dragones habitaban Galluvinchia, o eso dicen. Cazados por los dioses o combatidos por los gigantes, ¿guardan tesoros en cuevas olvidadas, o duermen en algún lugar esperando?

## Krusninglömda

Un nombre surge en los textos más antiguos recuperados de la Dama de Mármaros: **Krusninglömda**, un Dragón Anciano que se dice que tuvo su hogar en las venas de mármol bajo lo que hoy es la ciudad. Si fue cazado durante la fundación de Mármaros, o simplemente se retiró más profundo, ningún erudito lo ha confirmado.

## La Memoria Colectiva

Nadie vivo ha visto un dragón. Pero la palabra para dragón existe en todos los idiomas de Galluvinchia, incluidos algunos tan antiguos que ya no se hablan. Algo los nombró. Algo los recordó el tiempo suficiente para que la palabra sobreviviera.
'''))

# Remove old lesser-powers.md files (replaced by directory)
for old in ["wiki-docs/gods/lesser-powers.md", "wiki-docs/gods/lesser-powers.es.md"]:
    if os.path.exists(old):
        os.remove(old)
        print("Removed: " + old)

print("Done lesser powers: " + str(len(os.listdir(B))) + " files.")
