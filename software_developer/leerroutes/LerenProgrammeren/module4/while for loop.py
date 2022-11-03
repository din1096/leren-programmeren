
# variant 1 == lijsten
# variant 2 != lijsten randint(1 , 4) mbv . if

from random import randint


naam = input('wat is je naam')
complimenten = int(input('hoeveel complimenten wil je'))
getal = randint(1, 4)

for x in range(complimenten):
 if getal == 1:
    print(f'je bent gweldige {naam}')
 elif getal == 2:
    print(f'je bent zo slim {naam}')
 elif getal == 3:
    print(f'je doet het zo goed {naam}')
 else:
    print(f'je bent zo cool {naam}') 
vorige_random = getal