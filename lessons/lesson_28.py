list1 = list(range(1, 20))

print(list1)

list2 = []

for elem in list1:
    list2.append(elem * elem)

print(list2)


def plus_2(elem):
    return elem + 2


# генератор списка с функцией в логике:
print([plus_2(elem) for elem in list1 if elem < 10])

# генератор списка:
list3 = [elem * elem for elem in list1]
print(list3)

# запись с помощью лямбды
print(list(map(lambda el: plus_2(el), list1)))

# генератор словарей
dict1 = {elem: elem * elem for elem in list1}
print(dict1)

data = ["Молоко", "Кефир", "Масло"]

dict2 = {elem: len(elem) for elem in data}
dict3 = {elem: len(elem) for elem in data if len(elem) > 5}
print(dict2, "\n", dict3)
print({key.upper(): value for key, value in dict2.items()})
