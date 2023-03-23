import random
vormen = ['harten','klaveren','schoppen','ruiten']
kaarten = ['twee','drie','vier','vijf','zes','zeven','acht','negen','tien','boer','vrouw','heer','aas']
deck = ['joker','joker']

for vorm in vormen:
    for kaart in kaarten:
        nieuwe_kaarten =(f'{vorm} {kaart}')
        deck.append(nieuwe_kaarten)

random.shuffle(deck)
print(deck)
for i in range(len(deck)):
  print(f'{deck[i]}')
  if i == 6:
    del deck[0:7]
    break

print(deck)