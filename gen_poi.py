#!/usr/bin/env python3
import os

B = "wiki-docs/regions/points-of-interest"
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
description: Notable locations of Galluvinchia, Ice Peak, Aurora Densasilva, Ourobolis, the Mist, and the academies that shaped the world\'s magic.
---

# Points of Interest

Galluvinchia is vast, and much of it remains unexplored. These known places have drawn adventurers, scholars, and fools for generations.

<div class="grid cards" markdown>

-   **[Ice Peak](ice-peak.md)**

    ---

    The frozen northern stronghold of the giants, who have not forgotten their exile from An\'Ramoda.

-   **[Aurora Densasilva](aurora-densasilva.md)**

    ---

    The eternal forest at the heart of Galluvinchia, alive in ways no other forest is.

-   **[Breath of Sand](breath-of-sand.md)**

    ---

    The eastern desert where a jungle once grew, hiding ancient ruins and the last oasis.

-   **[Ourobolis](ourobolis.md)**

    ---

    The purple-sea island where the tainted tribe venerates the fallen serpent Aolosh.

-   **[The Mist](the-mist.md)**

    ---

    The permanent mist at the edge of the world, from which the elves came, or to which they retreated.

-   **[The Academies](academies.md)**

    ---

    Three institutions that shaped magic in Galluvinchia: one thriving, one humble, one lost to time.

</div>
''')

# ── Index ES ──
w(B + '/index.es.md', '''---
description: Lugares notables de Galluvinchia, Puntahelada, Aurora Densasilva, Ourobolis, la Bruma y las academias que moldearon la magia del mundo.
---

# Puntos de Interés

Galluvinchia es vasta, y gran parte de ella permanece inexplorada. Estos lugares conocidos han atraído a aventureros, eruditos e insensatos durante generaciones.

<div class="grid cards" markdown>

-   **[Puntahelada](ice-peak.md)**

    ---

    La gélida fortaleza norteña de los gigantes, que no han olvidado su exilio de An\'Ramoda.

-   **[Aurora Densasilva](aurora-densasilva.md)**

    ---

    El bosque eterno en el corazón de Galluvinchia, vivo de maneras que ningún otro bosque lo está.

-   **[El Suspiro de Arena](breath-of-sand.md)**

    ---

    El desierto oriental donde antaño crecía una jungla, que esconde ruinas antiguas y el último oasis.

-   **[Ourobolis](ourobolis.md)**

    ---

    La isla del mar púrpura donde la tribu corrupta venera a la serpiente caída Aolosh.

-   **[La Bruma](the-mist.md)**

    ---

    La bruma permanente al borde del mundo, de donde vinieron los elfos, o a donde se retiraron.

-   **[Las Academias](academies.md)**

    ---

    Tres instituciones que moldearon la magia en Galluvinchia: una próspera, una humilde, una perdida en el tiempo.

</div>
''')

# ── Individual POI pages ──

w(B + '/ice-peak.md', page(
    'Ice Peak',
    'Ice Peak, the hidden northern stronghold of the giants who were exiled from An\'Ramoda and have not forgotten.',
    box(None, 'Ice Peak', 'Stronghold of the Giants · The Frozen North',
        [('Location', 'Far north of Galluvinchia'), ('Inhabitants', 'Giants'), ('Danger', 'Extreme')]),
    '''In the furthest reaches of the north, behind hungry winters and mountains sharp as blades, lies Ice Peak, the hidden stronghold of the giants. Even in the current era of the *Pax Aremedia*, armed warriors are regularly lost attempting to reach this place and put limits on the giants\' violent raids.

Long ago, the giants lived harmoniously in An\'Ramoda. Then a choleric madness began to spread among them, an uncontrollable rage that threatened the city. [Aremedia](../../gods/aremedia.md) acted decisively: she exiled all the giants to the far north, where her influence wanes.

*The giants have not forgotten.*
'''))

w(B + '/ice-peak.es.md', page(
    'Puntahelada',
    'Puntahelada, la fortaleza oculta de los gigantes exiliados de An\'Ramoda, que no han olvidado lo que les hicieron.',
    box(None, 'Puntahelada', 'Morada de los Gigantes · El Norte Helado',
        [('Ubicación', 'Extremo norte de Galluvinchia'), ('Habitantes', 'Gigantes'), ('Peligro', 'Extremo')]),
    '''En los confines más septentrionales de Galluvinchia, tras hambrientos inviernos y montañas afiladas como cuchillas, se encuentra Puntahelada, la fortaleza oculta de los gigantes. Incluso en la actual era de la *Pax Aremedia*, guerreros armados se pierden regularmente intentando llegar aquí.

Hace mucho tiempo, los gigantes vivían en armonía en An\'Ramoda. Luego una colérica locura comenzó a apoderarse de ellos. [Aremedia](../../gods/aremedia.md) los desterró al extremo norte.

*No lo han olvidado.*
'''))

w(B + '/aurora-densasilva.md', page(
    'Aurora Densasilva',
    'Aurora Densasilva, the eternal forest at the heart of Galluvinchia, alive in ways no other forest is, its roots remembering the First Age.',
    box('artwork-queen-of-branches.webp', 'Aurora Densasilva', 'The Eternal Forest · The Twisted Wood',
        [('Location', 'Heart of Galluvinchia'), ('Ruler', 'The Queen of Branches · Will of the Wild'),
         ('Access', 'Friends of the forest only'), ('Danger', 'High for the unwelcome')]),
    '''At the heart of Galluvinchia spreads Aurora Densasilva, the perpetual, impenetrable, ancient forest. It is alive in ways that no other forest is: its roots remember the First Age, and its branches carry grudges.

Within its twisted roots lives a civilization, not numerous, but rich in spirituality, protected by the **Will of the Wild**. Only friends of the forest are welcome here. Treasure hunters and explorers are turned away, lost, or never seen again.

!!! quote ""
    *"Its hunger makes it grow without end. Political agreements, promises, are rarely kept by its inhabitants."*

The forest is directed, in grave matters, by the **Queen of Branches**, a herald of the Will of the Wild itself.

An\'Ramoda continues to expand eastward into the forest, and the forest burns with resentment.
'''))

w(B + '/aurora-densasilva.es.md', page(
    'Aurora Densasilva',
    'Aurora Densasilva, el bosque eterno en el corazón de Galluvinchia, vivo de maneras que ningún otro bosque lo está, con raíces que recuerdan la Primera Era.',
    box('artwork-queen-of-branches.webp', 'Aurora Densasilva', 'El Bosque Eterno · El Bosque Retorcido',
        [('Ubicación', 'Corazón de Galluvinchia'), ('Gobernante', 'La Reina de las Ramas · Voluntad de lo Salvaje'),
         ('Acceso', 'Solo amigos del bosque'), ('Peligro', 'Alto para los no bienvenidos')]),
    '''En el corazón de Galluvinchia se extiende Aurora Densasilva, el bosque perpetuo, impenetrable, antiguo. Se dice que está vivo de maneras que ningún otro bosque lo está: sus raíces recuerdan la Primera Era y sus ramas guardan rencores.

En el interior de sus retorcidas raíces vive una civilización, protegida por la **Voluntad de lo Salvaje**. Solo los amigos del bosque son bienvenidos. Los cazadores de tesoros y exploradores son rechazados, perdidos o jamás vistos de nuevo.

!!! quote ""
    *"Su hambre lo hace crecer sin fin. Los acuerdos políticos, las promesas, raramente son cumplidos por sus habitantes."*

El bosque está dirigido, en asuntos graves, por la **Reina de las Ramas**, un heraldo de la propia Voluntad de lo Salvaje.
'''))

w(B + '/breath-of-sand.md', page(
    'Breath of Sand',
    'The Breath of Sand, the eastern desert where a jungle once grew, hiding ancient ruins and the last surviving oasis.',
    box(None, 'Breath of Sand', 'The Eastern Desert · The Last Oasis',
        [('Location', 'East of Lord of Carbohyrr'), ('Former state', 'Jungle'), ('Inhabitants', 'Horangi family · Ruins')]),
    '''East of the Lord of Carbohyrr, where a jungle once stood, stretches now an endless arid expanse: the Breath of Sand. Hidden within it is a small community living in the last green remnants, the last oasis, kept alive by the **Horangi family**, the last of an ancient felinfolk lineage with deep and mysterious connections to the land.

Ancient ruins dot the desert. What they once were, cities, temples, academies, is mostly forgotten. Their stones remember things no living person knows.
'''))

w(B + '/breath-of-sand.es.md', page(
    'El Suspiro de Arena',
    'El Suspiro de Arena, el desierto oriental donde antaño creció una jungla, que esconde ruinas antiguas y el último oasis superviviente.',
    box(None, 'El Suspiro de Arena', 'El Desierto del Este · El Último Oasis',
        [('Ubicación', 'Al este del Señor de Carbohyrr'), ('Estado anterior', 'Jungla'), ('Habitantes', 'Familia Horangi · Ruinas')]),
    '''Al este del Señor de Carbohyrr, donde antaño se alzaba una jungla, se extiende ahora una interminable extensión árida: el Suspiro de Arena. Escondida en su interior hay una pequeña comunidad que vive en los últimos vestigios verdes, el último oasis, mantenido vivo por la **familia Horangi**, la última de un linaje felicio antiguo con conexiones profundas y misteriosas con la tierra.

Ruinas antiguas salpican el desierto. Lo que fueron en su día, ciudades, templos, academias, está en su mayor parte olvidado.
'''))

w(B + '/ourobolis.md', page(
    'Ourobolis',
    'Ourobolis, the island where the sea turned purple when the serpent Aolosh fell, home of the tribe that still venerates her.',
    box('artwork-abyss-walker.webp', 'Ourobolis', 'The Purple Sea · Where the Serpent Fell',
        [('Location', 'Far northeast, island'), ('Inhabitants', 'Tainted tribe'), ('Deity', 'Aolosh (fallen)'),
         ('Danger', 'Extreme · Extreme rituals')]),
    '''Far to the northeast, the sea around this island turned purple when the primordial serpent **Aolosh** was vanquished by the gods in ascent. The island is home to a tribe that still venerates the fallen serpent, their rituals the most extreme in all of Galluvinchia, fueled by the tainted blood of their fallen patron.

[Brenadette](../../gods/brenadette.md) watches this place with particular concern.

The tribe descended into madness when Aolosh was defeated. Driven by fury and despair, they once ventured into the Neverender itself and waged a ferocious battle against Brenadette. With the aid of [Aremedia](../../gods/aremedia.md), they were defeated and banished back to their island.

They have not stopped.
'''))

w(B + '/ourobolis.es.md', page(
    'Ourobolis',
    'Ourobolis, la isla donde el mar se volvió púrpura cuando cayó la serpiente Aolosh, hogar de la tribu que aún la venera.',
    box('artwork-abyss-walker.webp', 'Ourobolis', 'El Mar Púrpura · Donde Cayó la Serpiente',
        [('Ubicación', 'Noreste lejano, isla'), ('Habitantes', 'Tribu corrupta'), ('Deidad', 'Aolosh (caída)'),
         ('Peligro', 'Extremo · Rituales extremos')]),
    '''Lejos al noreste, el mar alrededor de esta isla se volvió púrpura cuando la serpiente primordial **Aolosh** fue vencida por los dioses en su ascenso. La isla es el hogar de una tribu que aún venera a la serpiente caída, con los rituales más extremos de toda Galluvinchia.

[Brenadette](../../gods/brenadette.md) observa este lugar con especial preocupación.

La tribu descendió a la locura cuando Aolosh fue derrotada. Impulsada por la furia, se adentró en el Rencarnatorno y libró una feroz batalla contra la propia Brenadette. Con la ayuda de [Aremedia](../../gods/aremedia.md), fueron derrotadas y desterradas de vuelta a su isla.

No han parado.
'''))

w(B + '/the-mist.md', page(
    'The Mist',
    'The Mist, the permanent haze at the far eastern edge of the world, from which the elves came or to which they returned.',
    box(None, 'The Mist', 'Origin of the Elves · The Far East',
        [('Location', 'Far eastern edge of the known world'), ('Inhabitants', 'Elves (rarely seen)'),
         ('Nature', 'Ancient · Magical · Impassable')]),
    '''At the far eastern edge of the known world, a permanent mist spreads. From here the elves came, or more precisely, here they retreated. They are part of legend now, rarely seen in the rest of Galluvinchia.

The mist is described as a place of wonder and rapture, of shadow and magic. From outside, one can only hear the resonance of something ancient and powerful.

> *"The elves were here before any of us were even a thought."*
> Juan Passage

Beyond the mist lie the ruins of **Ozan Tizuki**, once the greatest elven civilization Galluvinchia had ever seen. What happened to it is a mystery that even the elves themselves no longer remember.
'''))

w(B + '/the-mist.es.md', page(
    'La Bruma',
    'La Bruma, la neblina permanente en el extremo oriental del mundo, de donde vinieron los elfos o a donde se retiraron.',
    box(None, 'La Bruma', 'Origen de los Elfos · El Extremo Oriente',
        [('Ubicación', 'Extremo oriental del mundo conocido'), ('Habitantes', 'Elfos (raramente vistos)'),
         ('Naturaleza', 'Antigua · Mágica · Impenetrable')]),
    '''En el borde oriental del mundo conocido, una bruma permanente se extiende. De aquí vinieron los elfos, o más bien, aquí se retiraron. Son parte de la leyenda ahora, raramente vistos en el resto de Galluvinchia.

Desde fuera solo se puede escuchar la resonancia de algo antiguo y poderoso.

> *"Los elfos estuvieron aquí antes de que ninguno de nosotros fuera siquiera un pensamiento."*
> Juan Passage

Más allá de la bruma se encuentran las ruinas de **Ozan Tizuki**, antaño la mayor civilización élfica que Galluvinchia había conocido. Lo que le ocurrió es un misterio que incluso los propios elfos ya no recuerdan.
'''))

w(B + '/academies.md', page(
    'The Academies',
    'The three academies that shaped magical education in Galluvinchia: the Academy of Magic Wonders, the Academy of Magic Waves and Dreams, and the lost Academy of Infinite Travels.',
    box(None, 'The Academies', 'Three Institutions · Three Fates',
        [('Active', 'Academy of Magic Wonders · Academy of Magic Waves and Dreams'),
         ('Lost', 'Academy of Infinite Travels')]),
    '''Three academies have shaped the magical landscape of Galluvinchia, one in all its splendor, one thriving humbly, and one lost already to time.

## Academy of Magic Wonders

Located in the [Lady of Marmaros](../cities/lady-of-marmaros.md), the most exclusive scholarship in Galluvinchia. Presided over by [Magister Monica Mars](../../characters/monica-mars.md), it trains multidisciplinary mages considered among the brightest minds in the world. Its branded products — potions, magical garments, enchanted cosmetics — are sold across the continent.

## Academy of Magic Waves and Dreams

On the cliffs of [Doormi](../villages/doormi.md), this academy is more humble in focus but more generous in access. Led by [Merrion Meyer](../../characters/merrion-meyer.md), it offers the first year of study free to the most brilliant students. Its specialty lies in the **Loom of Dreams** and the craft of magical garments. Founded following the creation of the **Thread of Virtue** by [Morphia](../../gods/morphia.md).

## Academy of Infinite Travels *(Ruins)*

In the Gulf of Febris lie the ruins of a once-grand academy, long forgotten and occasionally used as a hideout. The memories of ancient spells are said to persist in its stones. What was studied here, and what happened to its scholars, is mostly lost.

[Leeve](../../gods/leeve.md) spent the early years of her mortal life in its halls. When the last of her teachers vanished, she turned to Morphia.
'''))

w(B + '/academies.es.md', page(
    'Las Academias',
    'Las tres academias que moldearon la educación mágica en Galluvinchia: la de Magias Maravillosas, la de las Ondas Étereas y los Sueños, y la perdida Academia de Viajes Infinitos.',
    box(None, 'Las Academias', 'Tres Instituciones · Tres Destinos',
        [('Activas', 'Academia de Magias Maravillosas · Academia de las Ondas Étereas y los Sueños'),
         ('Perdida', 'Academia de Viajes Infinitos')]),
    '''Tres academias han dado forma al paisaje mágico de Galluvinchia, una en todo su esplendor, una que prospera con humildad y una perdida ya en el tiempo.

## Academia de Magias Maravillosas

Situada en la [Dama de Mármaros](../cities/lady-of-marmaros.md), la beca más exclusiva de Galluvinchia. Presidida por la [Magistrada Monica Mars](../../characters/monica-mars.md), forma a magos multidisciplinares considerados entre las mentes más brillantes del mundo.

## Academia de las Ondas Étereas y los Sueños

En los acantilados de [Doormi](../villages/doormi.md), esta academia es más humilde pero más generosa en acceso. Dirigida por [Merrion Meyer](../../characters/merrion-meyer.md), ofrece el primer año de estudio gratuito. Su especialidad es el **Telar de los Sueños** y la confección de prendas mágicas.

## Academia de Viajes Infinitos *(Ruinas)*

En el Golfo de Febris se encuentran las ruinas de una academia en su día grandiosa, hace tiempo olvidada. Los recuerdos de antiguos conjuros se dice que persisten en sus piedras.

[Leeve](../../gods/leeve.md) pasó los primeros años de su vida mortal en sus salas.
'''))

print("Done POIs.")
