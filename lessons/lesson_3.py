class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Объект кот с именем: {self.name} создан")

    def __del__(self):  # Не гарантировано время удаления объекта (не знаем когда)
        print(f"Кот {self.name} закончился")


cat = Cat("Васька", 1)
print(cat.__dict__)
cat2 = Cat("Жорик", 2)
