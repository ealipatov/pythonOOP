from dataclasses import dataclass


@dataclass()
class Person:
    name: str
    age: int


print(Person("Alex", 25))