getal_1 = int(input('voer een getal in'))
getal_2 = int(input('voer een getal in'))

def compare_cijfer(getal_1,getal_2):
    if getal_1 > getal_2:
        print(f'{getal_1} is groter dan {getal_2}')
    elif getal_1 < getal_2:
        print(f'{getal_1} is kleiner dan {getal_2}')
    else:
        print(f'{getal_1} en {getal_1} zijn even groot')

compare_cijfer(getal_1,getal_2)