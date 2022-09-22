prijs_iphone = int(input('hoeveel kost een iphone'))
prijs_samsung = int(input('hoeveel kost een samsung'))


if prijs_iphone < prijs_samsung :
    print(f'De samsung is het duurst,de telefoon kost{prijs_samsung} euro')
    print(f'De iphone is het goedkoopst, de telefoon{prijs_iphone} euro')
    print(f'Het advies is dus de iphone te kopen.Deze is  namelijk{prijs_samsung - prijs_iphone} euro goedkoper dan de samsung galaxy s22')

elif prijs_iphone > prijs_samsung :
    print(f'De iphone is het duurst,De telefoon kost {prijs_iphone} euro')
    print(f'De samsung is het goedkoopst,de telefoon kost {prijs_samsung} euro')
    print(f'Het advies is dus de samsung te kopen.deze is namelijk {prijs_iphone - prijs_samsung} euro goedkoper dan de iphone 13')
    
elif prijs_iphone / prijs_samsung :
    print(f'niks is het duurst ze kosten allenbij het zelfde')
    print(f'het advies is dus de iphone te kopen deze is namelijk {prijs_iphone - prijs_samsung} euro goedkoper dan de samsung')