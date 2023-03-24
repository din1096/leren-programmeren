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
 
rond, niet_rond = 0, 0
for fruit in fruitmand:
    kleuren = fruit['color']
    if kleuren == vraag_kleur:
        if fruit['round']:
            rond += 1
        else:
            niet_rond += 1

if rond > niet_rond:
    print(f"Er zijn {rond} meer ronde vruchten dan niet ronde vruchten in de kleur {vraag_kleur}")
elif rond < niet_rond:
    print(f"Er zijn {rond} minder ronde vruchten dan niet ronde vruchten in de kleur {vraag_kleur}")
else:
    print(f"Er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {vraag_kleur}")