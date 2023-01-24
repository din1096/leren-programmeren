import random   
MnM = ("oranje mnm","blauw mnm","groen mnm","bruin mnm")
vraag = int(input('hoeveel m&m moeten toegevoeged worden aan de zak'))
zak_mnm = []

for x in range(vraag):
    zak = random.choice(MnM)
    zak_mnm.append(zak)

print(zak_mnm)