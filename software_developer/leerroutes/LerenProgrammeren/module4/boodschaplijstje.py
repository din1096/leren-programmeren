boodschappen_lijst = {}
lijst = True
while lijst:
    boodschappen = input('wat wil je als boodschappen').lower()
    hoeveel = int(input('hoeveel wil je ervan'))
    toevoegen = input('wil je nog wat toevoegen')
    if boodschappen not in boodschappen_lijst:
        boodschappen_lijst.update({boodschappen : hoeveel})      
    elif boodschappen in boodschappen_lijst:
        boodschappen_lijst[boodschappen] += hoeveel

    if toevoegen == 'nee':
        lijst = False


for x, y in boodschappen_lijst.items():
  print(x, y)

