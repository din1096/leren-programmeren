print('---------------------------------------------------------------------------------------------------------')
print('                  sollicitatieformulier circusdirecteur voor Circus Hotel De Botel                         ')
print('---------------------------------------------------------------------------------------------------------')
print('er word uw een aantal vragen gesteld als u voor alle creteria in aanmerking komt voor een serieus gesprek')
print('--------------------------------------------------------------------------------------------------------')

naam = input('wat is uw naam?')
mbo = input(' bent u in bezit van een mbo diploma ja/nee?')
rijbewijs = input('in bezit van een geldig vrachtwagen rijbewijs ja/nee?')
hoed = input('in bezit van een hoge hoed ja/nee?')
gender = input('bent uw een man of vrouw?')
if gender == 'man':
    snor = input('heeft u een snor ja/nee?')
    if snor == 'ja':
        snor_lengte = int(input('wat is de lengte van de snor in hele cm'))
        pass
 
elif gender == 'vrouw':
    haar = input('heeft u rood krullig haar ja/nee')
    if haar == 'ja':
        haar_lengte = int(input('wat is de lengte van uw haar in hele cm'))

lichaam_lengte = int(input('wat is uw lengte in hele cm'))
gewicht = int(input('wat is uw lichaamsgewicht in hele kilogram'))
certificaat = input('heb je een certificaat Overleven met gevaarlijk personeel ja/nee')
dieren_dressuur = int(input('hoeveel jaren ervaring heb je in dieren dressuur in hele jaren'))
jongleren = int(input('hoeveel jaren ervaring heb je met jongleren in hele jaren'))
acrobatiek = int(input('hoeveel jaren ervaring heb je met acrobatiek in hele jaren'))

if (snor_lengte > 10 or haar_lengte > 20) and mbo == 'ja' and rijbewijs == 'ja' and hoed == 'ja' and lichaam_lengte > 150 and lichaam_lengte < 220 and gewicht > 90   and gewicht < 120 and certificaat == 'ja' and (dieren_dressuur > 4 or jongleren > 5 or acrobatiek > 3):
    print('u voldoet aan alle criteria we hopen u te zien in sollecitatie gesprek')

else:
    print('uw voldoet niet aan alle eisen om in aanmerking te komen voor een sollicitatie gesprek')