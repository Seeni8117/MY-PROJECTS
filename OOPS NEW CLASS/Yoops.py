'''
class Student:
    pass
student1=Student()
student1.name="seeni"
student1.mark=85

print(student1.name)
print(student1.mark)
'''
'''
class Student:
    def check_pass_fail(self):
        if self.mark>=40:
            return True
        else:
            return False
student1=Student()#object
student1.name="seeni"#atribute
student1.mark=85
did_pass=student1.check_pass_fail()#call the funtion
print(did_pass)

student2=Student()#object
student2.name="sathish"#atribute
student2.mark=30
did_pass=student2.check_pass_fail()#call the funtion
print(did_pass)
'''
'''
class Student:
    def check_pass_fail(self):
        if self.mark>=40:
            return True
        else:
            return False
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
student1=Student("seeni",85)
student2=Student("sathish",30)
print(student1.name)
print(student1.mark)
did_pass=student1.check_pass_fail()
print(did_pass)

print(student2.name)
print(student2.mark)
did_pass=student2.check_pass_fail()
print(did_pass)
'''
def Union(lis1,list2,list3):
	final_list=list1+list2+list3
	return final_list

list1=[1,2,3]
list2=[1,2,3]
list3=[6,3,2]

print(Union(list1,list2,list3))