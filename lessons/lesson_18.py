class Product:
    def __init__(self, products, bonuses=0):
        self.products = products
        self.bonus = bonuses

    def get_sum_all_prise(self):
        return sum(self.products.values()) - self.bonus

    def __add__(self, other):
        if isinstance(other, int):
            return Product(self.products, self.bonus + other)
        elif isinstance(other, Product):
            new_product = {}
            for name, prise in self.products.items():
                if name not in new_product:
                    new_product[name] = prise
            for name, prise in other.products.items():
                if name not in new_product:
                    new_product[name] = prise
            return Product(new_product)

    def __radd__(self, other):
        if isinstance(other, int):
            return Product(self.products, self.bonus + other)


product1 = Product({'Молоко': 2, 'Сыр': 13})
product2 = Product({'Кефир': 3, 'Масло': 4})
product3 = product1 + product2
product4 = product3 + 10
print(product1.get_sum_all_prise(), product1.products)
print(product3.get_sum_all_prise(), product3.products)
print(product4.get_sum_all_prise())
