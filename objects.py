class Dog:
    def bark(self):
        print("Woof!")

dog1 = Dog()  # dog1 is an object
dog1.bark()

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Sathish")  # object of Student
print(s1.name)

class Fruit:
    def __init__(self, name):
        self.name = name

apple = Fruit("Apple")
banana = Fruit("Banana")

print(apple.name)
print(banana.name)

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

p1 = Person("Sathish")
p1.greet()

class Item:
    def __init__(self, name):
        self.name = name

i1 = Item("Pen")
# print(i1.price)  # AttributeError: 'Item' object has no attribute 'price'

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Python 101", "Mike")
b2 = Book("Learn JS", "John")

print(b1.title, "-", b1.author)
print(b2.title, "-", b2.author)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)  # False, different objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True


class User:
    pass

u1 = User()
u1.name = "Sathish"  # dynamic attribute
print(u1.name)

class Demo:
    def __init__(self):
        print("Object created")

obj = Demo()
del obj  # deletes the object


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Sathish", 90)
print(s1.__dict__)  # shows all attributes


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c1 = Circle(7)
print("Area:", c1.area())


class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l1 = Laptop("Dell", 60000)
l2 = Laptop("HP", 55000)

print(f"{l1.brand} - ₹{l1.price}")
print(f"{l2.brand} - ₹{l2.price}")


class Product:
    def __init__(self, name):
        self.name = name

p1 = Product("Mouse")
p2 = Product("Keyboard")
items = [p1, p2]

for item in items:
    print(item.name)

class Car:
    def __init__(self, color):
        self.color = color

my_car = Car("Red")
print(my_car.color)

my_car.color = "Blue"  # updating attribute
print(my_car.color)

class A:
    def show(self):
        print("Hello from A")

class B:
    def call_a(self):
        a = A()
        a.show()

b = B()
b.call_a()
