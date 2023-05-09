def leeftijd():
    dictonary_namen = {}
    naam_vraag = input('voeg een naam toe').lower()
    leeftijd_vraag = int(input('voeg een leeftijd toe'))
    dictonary_namen["name"] = naam_vraag
    dictonary_namen['age'] = leeftijd_vraag
    return dictonary_namen

list_namen = []

while True:
    list_namen.append(leeftijd())
    if input('wil je nog iemand toevoegen') == 'nee':
           break

for x in list_namen:
            print(f"{x['name']} is {x['age']} jaar oud")