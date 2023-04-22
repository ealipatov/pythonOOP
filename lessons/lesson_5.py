class Dog:
    animal_type = " Собака"

    def __init__(self, name, age):
        self.dog_name = name
        self.age = age

    def __str__(self):
        return f"{self.dog_name}, {self.age}, {Dog.animal_type}"
        # return f"{self.dog_name}, {self.age}, {self.animal_type}"


dog = Dog("Палкан", 2)
print(dog.dog_name)
print(dog)
print(Dog.animal_type)