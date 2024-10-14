class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        current_products = self.get_products().splitlines()
        current_product_descriptions = {line for line in current_products}

        with open(self.__file_name, 'a') as file:
            for product in products:
                if str(product) not in current_product_descriptions:
                    file.write(f"{str(product)}\n")
                    current_product_descriptions.add(str(product))
                else:
                    print(f"Продукт {str(product)} уже есть в магазине")


# Пример использования

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p3 = Product('Potato', 5.3, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
