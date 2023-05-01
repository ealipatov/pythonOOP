class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return hash(self) == hash(other)


dog1 = Dog('Шарик', 2)
dog2 = Dog('Шарик', 2)
dog3 = Dog('Тузик', 3)

print(hash(dog1))
print(hash(dog2))
print(hash(dog3))
print(dog1 == dog2)
print(dog1 == dog3)