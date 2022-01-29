class Student():
    def check_pass_fail(self):
        if self.mark >=40:
            return ("pass")
        else:
            return ("fail")

student1=Student()
student1.name="seeni"
student1.mark=90

std_pass=student1.check_pass_fail()
print(std_pass)


student2=Student()
student2.name="sathish"
student2.mark=35

std_pass=student2.check_pass_fail()
print(std_pass)