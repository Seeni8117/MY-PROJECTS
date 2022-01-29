import math
class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def cal(self):
        print("\nADD",self.a+self.b,"\nSUB",self.a-self.b,"\nMUL",self.a*self.b,"\nDIV",self.a/self.b)
class Normal_calulator(Calculator):
    def __init__(self,a,b):
        super().__init__(a,b)
    def cal(self):
        print("\nADD", self.a + self.b, "\nSUB", self.a - self.b, "\nMUL", self.a * self.b,
              "\nDIV", self.a / self.b,"\nExponent=",self.a**self.b)
class Scitcalculator(Calculator):
    def __init__(self, a, b,x):
        super().__init__(a, b)
        self.x=x
    def cal(self):
        print("\nADD", self.a + self.b, "\nSUB", self.a - self.b, "\nMUL", self.a * self.b,
              "\nDIV", self.a / self.b, "\nsin value=",(math.sin(self.x)),"\ncos value",(math.cos(self.x)),
              "\ntan value",(math.tan(self.x)))
calculator=Normal_calulator(20,4)
scitcalculator=Scitcalculator(20,4,6)
calculator.cal()
scitcalculator.cal()



