'''
def cal(x,y):
    try:
        return x/y
    except:
        return("Tis is not coerret cal")

x=cal(10,0)
print(x)
'''
'''
def cal(x,y):
    try:
        return x/y
    except:
        return x/1

x=cal(10,0)
print(x)
'''
'''
def cal(x,y):
    try:
        return x/y
    except:
        return x/1

x=cal(10,'1')
print(x)
'''
'''
def cal(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return x/1


x=cal(10,0)
print(x)
'''
'''
def cal(x,y):
    try:
        print(x/y)
    except TypeError:
        print(x/1)
    finally:
        print("finally block")
    print("end of the program")
x=cal(10,0)
'''
def cal(x,y):
    try:
        print(x/y)
    except TypeError:
        print(x/1)
    else:#else accept only excpet
        print("finally block")
    print("end of the program")
x=cal(10,'0')
