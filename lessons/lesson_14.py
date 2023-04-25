def validate_age(min_age, max_age):  # Обертка для декоратораБ которая принимает значения и возвращает декоратор
    def decorator(func):  # Непосредственно сам декоратор
        def inner(*args, **kwargs):
            valid_args = []
            for arg in args:
                if type(arg) == int and min_age <= arg <= max_age:
                    valid_args.append(arg)
                else:
                    valid_args.append(None)
            res = func(*valid_args, **kwargs)

            return res

        return inner
    return decorator


@validate_age(min_age=1, max_age=120)
def print_age(age, age2):
    print(f"Введенный возраст: {age}, {age2}")


print_age(-1, 25)
# print(validate_age(-1))
# print(validate_age(130))
# print(validate_age("10"))
