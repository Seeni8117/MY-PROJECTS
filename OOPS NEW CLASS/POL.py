'''
class parent():
    name="kumar"
class child(parent):
    name="sathish"      #over riding
obj=child()
print(obj.name)
'''
class Bank():
    def intrest(self):
        return 0
class icici():
    def intrest(self):
        return 10.5
obj=icici()
print(obj.intrest())
#obj1=Bank()
#obj1.intrest()
