'''
class School:
    pass
obj=School()
print(obj)
'''
'''
class School:
    def add(seeni):
        print(10+20)

obj=School()
obj.add()
'''
'''
class School:
    def __init__(self):
        print("this is init method")
    def add(seeni,a,b):
        return a+b

obj=School()
print(obj.add(10,20))
'''
'''
class School:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
obj=School(3,5)
print(obj.add())
'''
'''
#class vareyble
class School:
    def __init__(self,a,b=0):
        self.a=a     #constrector
        self.b=b
    def add(self):
        return self.a+self.b
obj=School(3)
print(obj.add())
obj1=School(15,30)
print(obj1.add())
del(obj)#delete the ogject
print(obj.add())
'''
'''
#class vareables
class myclass:
    myclassvar='hello'
    def __init__(self):
        print(self.myclassvar)
obj=myclass()
#print(obj)
'''
'''
#class vareables
class myclass:
    myclassvar='hello'
    def __init__(self):
        print(self.myclassvar)
    def printinfo(self):
        print(self.myclassvar)
obj=myclass()
obj.myclassvar='how are you'
obj.printinfo()
obj1=myclass()
'''
'''
num1=10#globle
class myclass:
    num2=20#instent
    def add(self):       
        print(num1+self.num2)
obj=myclass()
num1=50
obj.add()
'''
def add(self,num1=20):
    num = 10
    def inner():
        nonlocal num
        num=20
        print(num+num1)
    inner()
    print(num)
add(10,20)
