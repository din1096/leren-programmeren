

aantal_croissantjes = int(input('hoeveel croissantjes wil je')) 
croissantjes_prijs = (aantal_croissantjes * 0.39)

aantal_stokbrood = int(input('hoeveel stokbrood wil je')) 
stokbrood_prijs = (aantal_stokbrood * 2.78 )

aantal_kortingsbonnen = int(input('hoeveel kortingsbonnen heb je'))
kortingsbonnen_prijs = (aantal_kortingsbonnen * 0.50 )

print(f'{croissantjes_prijs + stokbrood_prijs - kortingsbonnen_prijs}')

croissantjes_prijs = round (croissantjes_prijs, 2);
stokbrood_prijs = round (stokbrood_prijs, 2);  
kortingsbonnen_prijs = round (kortingsbonnen_prijs, 2);
 