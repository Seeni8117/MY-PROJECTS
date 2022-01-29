import copy

a=[[1,2,4],4,2,4,6,7]
b=copy.copy(a)
b[4]=100
b[0].append('a')
print(a)
print(b)
