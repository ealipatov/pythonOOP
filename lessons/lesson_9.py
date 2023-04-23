class Dog:
    def __init__(self, name, age):
        self.__dog_name = name
        self.__age = age

    def set_name(self, name):
        self.__dog_name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__dog_name

    def get_age(self):
        return self.__age


dog = Dog("Тузик", 5)

print(dog.get_name())