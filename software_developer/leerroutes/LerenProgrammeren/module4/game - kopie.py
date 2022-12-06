print("Welcome bij de dungeon Game!")
print("je besloot deze dungeon te exploreren om schaten te vinden'.")
print("maar toen ging de ingang kapot toen je de dungeon instapte.")
print("je moet nu een andere uitgang vinden om uit de dungeon te komen.")
print("laten we eerst je naam vragen: ")
naam = input()
print("veel geluk, " +naam+ ".")

richtings = ("links","rechts","beneden")
print('je bent in een kamer en ziet meerdere kanten waar je heen kunt.Waar wil je heen?')
Input = ""
while Input not in richtings:
    print('opties links/rechts/beneden')
    Input = input()
    if Input == 'links':
        print('je komt in een kamer terecht en ziet een deur je hoort een stem hij zegt dat je een raadsel moet oplossen anders ga je dood')
        print('dit is het raadsel.Ik been een deel van je ik besta alleen als er licht is maar verdwijn als er licht op me komt. Wat ben ik?')
        raadsel = input('wat is je antwoord')
        if raadsel == 'schaduw':
            print('je hebt het goed je mag door')
            print('je gaat verder en komt in een kamer met een sleutel wat doe je?')
            print('opties pak de sleutel/pak de sleutel niet')
        else:
            print('Je ziet de deur dichtslaan en ziet groene gas in de kamer je word vergiftig.Een tijdje later ben je dood')
            break
        sleutel = input()
        if sleutel == 'pak de sleutel':
            print('je bent terug in de beginkamer waar wil je heen?')
            print('opties links/beneden')
        elif sleutel == 'pak de sleutel niet':
            print('je bent terug in de beginkamer waar wil je heen?')
            print('opties links/beneden')
            input()
    elif Input == 'beneden':
        print('je komt in een kamer en je ziet een groot wapenrek met verschillende wapens wat ga je doen')
        print('opties pak een wapen/pak geen wapen')
        input()