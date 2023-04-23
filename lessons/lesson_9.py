class Dog:

    __MIN_AGE = 0
    __MAX_AGE = 40

    @classmethod
    def __check_age(cls, age):
        if type(age) != int:
            raise TypeError("Введен некорректный возраст")
        elif not cls.__MIN_AGE <= age <= cls.__MAX_AGE:
            raise TypeError("Возраст не может быть меньше нуля и больше 40")
        else:
            return age

    @classmethod
    def __check_name(cls, name):
        if type(name) != str:
            raise TypeError("Имя может быть только строкой")
        else:
            return name

    def __init__(self, name, age):
        self.__dog_name = self.__check_name(name)
        self.__age = self.__check_age(age)

    @property
    def name(self):
        return self.__dog_name

    @name.setter
    def name(self, name):
        self.__dog_name = self.__check_name(name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = self.__check_age(age)


dog = Dog("Тузик", 40)
print(dog.name, dog.age)
dog.age = 15
print(dog.name, dog.age)
