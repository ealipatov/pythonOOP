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


dog = Dog("Fedor")

dog.get_name()
dog.do_sound()
