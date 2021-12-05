ssk={'color':'red','car':'RAIZE'}
print(ssk['color'])

ssk_value=ssk.get('point','nainai')
print(ssk_value)

for i,j in ssk.items():
    print(i)
    print(j)

for i in ssk.keys():
    print(i)