lijst =[]
namen = True
while namen:
    naam = input('welke naam wil je')
    opnieuw = input('wil je nog een naam ja of nee')
    if opnieuw == 'nee':
        namen = False
        if lijst == 3:
            namen = False

print(lijst)

