age = 18


def f():
    global age  # Разрешаем использование глобальной переменной
    age = 20
    print(age)


def f2():
    age = 19

    def f3():
        nonlocal age  # Разрешаем использовать предыдущую локальную переменную
        age = 21
        print(age)

    f3()
    print(age)


f()
f2()
