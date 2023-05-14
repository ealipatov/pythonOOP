list1 = list(range(1, 20))

print(list1)

list2 = []

for elem in list1:
    list2.append(elem * elem)

print(list2)


def plus_2(elem):
    return elem + 2


# генератор списка с функцией в логике:
print([plus_2(elem) for elem in list1])

# генератор списка:
list3 = [elem * elem for elem in list1]
print(list3)

# запись с помощью лямбды
print(list(map(lambda el: plus_2(el), list1)))
