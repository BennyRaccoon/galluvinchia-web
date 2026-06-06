#!/usr/bin/env python3
import os

def r(p):
    with open(p, encoding='utf-8') as f: return f.read()

def w(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

def fix(p, old, new):
    c = r(p)
    if old in c and new not in c:
        w(p, c.replace(old, new, 1))
        print(f'  fixed: {p.split("/")[-1]}')

C = 'wiki-docs/characters/'
G = 'wiki-docs/gods/'
LP = 'wiki-docs/gods/lesser-powers/'
RC = 'wiki-docs/regions/cities/'
RV = 'wiki-docs/regions/villages/'
RP = 'wiki-docs/regions/points-of-interest/'
T  = 'wiki-docs/tales/'

print('-- characters --')
# armada.md
fix(C+'armada.md', 'goddess Aremedia.', 'goddess [Aremedia](../gods/aremedia.md).')
fix(C+'armada.md', 'Alongside Lewis Pendeltag and Martin Goldberg', 'Alongside [Lewis Pendeltag](lewis-pendeltag.md) and [Martin Goldberg](martin-goldberg.md)')

# fernando-oldreekia.md
fix(C+'fernando-oldreekia.md', 'Led by Magister Monica Mars;', 'Led by [Magister Monica Mars](monica-mars.md);')
fix(C+'fernando-oldreekia.md', "power in the Lady of Marmaros since", "power in the [Lady of Marmaros](../regions/cities/lady-of-marmaros.md) since")

# lewis-pendeltag.md
fix(C+'lewis-pendeltag.md', 'chosen by Aremedia herself.', 'chosen by [Aremedia](../gods/aremedia.md) herself.')
fix(C+'lewis-pendeltag.md', "An'Ramoda's government.", "[An'Ramoda](../regions/cities/anramoda.md)'s government.")

# martin-goldberg.md
fix(C+'martin-goldberg.md', "third of the goddess's chosen consuls.", "third of the goddess [Aremedia](../gods/aremedia.md)'s chosen consuls.")
fix(C+'martin-goldberg.md', "engine of An'Ramoda.", "engine of [An'Ramoda](../regions/cities/anramoda.md).")

# maneless-king.md
fix(C+'maneless-king.md', 'Lorda Gorda is governed by an assembly', '[Lorda Gorda](../regions/cities/lorda-gorda.md) is governed by an assembly')
fix(C+'maneless-king.md', "crystals that light Lorda Gorda's streets", "crystals that light [Lorda Gorda](../regions/cities/lorda-gorda.md)'s streets")

# monica-mars.md
fix(C+'monica-mars.md', "One of the most skilled", "One of the most skilled")  # skip, already ok
fix(C+'monica-mars.md', "in the Lady of Marmaros.", "in the [Lady of Marmaros](../regions/cities/lady-of-marmaros.md).")
fix(C+'monica-mars.md', "most powerful people in Marmaros.", "most powerful people in [Marmaros](../regions/cities/lady-of-marmaros.md).")

# raquel.md
fix(C+'raquel.md', "connected to the Lord of Carbohyrr.", "connected to the [Lord of Carbohyrr](../regions/cities/lord-of-carbohyrr.md).")
fix(C+'raquel.md', "battlemages of Carbohyrr,", "battlemages of [Carbohyrr](../regions/cities/lord-of-carbohyrr.md),")

# salgu.md
fix(C+'salgu.md', "Salgu built the city of An'Ramoda", "Salgu built the city of [An'Ramoda](../regions/cities/anramoda.md)")
fix(C+'salgu.md', "memory is revered in An'Ramoda,", "memory is revered in [An'Ramoda](../regions/cities/anramoda.md),")

# agustin.md
fix(C+'agustin.md', 'Famous throughout Lakobordo for', 'Famous throughout [Lakobordo](../regions/villages/lakobordo.md) for')
fix(C+'agustin.md', 'smith in Lakobordo has', 'smith in [Lakobordo](../regions/villages/lakobordo.md) has')

# alice-rockwool.md
fix(C+'alice-rockwool.md', 'depths beneath Lakobordo,', 'depths beneath [Lakobordo](../regions/villages/lakobordo.md),')

# merrion-meyer.md
fix(C+'merrion-meyer.md', 'Dreams at Doormi.', 'Dreams at [Doormi](../regions/villages/doormi.md).')
fix(C+'merrion-meyer.md', 'magic more accessible in Doormi', 'magic more accessible in [Doormi](../regions/villages/doormi.md)')

# lumin-oldreekia.md
fix(C+'lumin-oldreekia.md', 'first king of Lorda Gorda. Centuries later, the Whisk of Lumin', 'first king of [Lorda Gorda](../regions/cities/lorda-gorda.md). Centuries later, the [Whisk of Lumin](../regions/villages/whisk-of-lumin.md)')

# silvino.md — second Panos mention
fix(C+'silvino.md', 'objects that Panos believes', 'objects that [Panos](../gods/panos.md) believes')

# kogarashi.md — Ancho Groncho (no dedicated page, skip), but An'Ramoda mention
fix(C+'kogarashi.md', "An'Ramoda has directed multiple assaults", "[An'Ramoda](../regions/cities/anramoda.md) has directed multiple assaults")

print('-- lesser powers --')
fix(LP+'the-light.md', 'The felinfolk of Lorda Gorda pray', 'The felinfolk of [Lorda Gorda](../../regions/cities/lorda-gorda.md) pray')

fix(LP+'will-of-the-wild.md', "An'Ramoda continues to expand", "[An'Ramoda](../../regions/cities/anramoda.md) continues to expand")
fix(LP+'will-of-the-wild.md', 'pact that [Aremedia](../aremedia.md) brokered', 'pact that [Aremedia](../aremedia.md) brokered')  # already linked, skip

fix(LP+'lady-of-horns.md', 'Deep below the Lord of Carbohyrr,', 'Deep below the [Lord of Carbohyrr](../../regions/cities/lord-of-carbohyrr.md),')

fix(LP+'dragons.md', 'from the Lady of Marmaros:', 'from the [Lady of Marmaros](../../regions/cities/lady-of-marmaros.md):')

print('-- cities --')
fix(RC+'anramoda.md', 'Built as a sanctuary by Salgu,', 'Built as a sanctuary by [Salgu](../../characters/salgu.md),')
fix(RC+'anramoda.md', '| **Aremedia** | Ultimate power', '| **[Aremedia](../../gods/aremedia.md)** | Ultimate power')
fix(RC+'anramoda.md', "Aremedia's approval |", "[Aremedia](../../gods/aremedia.md)'s approval |")

fix(RC+'lord-of-carbohyrr.md', 'crafted by the Battlemages,', 'crafted by the Battlemages,')  # skip, no dedicated page

print('-- POI --')
fix(RP+'aurora-densasilva.md', "An'Ramoda continues to expand eastward", "[An'Ramoda](../cities/anramoda.md) continues to expand eastward")

fix(RP+'ourobolis.md', 'With the aid of [Aremedia](../../gods/aremedia.md)', 'With the aid of [Aremedia](../../gods/aremedia.md)')  # already linked
fix(RP+'ice-peak.md', '[Aremedia](../../gods/aremedia.md) acted decisively', '[Aremedia](../../gods/aremedia.md) acted decisively')  # already linked

fix(RP+'academies.md', 'following the creation of the **Thread of Virtue** by [Morphia](../../gods/morphia.md)', 'following the creation of the **Thread of Virtue** by [Morphia](../../gods/morphia.md)')  # already linked

print('-- tales --')
# myths.md - link gods on first substantive body mention per section
fix(T+'myths.md', 'the city of An\'Ramoda.', "the city of [An'Ramoda](../regions/cities/anramoda.md).")
fix(T+'myths.md', 'With the aid of Aremedia, the tribe', 'With the aid of [Aremedia](../gods/aremedia.md), the tribe')
fix(T+'myths.md', 'Long ago, the giants lived harmoniously in An\'Ramoda,', "Long ago, the giants lived harmoniously in [An'Ramoda](../regions/cities/anramoda.md),")
fix(T+'myths.md', "She exiled the giants from An'Ramoda and banished", "She exiled the giants from An'Ramoda and banished")  # skip second mention
fix(T+'myths.md', 'Deep in the Lord of Carbohyrr,', 'Deep in the [Lord of Carbohyrr](../regions/cities/lord-of-carbohyrr.md),')
fix(T+'myths.md', 'she founded the **Academy of Magic Waves and Dreams**', 'she founded the **[Academy of Magic Waves and Dreams](../regions/villages/doormi.md)**')
fix(T+'myths.md', 'the paladin became **Leeve**, goddess of beauty', 'the paladin became **[Leeve](../gods/leeve.md)**, goddess of beauty')

# legends.md - Lakobordo mention
fix(T+'legends.md', 'below Lakobordo,', 'below [Lakobordo](../regions/villages/lakobordo.md),')

print('Done.')
