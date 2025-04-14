
# 🐍 Classes & Objects in Python

## 📘 What is a Class?

A **Class** is a blueprint or template for creating objects. It defines attributes (variables) and behaviors (methods/functions) that the objects created from it will have.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")
```

---

## 🧱 What is an Object?

An **Object** is an instance of a class. It represents a specific "thing" created using the class structure.

```python
p1 = Person("Sathish")  # p1 is an object
p1.greet()
```

---

## ⚙️ Important Components

| Concept        | Description |
|----------------|-------------|
| `class`        | Keyword used to define a class |
| `__init__()`   | Constructor method, runs when an object is created |
| `self`         | Refers to the current instance of the class |
| Object         | A variable that stores an instance of the class |

---

## 🎯 Example: Class and Object

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        print(f"Car: {self.brand} {self.model}")

# Creating objects
car1 = Car("Toyota", "Innova")
car2 = Car("Honda", "Civic")

car1.details()
car2.details()
```

---

## 🧠 Key Concepts

- **Instance Variables** – Belong to the object (`self.name`)
- **Class Variables** – Shared across all objects
- **Methods** – Functions defined inside a class
- **Encapsulation** – Keeping data and behavior in one unit (class)

---

## 📌 Object Operations

| Operation           | Example                        |
|---------------------|--------------------------------|
| Access attributes   | `obj.name`                     |
| Call methods        | `obj.greet()`                  |
| Modify attributes   | `obj.name = "New Name"`        |
| Delete object       | `del obj`                      |

---

## ✅ Benefits of Using Classes & Objects

- Code Reusability
- Organized Structure (OOP)
- Real-world modeling
- Easy maintenance and scalability

---

## 💡 Fun Fact

Python supports **multiple objects** from a single class and even **dynamic attribute assignment**!

```python
class Demo: pass

obj = Demo()
obj.new_attr = "Hello"
print(obj.new_attr)  # Hello
```
