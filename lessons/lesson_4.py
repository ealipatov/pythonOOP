# *args - набор аргументов
# **wkargs - набор аргументов с параметрами

# a, b, c = "a", "b", "c"
# a, b, c = ("a", "b", "c")
# a, b, c = ["a", "b", "c"]
# d = ["a", "b", "c"]
# print(a, b, c)
# print(d)

# a, b, *c = ["a", "b", "c", "d"]
# print(a, b, c)

# *a, b, c = ["a", "b", "c", "d"]
# print(a, b, c)
#
# nums = [1, 10]
# print(list(range(1, 5)))
# print(list(range(*nums)))
#
# print(1, 2, 3)
# print([1, 2, 3])
# print(*[1, 2, 3])

# def sum_numbers(*numbers):
#     res = 0
#     for number in numbers:
#         res += number
#     print(res)
#
#
# sum_numbers(1, 2, 3 ,4 , 5)

# print (1, 2, 3, 4)
# print (1, 2, 3, 4, sep="\n")

def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, "a", [1, 2, 3], key1="123", key2="234")
