print("Welcome bij de dungeon Game!")
print("je besloot deze dungeon te exploreren om schaten te vinden'.")
print("maar toen ging de ingang kapot toen je de dungeon instapte.")
print("je moet nu een andere uitgang vinden om uit de dungeon te komen.")
print("laten we eerst je naam vragen:")
naam = input()
print("veel geluk, " +naam+ ".")
print('je komt in een kamer en ziet meerdere kanten waar je heen kunt welke kant ga je heen')
print('opties links/rechts/beneden')
richting = input()
if richting == 'links':
    print('je komt in een kamer terecht en ziet een deur je hoort een stem hij zegt dat je een raadsel moet oplossen anders ga je dood')
    print('dit is het raadsel.Ik been een deel van je ik besta alleen als er licht is maar verdwijn als er licht op me komt. Wat ben ik?')
    raadsel = input('wat is je antwoord')
    if raadsel == 'schaduw':
        print('je hebt het goed je mag door')
        print('je gaat verder en komt in een kamer met een sleutel wat wil je doen')
        print('opties pak de sleutel')
        sleutel = input()
        if sleutel == 'pak de sleutel':
            print('je bent terug in de beginkamer met een sleutel waar wil je heen?')
            print('opties rechts/beneden')
            richting = input()
            if richting == 'rechts':
                print('je loopt rechts en komt een grote kamer met meerdere pilaars binnen en ziet een group zombies')
                print('wat ga je doen?')
                print('opties afleiden/rennen')
                antwoord = input()
                if antwoord == 'afleiden':
                    print('Je zoekt iets om de zombies af te leiden je ziet een steen op de grond en krijgt een idee je verstopt je achter een pilaar en gooit de steen.De zombies reageren meteen en rennen de kant van het geluid op')
                    print('je komt een kamer binnen met een deur die op slot is')
                    print('heb je een sleutel')
                    print('opties ja/nee')
                    antwoord = input()
                    if antwoord == 'ja':
                        print(f'Je bent uit de dungeon goed gedaan {naam}')
                    elif antwoord == 'nee':
                        print('je kreeg de deur niet open')
                        print('je kamer begint de gloeien en komen worden voor je het leest dat je nog een kans hebt en als je die fout hebt dan ga je dood')
                        print('je krijgt een raadsel')
                        print('dit is het raadsel.Hoe meer ervan is, hoe minder je ziet. Wat is het?')
                        raadsel = input('wat is je antwoord')
                        if raadsel == 'duisternis':
                            print('je hebt het raadsel goed lees je de deur gaat open.Je mag uit de dungeon')
                            print(f'het is je gelukt goed gedaan {naam}')
                        else:
                            print('Je hebt het fout lees je de kamer begint te trillen en de muren komen naar elkaar toe je bent dood')
                elif antwoord == 'rennen':
                    print('De zombies zien je en weg te rennen maar je struikelt je probeert op te staan maar de zombies beginnen je te pakken.Ze omcirkelen je en dat is het laatse dat je ziet.')
                    print('Je bent dood')
            elif richting == 'beneden':
                print('je komt in een kamer en je ziet een groot wapenrek met verschillende wapens wat ga je doen')
                print('opties pak een wapen')
                wapen = input()
                if wapen == 'pak een wapen':
                    print('je hebt nu een wapen')
                    print('je ziet twee verschillende kanten waar je heen kunt gaan')
                    print('Welke kant wil je op?')
                    print('opties links/rechts')
                    antwoord = input()
                    if antwoord == 'links':
                        print('Je loopt links en komt in een grote kamer en ziet overall goud munten en schatten')
                        print('Je pakt alles wat je kan en als je denkt dat je genoeg hebt ga je terug naar de wapenkamer')
                        print('welke kant ga je op')
                        print('opties rechts')
                        antwoord = input()
                    elif antwoord == 'rechts':
                        print('je loopt rechts en komt een grote kamer met meerdere pilaars binnen en ziet een group zombies')
                        print(f'heb je een {wapen} gepakt in de wapenkamer')
                        print('opties ja/nee')
                        antwoord = input()
                        if antwoord == 'ja':
                            print('De zombies zien je aankomen en rennen naar toe je pakt je wapen.Een paar minuten later sta je te hijgen en om je heen zijn lijken van zombies')
                            print('je komt een kamer binnen met een deur die op slot is')
                            print('heb je een sleutel')
                            print('opties ja/nee')
                            antwoord = input()
                            if antwoord == 'ja':
                                print(f'Je bent uit de dungeon goed gedaan {naam}')
                            elif antwoord == 'nee':
                                print('je kreeg de deur niet open')
                                print('je kamer begint de gloeien en komen worden voor je het leest dat je nog een kans hebt en als je die fout hebt dan ga je dood')
                                print('je krijgt een raadsel')
                                print('dit is het raadsel.Hoe meer ervan is, hoe minder je ziet. Wat is het')
                                raadsel = input('wat is je antwoord')
                                if raadsel == 'duisternis':
                                    print('je hebt het raadsel goed lees je de deur gaat open.Je mag uit de dungeon')
                                    print(f'het is je gelukt goed gedaan {naam}')
                                else:
                                    print('Je hebt het fout lees je de kamer begint te trillen en de muren komen naar elkaar toe je bent dood')
                else:
                    print('het antwoord is fout je ziet de deur dichtslaan en ziet groene gas de gamer in komen je word vergiftiged')
                    print('je bent dood')

elif richting == 'beneden':
    print('je komt in een kamer en je ziet een groot wapenrek met verschillende wapens wat ga je doen')
    print('opties pak een wapen')
    wapen = input()
    if wapen == 'pak een wapen':
        print('je hebt nu een wapen')
        print('je ziet twee verschillende kanten waar je heen kunt gaan')
        print('Welke kant wil je op?')
        print('opties links/rechts')
        antwoord = input()
        if antwoord == 'links':
            print('Je loopt links en komt in een grote kamer en ziet overall goud munten en schatten')
            print('Je pakt alles wat je kan en als je denkt dat je genoeg hebt ga je terug naar de wapenkamer')
            print('welke kant ga je op')
            print('opties rechts')
            antwoord = input()
        elif antwoord == 'rechts':
            print('je loopt rechts en komt een grote kamer met meerdere pilaars binnen en ziet een group zombies')
            print(f'heb je een {wapen} gepakt in de wapenkamer')
            print('opties ja/nee')
            antwoord = input()
            if antwoord == 'ja':
                print('De zombies zien je aankomen en rennen naar toe je pakt je wapen.Een paar minuten later sta je te hijgen en om je heen zijn lijken van zombies')
                print('je komt een kamer binnen met een deur die op slot is')
                print('heb je een sleutel')
                print('opties ja/nee')
                antwoord = input()
                if antwoord == 'ja':
                    print(f'Je bent uit de dungeon goed gedaan {naam}')
                elif antwoord == 'nee':
                    print('je kreeg de deur niet open')
                    print('je kamer begint de gloeien en komen worden voor je het leest dat je nog een kans hebt en als je die fout hebt dan ga je dood')
                    print('je krijgt een raadsel')
                    print('dit is het raadsel.Hoe meer ervan is, hoe minder je ziet. Wat is het')
                    raadsel = input('wat is je antwoord')
                    if raadsel == 'duisternis':
                        print('je hebt het raadsel goed lees je de deur gaat open.Je mag uit de dungeon')
                        print(f'het is je gelukt goed gedaan {naam}')
                    else:
                        print('Je hebt het fout lees je de kamer begint te trillen en de muren komen naar elkaar toe je bent dood')
                        
elif richting == 'rechts':
    print('je loopt rechts en komt een grote kamer met meerdere pilaars binnen en ziet een group zombies')
    print('wat ga je doen?')
    print('opties afleiden/rennen')
    antwoord = input()
    if antwoord == 'afleiden':
        print('Je zoekt iets om de zombies af te leiden je ziet een steen op de grond en krijgt een idee je verstopt je achter een pilaar en gooit de steen.De zombies reageren meteen en rennen de kant van het geluid op')
        print('je komt een kamer binnen met een deur die op slot is')
        print('heb je een sleutel')
        print('opties ja/nee')
        antwoord = input()
        if antwoord == 'ja':
            print(f'Je bent uit de dungeon goed gedaan {naam}')
        elif antwoord == 'nee':
            print('je kreeg de deur niet open')
            print('je kamer begint de gloeien en komen worden voor je het leest dat je nog een kans hebt en als je die fout hebt dan ga je dood')
            print('je krijgt een raadsel')
            print('dit is het raadsel.Hoe meer ervan is, hoe minder je ziet. Wat is het?')
            raadsel = input('wat is je antwoord')
            if raadsel == 'duisternis':
                print('je hebt het raadsel goed lees je de deur gaat open.Je mag uit de dungeon')
                print(f'het is je gelukt goed gedaan {naam}')
            else:
                print('Je hebt het fout lees je de kamer begint te trillen en de muren komen naar elkaar toe je bent dood')
    elif antwoord == 'rennen':
        print('De zombies zien je en weg te rennen maar je struikelt je probeert op te staan maar de zombies beginnen je te pakken.Ze omcirkelen je en dat is het laatse dat je ziet.')
        print('Je bent dood')