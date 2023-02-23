from random import randint
MnM = ["rood","blauw","groen","geel","bruin"]
hoeveel = int(input('hoeveel m&m moeten toegevoeged worden aan de zak'))
zak_mnm = {}

for x in range(hoeveel):
    verschil = randint(0,4)
    randomkleur = MnM[verschil]
    if MnM[verschil] not in zak_mnm:
        zak_mnm.update({randomkleur : 1})

print(zak_mnm)
