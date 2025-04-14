class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()  # my_dog is an object
my_dog.bark()

class Person:
    def say_hello(self):
        print("Hello!")

p1 = Person()
p1.say_hello()


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}")

p = Person("Sathish")
p.greet()

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

l1 = Laptop("HP", "8GB")
print(l1.brand, l1.ram)

class Employee:
    company = "Google"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

e1 = Employee("Alice")
e2 = Employee("Bob")
print(e1.name, e1.company)
print(e2.name, e2.company)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_details(self):
        print(f"{self.brand} {self.model}, {self.year}")

c = Car("Toyota", "Camry", 2020)
c.show_details()

class Calculator:
    def input_numbers(self):
        self.a = 10
        self.b = 20
        self.add()

    def add(self):
        print(self.a + self.b)

calc = Calculator()
calc.input_numbers()

class Demo:
    def show(self):
        print("This is:", self)

d = Demo()
d.show()

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 50:
            return 'C'
        else:
            return 'F'

s = Student("Sathish", 101, 88)
print(f"{s.name}'s Grade:", s.get_grade())


class Secret:
    def __init__(self):
        self.__password = "hidden"  # private variable

    def __hidden_method(self):  # private method
        print("You found the secret!")

    def access_secret(self):
        self.__hidden_method()

s = Secret()
s.access_secret()


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):  # overriding
        print("This is Child class")

c = Child()
c.show()

class MyClass:
    class_var = 0

    def __init__(self):
        MyClass.class_var += 1

    @classmethod
    def show_count(cls):
        print("Objects created:", cls.class_var)

    @staticmethod
    def greet():
        print("Hello from static method")

MyClass()
MyClass()
MyClass.show_count()
MyClass.greet()


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def total_objects(cls):
        print("Total objects created:", cls.count)

a = Counter()
b = Counter()
c = Counter()
Counter.total_objects()
