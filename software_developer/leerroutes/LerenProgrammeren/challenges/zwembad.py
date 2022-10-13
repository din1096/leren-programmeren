meter_lang = int(input('hoe lang is het in meter'))
meter_breed = int(input('hoe breed is het in meter'))
meter_diep = float(input('hoe diep is het in meter'))
grond = meter_lang * meter_breed * meter_diep

uitgraven_prijs = 25 * grond
afvoeren_prijs = 32.50 * grond
voorrijk_prijs = 270.50
totaal_prijs = uitgraven_prijs + afvoeren_prijs + voorrijk_prijs

print(f'in totaal moet {grond} grond worden afgevoerd')

print(f'offerte voor de een zwembad van {meter_lang} bij {meter_breed} bij {meter_diep} meter')
print(f'het kost {uitgraven_prijs} euro')
print (f'het kost {afvoeren_prijs} euro')
print(f'het kost {voorrijk_prijs} euro')
print(f'het kost in totaal {totaal_prijs} euro')