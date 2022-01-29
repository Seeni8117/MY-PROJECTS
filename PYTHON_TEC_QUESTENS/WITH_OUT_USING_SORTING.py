list=[24,55,78,64,25,12,22,11,1,2,44,3,122,23,34]
new_list=[]


while list:
    minimum = list[0]
    for x in list:
        if x > minimum:
            minimum = x
    new_list.append(minimum)
    list.remove(minimum)
print(new_list)
