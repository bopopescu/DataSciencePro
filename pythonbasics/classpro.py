class Myclass:

    name = "APsmind"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")

    def myclass1(self):
        print("Function Working")
        print("Name:", self.name)
        print("Age:", self.age)


a = Myclass("Ajay", 21)
a.myclass1()
print(Myclass.name)


class Car:
    pass


ferrari = Car()
ferrari.model = "2018"
ferrari.cost = "Kabade k bhaw"
print(ferrari.__dict__)


class Animal:
    def speack(self):
        print("hahahhaah,...")


class Dog(Animal):
    def bark(self):
        print("bhoobhooo")


tomy = Dog()
tomy.speack()

