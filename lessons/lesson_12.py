def hands_washer(func):  # На вход принимаем функцию
    def inner(*args, **kwargs):
        print("Моем руки")
        func(*args, **kwargs)
        print("Моем руки")

    return inner


def eat(meal1, meal2):
    print(f"Кушаю: {meal1} и {meal2}")


def eat_2(func, *args):
    print("Моем руки")
    func(*args)
    print("Моем руки")


hands_washer(eat)("Мясо", "Сыр")  # Сокращенное написание:
# clear_eat = hands_washer(eat)
# clear_eat()

eat_2(eat, "Сало", "Хлеб")
