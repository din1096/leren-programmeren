from fruitmand import fruitmand 
import random
aantal = int(input('type een hoeveelhijd in'))
fruit = []
for x in range(aantal):
    fruitjes = random.choice(fruitmand)
    fruitmand.remove(fruitjes)
    fruit.append(fruitjes)

print(fruit)