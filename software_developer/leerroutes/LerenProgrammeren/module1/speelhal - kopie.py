
aantal_toegangsticket = int(input('hoeveel tickets wil je'))
toegangsticket_prijs  = (aantal_toegangsticket * 7.45 )
aantal_gameseat = int(input('hoeveel lang ga je er in '))
gameseat_prijs = (aantal_gameseat * 0.37 )

print(f'het kost in totaal {toegangsticket_prijs + gameseat_prijs} euro')