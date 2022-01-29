'''
count = 1
while count <= 10:
    print(count)
    count = count + 1


promt = 'write a poem!\n'
promt +='enter "Quit" to end\n'

poem = ""
line = ""
while line != 'Quit':
    line = input(promt)
    poem += line
    poem += '\n'

print(poem.replace('Quit',''))

'''
pets =['dog','cat','mouse','rabit','cat','dog','cat']
print(pets)

while 'cat' and 'dog' in pets:
    pets.remove('cat')
    pets.remove('dog')

print(pets)



