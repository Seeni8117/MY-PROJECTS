odd_list = []
even_list = []



for i in range(1,100):
    if(i%2 != 0):
        odd_list.append(i)
        oddt = tuple(odd_list)
    elif(i%2 == 0):
        even_list. append(i)
        event = tuple(even_list)
    else:
        pass

print("odd numbers ", oddt," \neven numbers ", event)

