
aantal_toegangsticket = int(input('hoeveel tickets wil je'))
toegangsticket_prijs  = (aantal_toegangsticket * 7.45 )
tijd_gameseat = int(input('hoelang ga je er in '))
gameseat_prijs = (tijd_gameseat * 0.37/5 )




print(f'dit geweldige dagje-uit met {aantal_toegangsticket} mensen in de speelhal met {tijd_gameseat} minuten vr kost je maar {toegangsticket_prijs + gameseat_prijs} euro')

toegangsticket_prijs = round (toegangsticket_prijs, 2);
gameseat_prijs = round (gameseat_prijs, 2);