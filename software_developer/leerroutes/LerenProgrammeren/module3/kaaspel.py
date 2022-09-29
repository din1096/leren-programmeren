kaas = input(' is de kaas geel')

if kaas == 'ja':
    gaten = input('zitten er gaten in')
    if gaten == 'ja': 
        duur = input('is de kaas belachelijk duur')
        if duur == 'ja':
            print('emmenthaler')
        elif duur == 'nee':
         print('Leerdammer') 
    elif gaten == 'nee':
        steen = input('is de kaas hard als steen')
        if steen == 'ja':
            print('parmigiano reggiano')
        elif steen == 'nee':
            print('goudse kaas')

elif kaas == 'nee':
    schimmel = input('heeft de kaas blauwe schimmel')
    if schimmel == 'ja':
        korst_a = input('heeft de kaas een korst')
        if korst_a == 'ja':
            print('blue de rochbaron')
        elif korst_a == 'nee':
            print('foume dambert')
    if schimmel == 'nee':
        korst_b = input('heeft de kaas een korst')
        if korst_b == 'ja':
            print('canembert')
        elif korst_b == 'nee':
            print('mozzarella')
      

 