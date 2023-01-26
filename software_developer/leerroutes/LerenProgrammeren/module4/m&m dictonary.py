from random import randint
MnM = ["rood","blauw","groen","geel","bruin"]
hoeveel = int(input('hoeveel m&m moeten toegevoeged worden aan de zak'))
zak_mnm = {}

for x in range(hoeveel):
    verschil = randint(0,4)
    randomkleur = MnM[verschil]
    if MnM[verschil] not in zak_mnm:
        zak_mnm.update({randomkleur : 1})
    else:
        x = zak_mnm.get(MnM[verschil]) +1
        zak_mnm.update({MnM[verschil]:x})
print(zak_mnm)




