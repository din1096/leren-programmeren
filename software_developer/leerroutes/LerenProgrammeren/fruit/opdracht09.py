from fruitmand import fruitmand
kleur = []
for fruit in fruitmand:
    if fruit ['name'] == 'druif':
        fruitmand.remove(fruit)
for fruit in fruitmand:
    if fruit['color'] not in kleur:
        kleur.append(fruit["color"])
        print(",".join(kleur))