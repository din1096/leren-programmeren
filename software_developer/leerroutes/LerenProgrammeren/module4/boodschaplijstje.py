boodschappen_lijst = {}
lijst = True
while lijst:
    boodschappen = input('wat wil je als boodschappen').lower()
    hoeveel = input('hoeveel wil je ervan')
    toevoegen = input('wil je nog wat toevoegen')
    boodschappen_lijst.update({boodschappen : hoeveel})
    if toevoegen == 'nee':
        lijst == False
        for x in range(len(boodschappen_lijst)):
            print(x[boodschappen_lijst])
