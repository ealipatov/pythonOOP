class Animals:
    @staticmethod
    def do_sound():
        print("Звук животного")


class Dog(Animals):

    def do_sound(self):  # Переопределение
        print("Gav")

    @staticmethod
    def play_game():  # Расширение
        print("Я люблю приносить палку")
