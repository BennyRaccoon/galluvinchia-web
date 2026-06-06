#!/usr/bin/env python3
import os

B = "wiki-docs/tales"
os.makedirs(B, exist_ok=True)

def w(p, c):
    with open(p, "w", encoding="utf-8") as f:
        f.write(c)

# ── Updated index EN ──
w(B + '/index.md', '''---
description: Tales and legends from the world of Galluvinchia, myths of gods and heroes, epic arcane wars and the stories the land still remembers.
---

# Tales of Galluvinchia

Every culture in Galluvinchia tells stories. Some of those stories are true. Some of them are true in ways that facts cannot capture. And some of them are lies so old they have become true simply by being believed long enough.

This is the archive of what has been told.

## Types of Tales

| Type | Description |
|------|-------------|
| **Myth** | Stories about the gods and the shaping of the world |
| **Legend** | Stories about mortal heroes and the deeds that made them |
| **Folktale** | Stories told by common people, often with practical wisdom buried inside |
| **Chronicle** | Records of events written by those who claimed to witness them |

---

<div class="grid cards" markdown>

-   **[Myths](myths.md)**

    ---

    Stories of the gods: the Arcane War, the Gems of Origin, the Pillars of Rebirth, and the tales that explain the shape of the world.

-   **[Legends](legends.md)**

    ---

    Tales of mortal heroes: the founding of Lorda Gorda, the library beneath Lakobordo, and the deeds that outlasted their makers.

-   **[Folktales](folktales.md)**

    ---

    What the common folk say: the moon that never moves, the sound of the anvil, and the wisdom carried in old stories.

</div>
''')

# ── Updated index ES ──
w(B + '/index.es.md', '''---
description: Relatos y leyendas del mundo de Galluvinchia, mitos de dioses y héroes, épicas guerras arcanas y las historias que la tierra aún recuerda.
---

# Fábulas de Galluvinchia

Cada cultura en Galluvinchia cuenta historias. Algunas de esas historias son verdad. Algunas son verdad de maneras que los hechos no pueden capturar. Y algunas son mentiras tan antiguas que se han vuelto verdad por el simple hecho de creerse el tiempo suficiente.

Este es el archivo de lo que se ha contado.

## Tipos de Relatos

| Tipo | Descripción |
|------|-------------|
| **Mito** | Historias sobre los dioses y la formación del mundo |
| **Leyenda** | Historias sobre héroes mortales y las hazañas que los hicieron grandes |
| **Cuento Popular** | Historias contadas por el pueblo, a menudo con sabiduría práctica escondida dentro |
| **Crónica** | Registros de eventos escritos por quienes afirmaron ser testigos |

---

<div class="grid cards" markdown>

-   **[Mitos](myths.md)**

    ---

    Historias de los dioses: la Guerra Arcana, las Gemas del Origen, los Pilares del Resurgimiento, y los relatos que explican la forma del mundo.

-   **[Leyendas](legends.md)**

    ---

    Hazañas de héroes mortales: la fundación de Lorda Gorda, la biblioteca bajo Lakobordo, y los actos que sobrevivieron a quienes los realizaron.

-   **[Cuentos Populares](folktales.md)**

    ---

    Lo que dice el pueblo: la luna que nunca se mueve, el sonido del yunque, y la sabiduría en las historias antiguas.

</div>
''')

# ── Myths EN ──
w(B + '/myths.md', '''---
description: The myths of Galluvinchia, stories of the gods that explain the shape of the world, from the Arcane War to the Thread of Virtue.
---

# Myths, Stories of the Gods

---

### The Arcane War
*A Myth of Panos and Kogarashi*

![Archlich Kogarashi](../img/character-kogarashi.webp){ .wiki-portrait }

When the cosmos echoed with the whispers of newly born deities, an archmage of unparalleled fury arose: [Kogarashi](../characters/kogarashi.md). Having witnessed the gods\' ascent, he denounced them with seething contempt, calling them usurpers of divine thrones, ignorant of the true arcane arts.

He forged an unholy pact with a conclave of formidable mages and vowed to overthrow the celestial order.

The war that followed shook Galluvinchia. Its final clash erupted in the forsaken abyss of **Ancho Groncho**, a place where shadows breathed and labyrinths wove their own destinies.

[Panos](../gods/panos.md) triumphed over the rebellious mages. Yet the body of Kogarashi was never found, hidden somewhere in the labyrinthine depths the archmage had crafted with his own hand. For countless years, Panos has wandered the land, searching for the elusive scent of Kogarashi\'s lingering sorcery.

---

### The Gems of Origin
*A Myth of Panos*

Older than time and crafted from the Ripple itself, gems of unimaginable power were scattered across Galluvinchia. These gems represent the different forces of existence: *Light, Growth, Time,* and *Heat*.

One of them was gifted to Aremedia by Panos himself, and it is that gem whose light illuminates the city of An\'Ramoda.

Where the others are, no one says for certain.

---

### The Gates
*A Vision of Panos*

In the silent hours of the night, Panos is tormented by visions of a shadowy figure emerging from portals to claim Galluvinchia. These dreams, he believes, are more than mere figments, they are prophecies.

Within his fragmented sacred texts, he speaks of portals existing around the world, and his endless endeavor to find the key to using them, understanding how they work, and uncovering the truth behind them.

---

### The Pillars of Rebirth
*A Myth of Panos and Brenadette*

The restless Brenadette, bound forever to the Neverender by her eternal duty, brought Panos into a hollow sadness. He promised her that he would fix the cycle, so it could run without her constant vigil.

She could not envision when that time would come. But from Panos\'s loving words, she held hope.

Since that day, Panos wanders the world searching for the **Pillars of Rebirth**, to free his lover from her eternal burden.

---

### The Cycle of Life
*A Myth of Brenadette*

Right after defeating the Primordials and ascending to divinity, Brenadette realized that someone must take care of the Cycle of Life, to guide souls to the Renewal and bring new ones into existence.

She travelled to the Neverender and has wandered its scorched ground ever since, slave to the Renewal. The perpetual sight of its light made her blind. She has never slept again.

---

### The Tainted Tribe
*A Myth of Brenadette and the Serpent Aolosh*

A tribe descended into madness when their patron, the mythical snake Aolosh, was vanquished by the gods during their ascent to divinity. Driven by fury and despair, the tribe ventured into the Neverender and waged a ferocious battle against Brenadette herself.

With the aid of Aremedia, the tribe was defeated and banished back to their island, **Ourobolis**, where the sea turned purple with the serpent\'s tainted blood.

The tribe continues to venerate Aolosh and is said to conduct the most extreme rituals in all of Galluvinchia.

---

### Giants of the North
*A Myth of Aremedia*

Long ago, the giants lived harmoniously in An\'Ramoda, building and protecting alongside the rest of its citizens. But among them, a choleric madness began to spread, an uncontrollable rage that threatened the city\'s peace.

Aremedia, commanding her formidable army, acted decisively. She exiled the giants from An\'Ramoda and banished them to the far reaches of the North, where her influence wanes.

The giants have not forgotten this exile.

---

### The Fight With the Wild
*A Myth of Aremedia and Aurora Densasilva*

Not long after the giants\' exile, a new challenge emerged from the East. The forces of nature began to surge across the land, mighty roots tearing through farms, swallowing mills and structures whole.

Just as the expansion seemed unstoppable, Aremedia brokered a pact with the very heart of the forest. By agreeing to respect its ancient boundaries, she brought the growth to a halt.

Since that agreement, a delicate peace has reigned between An\'Ramoda and the wilds, maintained more by memory than by trust.

---

### Moroes the Lover
*A Myth of Moroes and Morphia*

![Moroes, God of the Forge](../img/artwork-moroes.webp){ .wiki-portrait }

Deep in the Lord of Carbohyrr, long before anyone ascended to divinity, a craftsman named Moroes fell in love with Morphia. His love for her was on par with his craftsmanship, and both were second to none.

He gifted the gods item after item, each one granting them more power, the sound of his anvil keeping rhythm with his heartbeat. He asked for Morphia\'s hand in exchange, and was promised it.

But when divinity was achieved, the wedding was cancelled.

Even if the blessing of godhood was shared with him, it was not enough to fill the void. Until the end of days, the heartbeat of his anvil is the only thing that stops the ache.

---

### The Thread of Virtue
*A Myth of Morphia*

After enduring the pain of leaving Moroes behind, and after a long period of isolation and grief, Morphia emerged with a renewed perspective. She wandered the land and, after great determination, created the **Thread of Virtue**, a divine thread imbued with the essence of her experiences.

With it, she founded the **Academy of Magic Waves and Dreams**, where magically attuned people from across the land would come to learn, grow, and craft garments that make everyone\'s life a little more wonderful.

---

### The Beauty of Her Life
*A Myth of Morphia and Leeve*

![Leeve, Goddess of Beauty and Nature](../img/artwork-leeve.webp){ .wiki-portrait }

With her heart shattered by the end of her relationship with Moroes, Morphia withdrew into nature, her divine duties abandoned, her presence dimmed by sorrow.

Seeing their goddess in despair, one of her devoted paladins swore an oath to restore Morphia to her grace. The paladin journeyed far and wide, seeking wisdom in ancient scripts and from wise scholars.

Through gentle words and acts of kindness, she drew Morphia out of her isolation. As Morphia\'s heart began to heal, she saw in the paladin a reflection of everything she had forgotten existed.

Moved by this realization, Morphia bestowed upon the paladin a divine gift, elevating her to godhood. The paladin became **Leeve**, goddess of beauty and nature.

---

### The Last Lost Scholar
*A Myth of Leeve*

Although raised a paladin, the benevolent Leeve was also deeply knowledgeable of the arcane, an intellectual whose focus was nature itself. She spent most of her early years in the halls of the **Academy of Infinite Travels**, a long-forgotten institution.

Dire times arrived. One by one, her teachers vanished.

When the last of them disappeared, she turned to the only one she could trust: her close friend Morphia.

---

### The Granter of the Holy
*A Myth of Moroes*

Before divinity, before heartbreak, Moroes\'s craftsmanship was already rivalled by none. Gift after gift, tools of power, items of wonder, he placed at the feet of those who would become gods.

Each was made in exchange for something. Each was made to the rhythm of his heartbeat.

In the end, he received godhood and a broken heart.

*Some say he is still paying the cost of that bargain.*
''')

# ── Myths ES ──
w(B + '/myths.es.md', '''---
description: Los mitos de Galluvinchia, historias de los dioses que explican la forma del mundo, desde la Guerra Arcana hasta el Hilo de la Virtud.
---

# Mitos, Historias de los Dioses

---

### La Guerra Arcana
*Un Mito de Panos y Kogarashi*

![Archliche Kogarashi](../img/character-kogarashi.webp){ .wiki-portrait }

Cuando el cosmos resonó con los susurros de las recién nacidas deidades, también engendró un archimago de furia y ambición sin par: [Kogarashi](../characters/kogarashi.md).

Tras el ascenso de los dioses a la divinidad, un desprecio hirviente lo habitaba, anunciándolos como usurpadores. Forjó un pacto prohibido con un cónclave de poderosos magos, jurando derrocar el orden celestial.

La guerra que siguió sacudió Galluvinchia. Su enfrentamiento final estalló en el olvidado abismo de **Ancho Groncho**, un lugar donde las sombras respiraban.

[Panos](../gods/panos.md) triunfó sobre la rebelión de los magos. Sin embargo, el cuerpo del archimago Kogarashi no fue encontrado en ningún lugar. Durante incontables años, Panos ha recorrido las tierras buscando el escurridizo rastro de la hechicería latente de Kogarashi.

---

### Las Gemas del Origen
*Un Mito de Panos*

Más antiguas que el tiempo y forjadas de la propia Reverberación, gemas de un poder inimaginable están dispersadas por las tierras de Galluvinchia. Estas gemas representan las diferentes fuerzas de la existencia: *Luz, Crecimiento, Tiempo* y *Calor*.

Una de ellas fue entregada a Aremedia por Panos, y es la luz que ilumina An\'Ramoda.

Dónde están las demás, nadie lo dice con certeza.

---

### Las Puertas
*Una Visión de Panos*

En el silencio de la noche, Panos es atormentado por visiones de una figura oscura emergiendo de portales para reclamar Galluvinchia. Estos sueños, cree, son más que meras ensoñaciones, son profecías.

En sus escasos escritos sagrados, habla de portales dispersos por el mundo y de su empeño por encontrar la llave para usarlos.

---

### Los Pilares del Resurgimiento
*Un Mito de Panos y Brenadette*

La incansable Brenadette sumió a Panos en una honda tristeza. Él le prometió arreglar el ciclo, para que pudiera funcionar sin su constante vigilia.

Desde ese día, Panos recorre el mundo buscando los **Pilares del Resurgimiento**, para liberar a su amada de esta carga eterna.

---

### El Ciclo de la Vida
*Un Mito de Brenadette*

Justo después de derrotar a los Primordiales y ascender a la divinidad, Brenadette comprendió que alguien debía hacerse cargo del Ciclo de la Vida.

Viajó al Rencarnatorno y desde entonces recorre su suelo abrasado, esclava del Resurgimiento. La visión perpetua de su luz la dejó ciega. Nunca ha vuelto a dormir.

---

### La Tribu Corrupta
*Un Mito de Brenadette y la Serpiente Aolosh*

Una tribu descendió a la locura cuando su patrón, la mítica serpiente Aolosh, fue vencida por los dioses. Impulsada por la furia y la desesperación, la tribu se adentró en el Rencarnatorno y libró una feroz batalla contra la propia Brenadette.

Con la ayuda de Aremedia, la tribu fue finalmente derrotada y desterrada de vuelta a su isla, **Ourobolis**, donde el mar se tiñó de púrpura.

La tribu continúa venerando a Aolosh y se dice que lleva a cabo los rituales más extremos de todo Galluvinchia.

---

### Los Gigantes del Norte
*Un Mito de Aremedia*

Hace mucho tiempo, los gigantes vivían en armonía en An\'Ramoda. Pero entre ellos, una colérica locura comenzó a extenderse.

Aremedia tomó medidas decisivas. Desterró a los gigantes de An\'Ramoda y los mandó a los confines del norte.

Los gigantes no han olvidado este exilio.

---

### La Lucha con lo Salvaje
*Un Mito de Aremedia y Aurora Densasilva*

No mucho después del exilio de los gigantes, surgió un nuevo desafío desde el este. Las fuerzas de la naturaleza comenzaron a extenderse, poderosas raíces desgarrando campos de cultivo.

Aremedia negoció un pacto con el mismísimo corazón del bosque. Al acordar respetar sus antiguos límites, detuvo la expansión.

Desde entonces, una delicada paz ha reinado entre An\'Ramoda y lo salvaje.

---

### Moroes el Amante
*Un Mito de Moroes y Morphia*

![Moroes, Dios de la Forja](../img/artwork-moroes.webp){ .wiki-portrait }

En lo más profundo del Señor de Carbohyrr, mucho antes de que nadie ascendiera a la divinidad, un artesano llamado Moroes se enamoró de Morphia.

Regalo tras regalo, herramientas de poder, objetos de maravilla, los colocó a los pies de quienes se convertirían en dioses, el sonido de su yunque llevando el ritmo de los latidos de su corazón. Pidió la mano de Morphia a cambio, y se la prometieron.

Pero cuando se alcanzó la divinidad, la boda fue cancelada.

Hasta el fin de los días, el latido de su yunque es lo único que puede detener el dolor de su corazón roto.

---

### El Hilo de la Virtud
*Un Mito de Morphia*

Tras soportar el dolor de dejar atrás a un ser querido, y tras un largo período de aislamiento, Morphia emergió con una perspectiva renovada. Recorrió las tierras y creó el **Hilo de la Virtud**, un hilo divino imbuido de la esencia de sus experiencias.

Con él, fundó la **Academia de las Ondas Étereas y los Sueños**.

---

### La Belleza de su Vida
*Un Mito de Morphia y Leeve*

![Leeve, Diosa de la Belleza y la Naturaleza](../img/artwork-leeve.webp){ .wiki-portrait }

Con el corazón destrozado, la diosa Morphia se retiró a la soledad de la naturaleza, abandonando sus deberes divinos.

Uno de sus devotos paladines juró restaurar a Morphia a su antiguo esplendor. Con palabras amables y actos de bondad, fue sacando poco a poco a Morphia de su aislamiento.

Conmovida por esta revelación, Morphia otorgó a la paladina un don divino, elevándola a la divinidad. Se convirtió en **Leeve**, la diosa de la belleza y la naturaleza.

---

### La Última Erudita Perdida
*Un Mito de Leeve*

Aunque criada como paladín, la benevolente Leeve también dominaba lo arcano. Pasó la mayor parte de sus primeros años en los salones de la **Academia de Viajes Infinitos**, una institución hace tiempo olvidada.

Llegaron tiempos difíciles. Uno a uno, sus maestros desaparecieron.

Cuando desapareció el último de ellos, se volvió hacia la única en quien podía confiar: su amiga más cercana, Morphia.

---

### El Otorgador de lo Sagrado
*Un Mito de Moroes*

Antes de la divinidad, antes del corazón roto, la maestría artesanal de Moroes no tenía rival. Regalo tras regalo, los colocó a los pies de quienes se convertirían en dioses.

Cada uno fue hecho a cambio de algo. Cada uno fue hecho al ritmo de los latidos de su corazón.

Al final, recibió la divinidad y un corazón roto.

*Algunos dicen que aún está pagando el precio de ese trato.*
''')

# ── Legends EN ──
w(B + '/legends.md', '''---
description: Legends of Galluvinchia, tales of mortal heroes whose deeds outlasted them, from the founding of Lorda Gorda to the library beneath Lakobordo.
---

# Legends, Tales of Mortal Heroes

---

### The Founding of Lorda Gorda
*A Legend of Lumin Oldreekia*

![The Maneless King of Lorda Gorda, heir of Lumin\'s legacy](../img/character-maneless-king.webp){ .wiki-portrait }

[Lumin Oldreekia](../characters/lumin-oldreekia.md), the legendary leokin felinfolk, was the greatest hero his people had ever known. Before becoming their first king, he created the first felinfolk city, now called the Whisk of Lumin, along the southern coast as a bastion against sandstorms, pirates, and ghouls.

Centuries later, the Whisk of Lumin still stands.

---

### Alice Rockwool and the Cyclopean Construct
*A Chronicle from Below Lakobordo*

Traveling the depths beneath Lakobordo, amidst marble pillars and pale tourmaline dust, [Alice Rockwool](../characters/alice-rockwool.md) and her companions discovered a timeless library long lost to the world.

A cyclopean construct stood waiting for them. Before the battle could begin, Alice Rockwool stepped forward and said:

> *"Yield to the sword of your masters! Look upon it!"*

And the construct kneeled.

Whether this is history or a tall tale depends on who is doing the telling.
''')

# ── Legends ES ──
w(B + '/legends.es.md', '''---
description: Leyendas de Galluvinchia, hazañas de héroes mortales cuyas acciones los sobrevivieron, desde la fundación de Lorda Gorda hasta la biblioteca bajo Lakobordo.
---

# Leyendas, Hazañas de Héroes Mortales

---

### La Fundación de Lorda Gorda
*Una Leyenda de Lumin Oldreekia*

![El Rey sin Melena de Lorda Gorda, heredero del legado de Lumin](../img/character-maneless-king.webp){ .wiki-portrait }

[Lumin Oldreekia](../characters/lumin-oldreekia.md), el legendario leokin felicio, fue el mayor héroe que su pueblo había conocido jamás. Antes de convertirse en su primer rey, creó la primera ciudad felicia, ahora llamada el Whisk de Lumin, a lo largo de la costa sur, como bastión contra tormentas de arena, piratas y necrófagos.

Siglos después, el Whisk de Lumin sigue en pie.

---

### Alice Rockwool y el Autómata
*Una Crónica desde las Profundidades de Lakobordo*

Viajando por las profundidades bajo Lakobordo, entre pilares de mármol y pálido polvo de turmalina, [Alice Rockwool](../characters/alice-rockwool.md) y sus compañeros descubrieron una biblioteca atemporal perdida para el mundo.

Un autómata de inmensas proporciones los aguardaba. Antes de que la batalla pudiera comenzar, Alice Rockwool dio un paso al frente y dijo:

> *"¡Ríndete ante la espada de tus maestros! ¡Mírala!"*

Y el autómata se arrodilló.

Si esto es historia o una historia exagerada depende de quién lo cuente.
''')

# ── Folktales EN ──
w(B + '/folktales.md', '''---
description: Folktales of Galluvinchia, the stories common people tell, the moon that never moves, the sound of the anvil, and the wisdom hidden in old words.
---

# Folktales, What the Common Folk Say

---

### The Moon That Never Moves
*A Folktale of Galluvinchia*

The moon of Galluvinchia does not move. It hangs in the sky at the same point, night after night. Scholars have debated this for centuries and reached no conclusion.

The common folk have a simpler explanation: *it is watching.*

---

### The Sound of the Anvil
*A Folktale of the Ripple*

Those who spend too long attuned to the Ripple, or who listen too closely to magic, begin to hear something at the edge of perception. Not a voice exactly. More like a sound.

The clink of a hammer. The ring of an anvil.

Nobody forges in the open air of that sound. But something is shaping something, always, somewhere.
''')

# ── Folktales ES ──
w(B + '/folktales.es.md', '''---
description: Cuentos populares de Galluvinchia, las historias que cuenta el pueblo, la luna que nunca se mueve, el sonido del yunque, y la sabiduría escondida en las palabras antiguas.
---

# Cuentos Populares, Lo que Dice el Pueblo

---

### La Luna que Nunca Se Mueve
*Un Cuento Popular de Galluvinchia*

La luna de Galluvinchia no se mueve. Cuelga en el cielo en el mismo punto, noche tras noche. Los eruditos han debatido esto durante siglos sin llegar a ninguna conclusión.

El pueblo tiene una explicación más simple: *está observando.*

---

### El Sonido del Yunque
*Un Cuento Popular de la Reverberación*

Quienes pasan demasiado tiempo sintonizados con la Reverberación, o que escuchan demasiado de cerca la magia, comienzan a oír algo en el borde de la percepción. No exactamente una voz. Más bien un sonido.

El tintineo de un martillo. El repique de un yunque.

Nadie forja en el aire abierto de ese sonido. Pero algo está dando forma a algo, siempre, en algún lugar.
''')

print("Done tales.")
