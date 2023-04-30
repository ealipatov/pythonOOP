class Product:
    def __init__(self, products, bonuses=0):
        self.products = products
        self.bonus = bonuses

    def get_sum_all_prise(self):
        return sum(self.products.values())

    def __add__(self, other):
        if isinstance(other, int):
            return Product(self.products, self.bonus + other)
        elif isinstance(other, Product):
            new_product = {}
            for name, price in self.products.items():
                if name not in new_product:
                    new_product[name] = price
            for name, price in other.products.items():
                if name not in new_product:
                    new_product[name] = price
            return Product(new_product, self.bonus)

    def __radd__(self, other):
        if isinstance(other, int):
            return Product(self.products, self.bonus + other)

    def __sub__(self, other):
        if isinstance(other, int):
            return Product(self.products, self.bonus - other)
        elif isinstance(other, str):
            new_products = {}
            for name, price in self.products.items():
                if name != other:
                    new_products[name] = price
            return Product(new_products, self.bonus)
        elif isinstance(other, Product):
            new_products = {}
            new_bonus = self.bonus - other.bonus
            for name, price in self.products.items():
                if name not in other.products:
                    new_products[name] = price
            return Product(new_products, new_bonus)

    def __rsub__(self, other):
        if isinstance(other, int):
            return Product(self.products, self.bonus - other)
        elif isinstance(other, str):
            new_products = {}
            for name, price in self.products.items():
                if name != other:
                    new_products[name] = price
            return Product(new_products, self.bonus)


def print_product(product):
    print(f"Сумма: {product.get_sum_all_prise()}, Бонусов: {product.bonus}, "
          f"Итого: {product.get_sum_all_prise() - product.bonus}, {product.products}")


product1 = Product({'Молоко': 2, 'Сыр': 13})
product2 = Product({'Кефир': 3, 'Масло': 4})
product2 += 1
product3 = product1 + product2
product3 = product3 + 5
product4 = product3 - "Сыр"
product4 += 2
product5 = product4 - product2
product6 = 1 - product3
product6 -= "Масло"

print_product(product1)
print_product(product2)
print_product(product3)
print_product(product4)
print_product(product5)
print_product(product6)
