class Student():

    def __init__(self,name,rnum):
        self.name=name
        self.rnum=rnum

    def myIntro(self):
        print("my name is",self.name,"my rnum is",self.rnum)

student1 = Student("seeni",102)
student2 = Student("venu",103)
print(student1.name)
print(student1.rnum)
student1.myIntro()

print(student2.name)
print(student2.rnum)
student2.myIntro()
