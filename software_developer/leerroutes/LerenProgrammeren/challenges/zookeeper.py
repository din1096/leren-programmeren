girrafen = int(input('hoeveel girrafen zijn er'))
struisvogels= int(input('hoeveel girrafen zijn er'))
zebra = int(input('hoeveel zebras zijn er'))
girrafen_poten = 0
struisvogels_poten = 0
zebra_poten = 0

def bereken_poten(girrafen , struisvogel, zebra):
    berekening = print(f'{girrafen * girrafen_poten + struisvogels * struisvogels_poten + zebra * zebra_poten} poten')
    return berekening

print(bereken_poten(4,2,4))