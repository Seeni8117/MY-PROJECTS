odd_list = []
even_list = []


for i in range(1,101):
    if(i%2 != 0):
        odd_count=odd_count+1
    elif(i%2 == 0):
        even_count=even_count+1
    else:
        pass

print("odd numbers ", odd_count," \neven numbers ", even_count)

