class AgeExcept(Exception):
    def __init__(self,age):
        self.age=age
        super().__init__('age is not eligibal')
age=int(input('place provide age:'))
if not 18<age<35:
    raise AgeExcept(age)
else:
    print('age is eligibal')
