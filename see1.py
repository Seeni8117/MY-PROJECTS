a = (1,2,3,4,5,6)
b = (10,12,14,55,74,91)
print("a value is:",a)
print("b value is :",b)
c = []

for i in range(len(a)):
    c.append(a[i]+b[i])
    ctup = tuple(c)

print("Sum of two values:", ctup)




