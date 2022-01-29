
class Student():
    def chech_pass_fail(self):
        if self.mark >=40:
            return ("pass")
        else:
            return("fail")

    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

student1 = Student("seeni",85)
print(student1.name)
print(student1.mark)
