

aantal_croissantjes = float(input('hoeveel croissantjes wil je')) 
croissantjes_prijs = (aantal_croissantjes * 390/100)

aantal_stokbrood = float(input('hoeveel stokbrood wil je')) 
stokbrood_prijs = (aantal_stokbrood * 278/100)

aantal_kortingsbonnen = float(input('hoeveel kortingsbonnen heb je'))
kortingsbonnen_prijs = (aantal_kortingsbonnen * 50/100)

print(f'de feestlunch kost je bij de baker {croissantjes_prijs + stokbrood_prijs - kortingsbonnen_prijs} euro voor de {aantal_croissantjes} als de {aantal_kortingsbonnen} nog geldig zijn!') 

