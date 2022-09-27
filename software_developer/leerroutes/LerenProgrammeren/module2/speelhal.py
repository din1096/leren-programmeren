
aantal_toegangsticket = int(input('hoeveel tickets wil je'))
toegangsticket_prijs  = (aantal_toegangsticket * 745 )
tijd_gameseat = int(input('hoelang ga je er in '))
gameseat_prijs = (tijd_gameseat * 37 )
totaal_prijs = (toegangsticket_prijs + gameseat_prijs) / 100

print(f'dit geweldige dagje-uit met {aantal_toegangsticket} mensen in de speelhal met {tijd_gameseat} minuten vr kost je maar {totaal_prijs} euro')
