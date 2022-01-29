class Animal():
    def eat(self):
        print("i can eat")
class Dog(Animal):
    def bark(self):
        print("i can bark")
class Cat(Animal):
    def drink(self):
        print("my favret is milk")

dog1=Dog()
dog1.bark()
dog1.eat()

cat=Cat()
cat.drink()