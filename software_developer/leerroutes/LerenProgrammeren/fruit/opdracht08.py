from fruitmand import fruitmand
fruitmand.append({
'name': 'watermeloen', 
'weight': 1000, 
'color': 'green', 
'round' : True 
})
totaal = 0
for x in fruitmand:
    totaal += x['weight']
print(totaal)

