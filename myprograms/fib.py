
def fib(n):
    a=0
    b=1

    print(a)
    print(b)

    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)
print("fibonace numbers")

fib(10)

'''
def fib(x):
    a,b=0,1
    print(a,b,sep=',',end='\n')
    for i in range(2,x):
        temp=a+b
        a=b
        b=temp
        print(temp)
fib(10)


def fun(x):
    if(x<=0):
        return 2
    else:
        return fun(x-1)+fun(x-2)
for i in range(10):
        print(fun(i))
#print(fun)

'''
