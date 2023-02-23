import random   
MnM = ("oranje m&m","blauw m&m","groen m&m","bruin m&m")
vraag = int(input('hoeveel m&m moeten toegevoeged worden aan de zak'))
zak_mnm = []

for x in range(vraag):
    zak = random.choice(MnM)
    zak_mnm.append(zak)

print(zak_mnm)

