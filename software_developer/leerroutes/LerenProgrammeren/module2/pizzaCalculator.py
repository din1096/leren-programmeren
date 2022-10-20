# dinho hooi pizza calculator
from distutils.log import error

try:
    pizza_small = int(input('hoeveel kleine pizza wil je'))
except:
    print('vul een heel getal')

try:
    pizza_medium = int(input('hoeveel medium pizza wil je'))
except:
    print('vul een heel getal in')
try:
    pizza_large = int(input('hoeveel grote pizza wil je'))
except:
    print('vul een heel getal in')

prijs_s = 7,77
prijs_m = 10,80
prijs_l = 12,99
pizza_prijs_s = pizza_small * prijs_s
pizza_prijs_m = pizza_medium * prijs_m
pizza_prijs_l = pizza_large * prijs_l
totaal_prijs = pizza_prijs_s + pizza_prijs_m + pizza_prijs_l
pizza_totaal = pizza_small + pizza_medium + pizza_large

pizza_prijs_s = round (pizza_prijs_s, 2);
pizza_prijs_m = round (pizza_prijs_m,2);
pizza_prijs_l = round(pizza_prijs_l,2);
totaal_prijs = round(totaal_prijs,2);

print('-----------------------------------------------------------------------')
print(f'het kost voor de {pizza_small} kleine pizza {pizza_prijs_s} euro')
print(f'het kost voor de {pizza_medium} medium pizza {pizza_prijs_m} euro')
print(f'het kost voor de {pizza_large} grote pizza {pizza_prijs_l} euro')
print(f'het kost voor alle {pizza_totaal} pizza {totaal_prijs} euro ')
print('------------------------------------------------------------------------')