class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"


print(Person("Alex", 25))