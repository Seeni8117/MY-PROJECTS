class Triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def ang(self):
        print('ang',self.a+self.b+self.c)

tri=Triangle(3,4,5)

tri.ang()