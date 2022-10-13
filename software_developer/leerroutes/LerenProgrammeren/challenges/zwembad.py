meter_lang = 8
meter_breed = 3
meter_diep = 1.5
grond = meter_lang * meter_breed * meter_diep

uitgraven_prijs = 25 * grond
afvoeren_prijs = 32.50 * grond
voorrijk_prijs = 270.50
totaal_prijs = uitgraven_prijs + afvoeren_prijs + voorrijk_prijs

print(f'in totaal moet {grond} grond worden afgevoerd')

print('offerte voor de een zwembad van 8 bij 3 bij 1.5 meter')
print(f'het kost {uitgraven_prijs} euro')
print (f'het kost {afvoeren_prijs} euro')
print(f'het kost {voorrijk_prijs} euro')
print(f'het kost in totaal {totaal_prijs} euro')