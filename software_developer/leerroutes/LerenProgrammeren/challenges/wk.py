land_1 = input('land 1')
land_2 = input('land 2')
land_3 = input('land 3')

score_land1 = 0
score_land2 = 0
score_land3 = 0

doelsaldo_land1 = 0
doelsaldo_land2 = 0
doelsaldo_land3 = 0

voor_land1 = 0
voor_land2 = 0
voor_land3 = 0

tegen_land1 = 0
tegen_land2 = 0
tegen_land3 = 0


print('wedstrijd 1')
land_1_doelpunten = int(input(f'doelenpunten {land_1}'))
land_2_doelpunten = int(input(f'doelenpunten {land_2}'))
land_3_doelpunten = int(input(f'doelenpunten {land_3}'))

voor_land1 += land_1_doelpunten
tegen_land1 =+ land_2_doelpunten
voor_land2 += land_2_doelpunten
tegen_land2 += land_1_doelpunten

if land_1_doelpunten > land_2_doelpunten:
    score_land1 = 3
else:
    score_land2 = 3

doelsaldo_land1 = land_1_doelpunten - land_2_doelpunten
doelsaldo_land2 = land_2_doelpunten - land_1_doelpunten

print(f'{land_1} - {score_land1} - {doelsaldo_land1}')
print(f'{land_2} - {score_land2} - {doelsaldo_land2}')
print(f'{land_2} - {score_land2} - {doelsaldo_land2}')


print('wedstrijd 2')
land_2_doelpunten = int(input(f'doelenpunten {land_2}'))
land_3_doelpunten = int(input(f'doelenpunten {land_3}'))

voor_land2 += land_2_doelpunten
tegen_land2 += doelsaldo_land3
voor_land3 += land_3_doelpunten
tegen_land3 += land_2_doelpunten

if land_2_doelpunten > land_3_doelpunten:
    score_land2 = 3
else:
    score_land3 = 3

doelsaldo_land2 = land_2_doelpunten - land_3_doelpunten
doelsaldo_land3 = land_3_doelpunten - land_3_doelpunten

print(f'{land_2} - {score_land2} - {doelsaldo_land2}')
print(f'{land_3} - {score_land3} - {doelsaldo_land3}')

print('wedstrijd 3')
land_1_doelpunten = int(input(f'doelenpunten {land_2}'))
land_3_doelpunten = int(input(f'doelenpunten {land_3}'))

voor_land1 += land_1_doelpunten
tegen_land1 += doelsaldo_land3
voor_land3 += land_3_doelpunten
tegen_land3 += land_1_doelpunten

if land_1_doelpunten > land_3_doelpunten:
    score_land1 = 3
else:
    score_land3 = 3

doelsaldo_land1 = land_1_doelpunten - land_3_doelpunten
doelsaldo_land3 = land_1_doelpunten - land_3_doelpunten
print(f'{land_1} score uit alle wedstrijden {score_land1} doelpunten voor {voor_land1}doelpunten tegen {tegen_land1}')
print(f'{land_2} score uit alle wedstrijden {score_land2} doelpunten voor {voor_land2}doelpunten tegen {tegen_land2}')
print(f'{land_3} score uit alle wedstrijden {score_land3} doelpunten voor {voor_land3}doelpunten tegen {tegen_land3}')
