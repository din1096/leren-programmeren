def vraag_en_controleer_leeftijd(vraag: str) int:
    while True:
        leeftijd_string = input('wat is je leeftijd')
        if not leeftijd_string.isnumeric():
            print('voer een cijfer in')
        elif int(leeftijd_string) < 0:
            print('u moet nog geboren worden')
        else:
            leeftijd = int(leeftijd_string)
            break
        return leeftijd


naam = input('wat is je naam')
leeftijd = vraag_en_controleer_leeftijd

print(f'')