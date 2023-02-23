def bereken_poten():
    girrafen_aantal = int(input('hoeveel girrafen zijn er'))
    girrafen_poten = 4
    struisvogels_aantal = int(input('hoeveel struisvogels zijn er'))
    struisvogels_poten = 2
    zebra_aantal = int(input('hoeveel zebras zijn er'))
    zebra_poten = 4
    girrafen_antwoord = girrafen_aantal * girrafen_poten
    struisvogel_antwoord = struisvogels_aantal * struisvogels_poten
    zebra_antwoord = zebra_aantal * zebra_poten
    berekening = print(f'{zebra_antwoord + girrafen_antwoord + struisvogel_antwoord} poten')

bereken_poten()
