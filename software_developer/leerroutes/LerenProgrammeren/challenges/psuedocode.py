gastheer = input('naam gastheer?')
gasten = 12
drank = True
chips = True

aanwezigen = gasten + 1

if drank and gastheer != 'rudi' and (gastheer or gasten >= 5) and aanwezigen <=13:
    print('start the party')
else:
    print('no party')