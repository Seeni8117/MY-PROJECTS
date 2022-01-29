my_tup = (1,2,3,4,5,'tom',77,'seeni','suraj')
print(my_tup)
newlist =[]
strlist =[]

for i in my_tup:
    if isinstance(i,int):
        newlist.append(i)
        newt=tuple(newlist)
    elif isinstance(i,str):
        strlist.append(i)
        strt=tuple(strlist)
    else:
        print("No one match:")

print("int values:",newt)
print("string values:",strt)





