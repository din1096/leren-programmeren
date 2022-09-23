
aantal_toegangsticket = float(input('hoeveel tickets wil je'))
toegangsticket_prijs  = (aantal_toegangsticket * 745/100 )
tijd_gameseat = float(input('hoelang ga je er in '))
gameseat_prijs = (tijd_gameseat * 37/100 )


print(f'dit geweldige dagje-uit met {aantal_toegangsticket} mensen in de speelhal met {tijd_gameseat} minuten vr kost je maar {toegangsticket_prijs + gameseat_prijs} euro')
