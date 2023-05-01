from abc import ABC, abstractmethod


class Printable(ABC):  # Пример интерфейса (класс который содержит абстрактный метод)
    @abstractmethod
    def pretty_print(self):
        pass

    def final_print(self):
        print("=" * 80)
        self.pretty_print()
        print("=" * 80)


class Car(Printable):
    def pretty_print(self):
        print("===Машина едет===")


class Dog(Printable):
    def pretty_print(self):
        print("===Собака лает===")


class Cat(Printable):
    def pretty_print(self):
        print("===кот мяукает===")


car = Car()
dog = Dog()
cat = Cat()

printable = [car, dog, cat]
for obj in printable:
    obj.final_print()


class BirthDay(ABC):
    def get_name(self):
        pass

    def print_final(self):
        print(f"С днем рождения {self.get_name()} !")


class Student(BirthDay):
    def get_name(self):
        return "Иван"


class Tither(BirthDay):
    def get_name(self):
        return "Василий"


student = Student()
tither = Tither()

printable = [student, tither]
for obj in printable:
    obj.print_final()
