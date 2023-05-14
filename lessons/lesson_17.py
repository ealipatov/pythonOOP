import time


class Timer:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        res = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time}")
        return res


@Timer
def func():
    print("1")
    time.sleep(0.5)
    print("2")


func()
