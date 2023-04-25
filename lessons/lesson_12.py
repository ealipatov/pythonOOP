def hands_washer(func):  # На вход принимаем функцию
    def inner(arg):
        print("Моем руки")
        func(arg)
        print("Моем руки")

    return inner


def eat(arg):
    print(f"Кушаю {arg}")


def eat_2(func, arg):
    print("Моем руки")
    func(arg)
    print("Моем руки")


hands_washer(eat)("Мясо")  # Сокращенное написание:
# clear_eat = hands_washer(eat)
# clear_eat()

eat_2(eat, "Сало")
