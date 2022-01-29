class Complex:
    def __init__ (self,rel,img):
        self.rel=rel
        self.img=img
    def add(self,number):
        rel = self.rel + number.rel
        img = self.img + number.img
        result = Complex(rel, img)
        return result

n1=Complex(20,30)
n2=Complex(-4,10)
result = n1.add(n2)
print(result.rel)
print(result.img)


