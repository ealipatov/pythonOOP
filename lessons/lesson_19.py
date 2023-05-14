class Product:
    def __init__(self, products, bonuses=0):
        self.products = products
        self.bonus = bonuses

    def get_sum_all_prise(self):
        return sum(self.products.values())

    def __eq__(self, other):
        res = False
        if len(self.products) == len(other.products):
            for name, price in self.products.items():
                if name in other.products and other.products[name] == price:
                    res = True
                else:
                    return False
        return res

    def __gt__(self, other):
        return self.get_sum_all_prise() > other.get_sum_all_prise()

    def __ge__(self, other):
        return self.get_sum_all_prise() >= other.get_sum_all_prise()


def print_product(product):
    print(f"Сумма: {product.get_sum_all_prise()}, Бонусов: {product.bonus}, "
          f"Итого: {product.get_sum_all_prise() - product.bonus}, {product.products}")


product1 = Product({'Кефир': 3, 'Сыр': 13})
product2 = Product({'Кефир': 4, 'Масло': 4})
product3 = Product({'Кефир': 3, 'Масло': 4})

print(product3 == product2)
print(product3 >= product2)
