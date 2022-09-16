

aantal_croissantjes = int(input('hoeveel croissantjes wil je')) 
croissantjes_prijs = (aantal_croissantjes * 0.39)

aantal_stokbrood = int(input('hoeveel stokbrood wil je')) 
stokbrood_prijs = (aantal_stokbrood * 2.78 )
print(type(stokbrood_prijs))
print('hallo')
aantal_kortingsbonnen = int(input('hoeveel kortingsbonnen heb je'))
kortingsbonnen_prijs = (aantal_kortingsbonnen * 0.50 )

print(f'de feestlunch kost bij je bakker {croissantjes_prijs + stokbrood_prijs - kortingsbonnen_prijs} voor {aantal_croissantjes} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!')
