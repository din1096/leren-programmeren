a = int(input('voer een getal in'))
b = int(input('voer een getal in'))


if a > b:
   Max = a
   Min = b
   print(f'a is het grootste getal is {Max}')

elif a < b:
   Min = a
   Max = b
   print(f'a is het kleinste getal is {Min}')

else:
   print('a en b zijn even groot')
   
   Max = a
   Min = b
   
   print(f'het maximum is{Max}')
   print(f'het minimum is {Min}')