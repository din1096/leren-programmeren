from fruitmand import fruitmand
fruitmand.append({
'name': 'watermeloen', 
'weight': 1000, 
'color': 'lime', 
'round' : True 
})
totaal = 0
for fruit in fruitmand:
    totaal += fruit['weight']
print(totaal)

