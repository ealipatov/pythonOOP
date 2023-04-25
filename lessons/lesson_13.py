import time
import requests


def time_counting(func):  # На вход принимаем функцию
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        finish_time = time.time()
        print(f"Функция выполнялась: {finish_time - start_time}")
        return res

    return inner


@time_counting
def fu():
    time.sleep(1)
    print("213213123")


# На рекурсивных функциях декораторы вызываются много раз (сколько происходит рекурсия)
def fibonachi(num):  # Рекурсивная функция расчета числа Фибоначи
    if num in range[1, 2]:
        return num
    return fibonachi(num - 1) + fibonachi(num - 2)


@time_counting
def f3():
    res = requests.get("https://www.google.by/")
    res1 = requests.get("https://www.google.by/")
    res2 = requests.get("https://www.google.by/")
    print()


fu()
f3()
