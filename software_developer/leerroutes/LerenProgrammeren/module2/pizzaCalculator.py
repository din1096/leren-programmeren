# dinho hooi pizza calculator

pizza_small = int(input('hoeveel kleine pizza wil je'))
pizza_medium = int(input('hoeveel medium pizza wil je'))
pizza_large = int(input('hoeveel grote pizza wil je'))

pizza_prijs_s = (pizza_small * 7)
pizza_prijs_m = (pizza_medium * 10)
pizza_prijs_l = (pizza_large * 12)
totaal_prijs = pizza_prijs_s + pizza_prijs_m + pizza_prijs_l

print('-----------------------------------------------------------------------')
print('|',pizza_prijs_s,'euro')
print('|',pizza_prijs_m,'euro')
print('|',pizza_prijs_l,'euro')
print('|',totaal_prijs,'euro')
print('------------------------------------------------------------------------')