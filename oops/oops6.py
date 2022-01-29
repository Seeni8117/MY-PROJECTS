class Mat():

    def __init__(self,r):
        self.r=r
    def volumofcube(self):
        print(self.r*self.r*self.r)
    def volumofspher(self):
        print(4/3*13.14*self.r*self.r*self.r)

mat1=Mat(14)
print("r=",mat1.r)
print("volum of cub:",mat1.r*mat1.r*mat1.r)
print("volum of speher:",4/3*13.14*mat1.r*mat1.r*mat1.r)
print("area of cube:",6*mat1.r*mat1.r)
print("Area if circule:",3.14*mat1.r*mat1.r)