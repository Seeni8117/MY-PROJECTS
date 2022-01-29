class Calculation():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Addtion(self):
        print("ADD", self.a + self.b)
    def Subtraction(self):
        print("SUB", self.a - self.b)
    def Multepcatio(self):
        print("MUL", self.a * self.b)
    def divtion(self):
        print("DIV", self.a / self.b)

cal1=Calculation(20,3)
print("A=",cal1.a, "\nB=",cal1.b)
cal1.Addtion()
cal1.Subtraction()
cal1.Multepcatio()
cal1.divtion()



