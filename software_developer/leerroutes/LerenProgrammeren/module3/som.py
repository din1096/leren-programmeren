begingetal = 50
getal = 50
som = 50

while getal < 1000:
    getal += 1
    som += getal
    print(f'{begingetal} + {som} = {begingetal + som}')
    if som >= 1000:
        break