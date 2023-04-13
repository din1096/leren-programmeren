def leeftijd():
    lijst = True
    while lijst:
        lijst_namen = {}
        name = input('voeg een naam toe').lower()
        age = int(input('voeg een leeftijd toe'))
        if name not in lijst_namen:
            lijst_namen.update({name : age})
        elif name in lijst_namen:
            print('dit heb je al gekozen')

