def hands_washer(func):  # На вход принимаем функцию
    def inner(*args, **kwargs):
        print("Моем руки")
        res = func(*args, **kwargs)  # Если надо вернуть результат выполнения функциии
        print("Моем руки")
        return res  # Возвращаем результат выполнения функции

    return inner


def eat_2(func, *args):
    print("Моем руки")
    res = func(*args)
    print("Моем руки")
    return res


@hands_washer
def eat(meal1, meal2):
    print(f"Кушаю: {meal1} и {meal2}")
    return "Я покушал"


# @eat_2  # не работает
# def eat(meal1, meal2):
#     print(f"Кушаю: {meal1} и {meal2}")
#     return "Я покушал"
#

print(eat("Мясо", "Сыр"))

# print(hands_washer(eat)("Мясо", "Сыр"))  # Сокращенное написание:
# # clear_eat = hands_washer(eat)
# # clear_eat()
# print("=" *80)
# print(eat_2(eat, "Сало", "Хлеб"))
