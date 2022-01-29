'''
class employee1():
    def name(self):
        print("harshit is his name")
    def salary(self):
        print("3000 is his salary")
    def age(self):
        print("20 is his age")
class employee2():
    def name(self):
        print("sathish is his name")

    def salary(self):
        print("3000 is his salary")

    def age(self):
        print("23 is his age")

def fun(obj):
    obj.name()
    obj.salary()
    obj.age()
obj_emp1=employee1()
obj_emp2=employee2()
fun(obj_emp1)
fun(obj_emp2)
'''
