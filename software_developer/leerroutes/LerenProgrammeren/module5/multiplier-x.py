getal = int(input('van welk getal wil je de tafel zien?'))

def tafel(getal):
    for x in range(1,11):
        som = x * getal
        print(f'{x} x {getal} = {som}')


tafel(getal)
