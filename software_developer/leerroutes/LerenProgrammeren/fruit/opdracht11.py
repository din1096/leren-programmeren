from fruitmand import fruitmand

kleuren = []

for fruit in fruitmand :
    if not fruit["color"] in kleuren:
        kleuren.append(fruit["color"])
prompt = ""
for kleur in kleuren :
    prompt += kleur+", "
print(prompt)

while True:
    vraag_kleur = input("Kies een kleur uit. ")
    if vraag_kleur in kleuren:
        break
    else:
        print(f"De kleur {vraag_kleur} zit er niet in de fruitmand.")
 
rond, nietRond = 0, 0
for fruit in fruitmand:
    kleuren = fruit['color']
    if kleuren == vraag_kleur:
        if fruit['round']:
            rond += 1
        else:
            nietRond += 1

if rond > nietRond:
    print(f"Er zijn {rond} meer ronde vruchten dan niet ronde vruchten in de kleur {vraag_kleur}")
elif rond < nietRond:
    print(f"Er zijn {rond} minder ronde vruchten dan niet ronde vruchten in de kleur {vraag_kleur}")
else:
    print(f"Er zijn {rond} ronde vruchten en {nietRond} niet ronde vruchten in de kleur {vraag_kleur}")