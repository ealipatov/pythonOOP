class Dog:

    __MIN_AGE = 0
    __MAX_AGE = 40

    @classmethod
    def __check_age(cls, age):
        if type(age) != int:
            raise TypeError("Введен некорректный возраст")
        elif cls.__MIN_AGE <= age <= cls.__MAX_AGE:
            raise TypeError("Возраст не может быть меньше нуля и больше 40")
        else:
            return age

    def __init__(self, name, age):
        self.__dog_name = name
        self.__age = self.__check_age(age)

    def set_name(self, name):
        self.__dog_name = name

    def set_age(self, age):
        self.__age = self.__check_age(age)

    def get_name(self):
        return self.__dog_name

    def get_age(self):
        return self.__age


dog = Dog("Тузик", 1)

print(dog.get_age())
