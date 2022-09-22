prijs_iphone = int(input('hoeveel kost een iphone'))
prijs_samsung = int(input('hoeveel kost een samsung'))

verschil = prijs_samsung - prijs_iphone

if verschil > 50 :
    print(f'de samsung is het duurst de telefoon kost {prijs_samsung} euro')
    print(f'de iphone is het goedkoopst de telefoon kost {prijs_iphone} euro')
    print(f'het advies is dus de iphone te kopen. deze is namelijk {prijs_samsung - prijs_iphone} goedkoper dan de samsung')

elif verschil < 50 :
    print(f'de iphone is het duurst de telefoon kost{prijs_iphone} euro')
    print(f'de samsung is het goedkoopst de telefoon kost{prijs_samsung} euro ')
    print(f'het advies is dus de samsung te kopen deze is namelijk {prijs_iphone - prijs_samsung} euro goedkoper dan de iphone')
    
elif prijs_iphone == prijs_iphone :
    print(f'het advies is dus om de iphone te kopen  deze is namelijk {prijs_samsung - prijs_iphone} goedkoper dan de samsung')    

    