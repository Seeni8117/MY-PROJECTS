
x=[1,2,3,4]
y=[4,6,7,9]
print(x+y)
print(x)
print(x.extend(y))
print(x)
x.sort(reverse=True)
print(x)

'''
str1="hello"
str2="seeni"
print(str1+str2)


list=[1,2,3,4,3,2,1,10,20,40,10,10,9]
(list.remove(10))
print(list)
x=list.pop(0)
print(x)
print(list)
list.reverse()
print(list)
'''

a=[1,2,5,6,3,4]
b=[10,4,7,2,10,3,6,7,10]
'''
def add():
    list=[]
    for i,j in zip(a,b):
        list.append(i+j)
    return list
print(add())
'''
x=[a[i]*b[i] for i in range(0,len(a))]
print(x)