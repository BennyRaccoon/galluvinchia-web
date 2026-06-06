#!/usr/bin/env python3

def r(p):
    with open(p, encoding='utf-8') as f: return f.read()

def w(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

def fix(p, old, new):
    c = r(p)
    if old in c and new not in c:
        w(p, c.replace(old, new, 1))
        print(f'  fixed: {p.split("/")[-1]}')

C  = 'wiki-docs/characters/'
LP = 'wiki-docs/gods/lesser-powers/'
RC = 'wiki-docs/regions/cities/'
RP = 'wiki-docs/regions/points-of-interest/'
T  = 'wiki-docs/tales/'

print('-- personajes --')
# armada.es.md
fix(C+'armada.es.md', 'elegido personalmente por la diosa Aremedia.', 'elegido personalmente por la diosa [Aremedia](../gods/aremedia.md).')
fix(C+'armada.es.md', 'Junto a Lewis Pendeltag y Martin Goldberg', 'Junto a [Lewis Pendeltag](lewis-pendeltag.md) y [Martin Goldberg](martin-goldberg.md)')

# fernando-oldreekia.es.md
fix(C+'fernando-oldreekia.es.md', 'Dirigida por la Magistrada Monica Mars; poder creciente', 'Dirigida por la [Magistrada Monica Mars](monica-mars.md); poder creciente')
fix(C+'fernando-oldreekia.es.md', 'el poder en la Dama de Mármaros desde', 'el poder en la [Dama de Mármaros](../regions/cities/lady-of-marmaros.md) desde')

# lewis-pendeltag.es.md
fix(C+'lewis-pendeltag.es.md', 'elegidos por la propia Aremedia.', 'elegidos por la propia [Aremedia](../gods/aremedia.md).')
fix(C+'lewis-pendeltag.es.md', "del gobierno de An'Ramoda.", "del gobierno de [An'Ramoda](../regions/cities/anramoda.md).")

# martin-goldberg.es.md
fix(C+'martin-goldberg.es.md', 'cónsules elegidos por la diosa.', 'cónsules elegidos por la diosa [Aremedia](../gods/aremedia.md).')
fix(C+'martin-goldberg.es.md', "motor económico de An'Ramoda.", "motor económico de [An'Ramoda](../regions/cities/anramoda.md).")

# maneless-king.es.md
fix(C+'maneless-king.es.md', 'Lorda Gorda está gobernada por una asamblea', '[Lorda Gorda](../regions/cities/lorda-gorda.md) está gobernada por una asamblea')
fix(C+'maneless-king.es.md', 'Los cristales que iluminan las calles de Lorda Gorda', 'Los cristales que iluminan las calles de [Lorda Gorda](../regions/cities/lorda-gorda.md)')

# monica-mars.es.md
fix(C+'monica-mars.es.md', 'en todas las ciudades.', 'en todas las ciudades.')  # skip, already ok
fix(C+'monica-mars.es.md', 'más poderosas de Mármaros.', 'más poderosas de [Mármaros](../regions/cities/lady-of-marmaros.md).')

# raquel.es.md
fix(C+'raquel.es.md', 'vinculada al Señor de Carbohyrr.', 'vinculada al [Señor de Carbohyrr](../regions/cities/lord-of-carbohyrr.md).')
fix(C+'raquel.es.md', 'Mago-Guerreros de Carbohyrr,', 'Mago-Guerreros de [Carbohyrr](../regions/cities/lord-of-carbohyrr.md),')

# salgu.es.md
fix(C+'salgu.es.md', "Salgu construyó An'Ramoda como", "Salgu construyó [An'Ramoda](../regions/cities/anramoda.md) como")

# agustin.es.md
fix(C+'agustin.es.md', 'Famoso en todo Lakobordo por', 'Famoso en todo [Lakobordo](../regions/villages/lakobordo.md) por')
fix(C+'agustin.es.md', 'herrero de Lakobordo haya', 'herrero de [Lakobordo](../regions/villages/lakobordo.md) haya')

# alice-rockwool.es.md
fix(C+'alice-rockwool.es.md', 'profundidades bajo Lakobordo,', 'profundidades bajo [Lakobordo](../regions/villages/lakobordo.md),')

# merrion-meyer.es.md
fix(C+'merrion-meyer.es.md', 'Sueños en Doormi.', 'Sueños en [Doormi](../regions/villages/doormi.md).')
fix(C+'merrion-meyer.es.md', 'accesible en Doormi', 'accesible en [Doormi](../regions/villages/doormi.md)')

# lumin-oldreekia.es.md
fix(C+'lumin-oldreekia.es.md', 'primer rey de Lorda Gorda. Siglos después, el Whisk de Lumin', 'primer rey de [Lorda Gorda](../regions/cities/lorda-gorda.md). Siglos después, el [Whisk de Lumin](../regions/villages/whisk-of-lumin.md)')

# silvino.es.md
fix(C+'silvino.es.md', 'que [Panos](../gods/panos.md) cree', 'que [Panos](../gods/panos.md) cree')  # already linked

# kogarashi.es.md
fix(C+'kogarashi.es.md', 'que [Panos](../gods/panos.md) triunfó', 'que [Panos](../gods/panos.md) triunfó')  # already linked

print('-- poderes menores --')
fix(LP+'the-light.es.md', 'Los felicios de Lorda Gorda rezan', 'Los felicios de [Lorda Gorda](../../regions/cities/lorda-gorda.md) rezan')

fix(LP+'will-of-the-wild.es.md', "An'Ramoda continúa expandiéndose", "[An'Ramoda](../../regions/cities/anramoda.md) continúa expandiéndose")

fix(LP+'lady-of-horns.es.md', 'bajo el Señor de Carbohyrr,', 'bajo el [Señor de Carbohyrr](../../regions/cities/lord-of-carbohyrr.md),')
fix(LP+'lady-of-horns.es.md', 'profundidades bajo el [Señor de Carbohyrr](../../regions/cities/lord-of-carbohyrr.md), la voz que enloqueció a [Moroes](../moroes.md)', 'profundidades bajo el [Señor de Carbohyrr](../../regions/cities/lord-of-carbohyrr.md), la voz que enloqueció a [Moroes](../moroes.md)')  # already ok after above

fix(LP+'dragons.es.md', 'de la Dama de Mármaros:', 'de la [Dama de Mármaros](../../regions/cities/lady-of-marmaros.md):')

print('-- ciudades --')
fix(RC+'anramoda.es.md', 'Construida como santuario por Salgu,', 'Construida como santuario por [Salgu](../../characters/salgu.md),')
fix(RC+'anramoda.es.md', '| **Aremedia** | Poder supremo', '| **[Aremedia](../../gods/aremedia.md)** | Poder supremo')
fix(RC+'anramoda.es.md', 'aprobación de Aremedia |', 'aprobación de [Aremedia](../../gods/aremedia.md) |')

print('-- POI --')
fix(RP+'aurora-densasilva.es.md', "An'Ramoda continúa expandiéndose hacia el este", "[An'Ramoda](../cities/anramoda.md) continúa expandiéndose hacia el este")
fix(RP+'ice-peak.es.md', '[Aremedia](../../gods/aremedia.md) actuó', '[Aremedia](../../gods/aremedia.md) actuó')  # already linked

print('-- relatos --')
# myths.es.md
fix(T+'myths.es.md', "que ilumina An'Ramoda.", "que ilumina [An'Ramoda](../regions/cities/anramoda.md).")
fix(T+'myths.es.md', 'Con la ayuda de Aremedia, la tribu', 'Con la ayuda de [Aremedia](../gods/aremedia.md), la tribu')
fix(T+'myths.es.md', "en armonía en An'Ramoda. Pero", "en armonía en [An'Ramoda](../regions/cities/anramoda.md). Pero")
fix(T+'myths.es.md', 'En lo más profundo del Señor de Carbohyrr,', 'En lo más profundo del [Señor de Carbohyrr](../regions/cities/lord-of-carbohyrr.md),')
fix(T+'myths.es.md', 'fundó la **Academia de las Ondas Étereas y los Sueños**', 'fundó la **[Academia de las Ondas Étereas y los Sueños](../regions/villages/doormi.md)**')
fix(T+'myths.es.md', 'Se convirtió en **Leeve**, la diosa de la belleza', 'Se convirtió en **[Leeve](../gods/leeve.md)**, la diosa de la belleza')

# legends.es.md
fix(T+'legends.es.md', 'profundidades bajo Lakobordo,', 'profundidades bajo [Lakobordo](../regions/villages/lakobordo.md),')

print('Listo.')
