def validate_age(func):
    def inner(*args, **kwargs):
        valid_args = []
        for arg in args:
            if type(arg) == int and 0 <= arg <= 120:
                valid_args.append(arg)
            else:
                valid_args.append(None)
        res = func(*valid_args, **kwargs)

        return res

    return inner


@validate_age
def print_age(age, age2):
    print(f"Введенный возраст: {age}, {age2}")


print_age(-1, 25)
# print(validate_age(-1))
# print(validate_age(130))
# print(validate_age("10"))
