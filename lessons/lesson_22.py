class Animals:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def do_sound():
        print("Звук животного")

    def get_name(self):
        print(f"Меня зовут: {self.name}")


class Dog(Animals):

    def do_sound(self):
        print("Gav")

    @staticmethod
    def play_game():
        print("Я люблю приносить палку")


class Spiz(Dog):
    @staticmethod
    def spiz_method():
        print("Вилять хвостом")


class my_int(int):
    pass


# Выведем на экран имя класса:
print(Animals.__name__)
print(str.__name__)

# Проверяем наследование
print(issubclass(Spiz, Dog))
print(issubclass(Spiz, Animals))
print(issubclass(Dog, Spiz))

dog = Dog("Тузик")

print(isinstance(dog, Dog))
print(isinstance(dog, Animals))
print(isinstance(dog, Spiz))

print(isinstance(1, int))