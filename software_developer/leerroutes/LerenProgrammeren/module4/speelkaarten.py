import random
vormen = ['harten','klaveren','schoppen','ruiten']
kaarten = ['twee','drie','vier','vijf','zes','zeven','acht','negen','tien','boer','vrouw','heer','aas']
deck = ['joker','joker']

for vorm in vormen:
    for kaart in kaarten:
        nieuwe_kaarten =vorm + kaart
        deck.append(nieuwe_kaarten)
random.shuffle(deck)
for x in range(1,8):
    
    shuffle = random.choice(deck)
    deck.remove(shuffle)
    print(shuffle)
print(f'deck (47 kaarten):{deck}')