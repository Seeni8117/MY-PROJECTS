
def decor(fun):
    def inner():
        print("this is first")
        fun()
        print("this is last")
    return inner

@ decor
@ decor
def myfun():
    print("this is main")

myfun()

'''
def decorplus(fun):
    def inner():
        print("++++++")
        fun()
        print("++++++")
    return inner
def decorstar(fun):
    def inner():
        print("******")
        fun()
        print("*****")
    return inner
@ decorplus
@ decorstar
def myfun():
    print("this is main")
myfun()
'''
'''
def decor(fun):
    def inner(a,b):
        print("first line")
        x=fun(a,b)
        return x
    print("last line")
    return inner
@ decor
def add(a,b):
    return a+b
print(add(1,3))
'''
'''
def first(msg):
    print(msg)

first("Hello")

second = first
second("Hello")
'''
'''
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)
print(divide(10,2))
'''

