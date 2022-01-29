from functools import reduce as red, reduce

lst=[10,15,20,25,30,35]
x= reduce (lambda a,b:a+b,lst)
print(x)
#y=reduce(lambda a,b:a if a<b else b,lst)
#print(y)
