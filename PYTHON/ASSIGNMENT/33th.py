class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Anitesh")

try:
    print(p1.age)
except AttributeError:
    print("Error: Attribute does not exist")

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

try:
    num = int("hello")
except ValueError:
    print("Error: Invalid number value")

try:
    result = 5 + "5"
except TypeError:
    print("Error: Different data types cannot be added")
