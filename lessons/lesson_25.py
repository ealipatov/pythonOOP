from dataclasses import dataclass, field


@dataclass(frozen=True)  # frozen=True - запрет на изменение данных в классе, можно без нее.
class Person:
    name: str
    age: int
    childs: list = field(default_factory=list)


person1 = Person("Alex", 25)
person2 = Person("Ben", 30)
print(person1)
print(person2)
person1.childs.append("Lusy")
print(person1)
print(person2)