
aantal_toegangsticket = int(input('hoeveel tickets wil je'))
toegangsticket_prijs  = (aantal_toegangsticket * 7.45 )
aantal_gameseat = int(input('hoeveel lang ga je er in '))
gameseat_prijs = (aantal_gameseat * 0.37 )

print(f'dit geweldige dagje-uit met {aantal_toegangsticket} mensen in de speelhal met {aantal_gameseat} minuten vr kost je maar {toegangsticket_prijs + gameseat_prijs} euro')