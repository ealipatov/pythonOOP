from dataclasses import dataclass


class DBSaver:
    def __init__(self, arg1):
        self.arg1 = arg1

    def save_to_DB(self):
        print(f"Saved to DB: {self}")


class XlsxSaver:
    def __init__(self, arg1):
        self.arg1 = arg1

    def save_to_exel(self):
        print(f"Saved to xlsx: {self}")


@dataclass(frozen=True)
class Car(DBSaver, XlsxSaver):
    model: str
    year: int


@dataclass(frozen=True)
class Student(DBSaver, XlsxSaver):
    first_name: str
    last_name: str


car = Car("Lada", 2018)
student = Student("Ivan", "Ivanov")
to_save = [car, student]

for elem in to_save:
    elem.save_to_DB()
    elem.save_to_exel()


# MRO порядок вызова методов
# print(Car.__mro__)