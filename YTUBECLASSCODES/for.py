'''
lang =['java','c','c++','javascript','python']

count = 0
while count < len(lang):
    print(lang[count])
    count += 1

for i in lang:
    print(i)


p = 'PYTHON'
for i in p:
    print(i)
'''

cars = ['audi','bmw','maruti','toyota']

for i in cars:
    if i == 'bmw':
        print(i.upper())
    else:
        print(i.title())

dosa_price = 20
req_toop = ['ghee','veg']

for i in req_toop:
    if i == 'veg':
        dosa_price += 5
    else:
        dosa_price +=20

print(f'Dosa price:{dosa_price}')

