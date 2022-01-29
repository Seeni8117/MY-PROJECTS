class Student():
    name = "seeni"
    rnum = "102"

    def __init__(self):
        pass

    def myIntro(self):
        print("hello",self.name,"my rnum is",self.rnum)

student1 = Student()
print(student1.name)
print(student1.rnum)
student1.myIntro()
