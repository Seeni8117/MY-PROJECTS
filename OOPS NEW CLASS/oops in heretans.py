

class Animal:
    def eat(self):
        print("i can eat")

class Dog(Animal):#we derived dog in main class
    def bark(self):
        print("i can bark")
class Cat(Animal):
    def get_grumpy(self):
        print("i am get grumpy")
dog1=Dog()
dog1.eat()
dog1.bark()

cat1=Cat()
cat1.eat()

