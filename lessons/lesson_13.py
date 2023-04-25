import time


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


fu()
