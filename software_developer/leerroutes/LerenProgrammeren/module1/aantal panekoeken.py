import math


bloem = 500/20
melk = 800/20
eieren = 3/20
zout = 1/20  
boter = 30/20   

aantal = int(input('hoeveel panenkoeken wil je'))
bloem = aantal * bloem
melk = aantal * melk
eieren = aantal * eieren
zout = aantal * zout
boter = aantal * boter

print(f'voor {aantal} heeft u nodig:')
print(f'{math.ceil(bloem):.0f} g bloem' )
print(f'{math.ceil(melk):.0f} ml melk' )
print(f'{math.ceil(eieren):.0f} eieren' )
print(f'{math.ceil(zout):.0f} tl zout' )
print(f'{math.ceil(boter):.0f} g boter' )
