class Dog:
    def __init__(self):
        print("Гав")

    def __call__(self, *args, **kwargs):
        print("вызов объекта как функции")
        print(args)


dog = Dog()
dog()
dog("собака сказала гав")