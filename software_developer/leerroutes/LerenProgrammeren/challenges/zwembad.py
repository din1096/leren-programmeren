uitgraf_kuub = 25
afvoer_kuub = 32.5


meter_lang = int(input('hoe lang is het in meter'))
meter_breed = int(input('hoe breed is het in meter'))
meter_diep = float(input('hoe diep is het in meter'))
afstand = 60
grond = meter_lang * meter_breed * meter_diep 



uitgraven_prijs = round(uitgraf_kuub * grond,2)
afvoeren_prijs = round(afvoer_kuub * grond,2)

 
voorrijkosten = 0
if afstand < 50 and grond < 20:
    vorrij_prijs_km = 1.25
    vaste_prijs = 100
elif afstand > 50 and grond < 20:
    vorrij_prijs_km = 1.15
    vaste_prijs = 100
elif afstand < 50 and grond >= 20:
    vorrij_prijs_km = 2.15
    vaste_prijs = 250
elif afstand >= 50 and grond >= 20:
    vorrij_prijs_km = 2.05
    vaste_prijs = 250
else:
    print('foutje')

vorrijk_prijs = round(vaste_prijs + vorrij_prijs_km * grond,2)
totaal_prijs = round(uitgraven_prijs + afvoeren_prijs + vorrijk_prijs,2) 

print(f'''
uitgrafkosten:       {uitgraven_prijs:.2f} euro
afvoeren:         {afvoeren_prijs:.2f} euro
voorijk            {vorrijk_prijs:.2f} euro 
totaal:            {totaal_prijs:.2f} euro
'''
)                      