class Laptop():
    company="dell computers"


    def  __init__(self,name,modelno):
        self.name=name
        self.modelno=modelno

    def myIntro(self):
        print("my loptop ",self.name,"laptop modelno ",self.modelno)


laptop1 = Laptop("lenova",1331)
laptop2 = Laptop("acer",1452)
print(laptop1.name)
print(laptop1.modelno)
laptop1.myIntro()

print(laptop2.name)
print(laptop2.modelno)
laptop2.myIntro()