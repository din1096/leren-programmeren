kaas = input(' is de kaas geel')

if kaas == 'ja':
    gaten = input('zitten er gaten in')
    if gaten == 'ja': 
        duur = input('is de kaas belachelijk duur')
        if duur == 'ja':
            print('je kaas is emmenthaler')
        elif duur == 'nee':
         print('je kaas is Leerdammer') 
    elif gaten == 'nee':
        steen = input('is de kaas hard als steen')
        if steen == 'ja':
            print('je kaas is parmigiano reggiano')
        elif steen == 'nee':
            print('ke kaas is goudse kaas')

elif kaas == 'nee':
    schimmel = input('heeft de kaas blauwe schimmel')
    if schimmel == 'ja':
        korst_a = input('heeft de kaas een korst')
        if korst_a == 'ja':
            print('je kaas is blue de rochbaron')
        elif korst_a == 'nee':
            print('je kaas is foume dambert')
    if schimmel == 'nee':
        korst_b = input('heeft de kaas een korst')
        if korst_b == 'ja':
            print('je kaas is canembert')
        elif korst_b == 'nee':
            print('je kaas is mozzarella')