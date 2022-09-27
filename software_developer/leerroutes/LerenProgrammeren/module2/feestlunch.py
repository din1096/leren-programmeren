

aantal_croissantjes = int(input('hoeveel croissantjes wil je')) 
croissantjes_prijs = (aantal_croissantjes * 390)

aantal_stokbrood = int(input('hoeveel stokbrood wil je')) 
stokbrood_prijs = (aantal_stokbrood * 278)

aantal_kortingsbonnen = int(input('hoeveel kortingsbonnen heb je'))
kortingsbonnen_prijs = (aantal_kortingsbonnen * 50)
totaal_prijs = (croissantjes_prijs + stokbrood_prijs - kortingsbonnen_prijs) / 100

print(f'de feestlunch kost je bij de baker {totaal_prijs} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!') 

