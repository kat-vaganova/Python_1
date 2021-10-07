# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


product_template = {
    'название': ("имя товара", str),
    'количество': ('количество товара', int),
    'цена': ('стоимость товара', int),
}
type_product = {'тип': ('тип оргтехники (принтер, сканер, копир)', str)}
count_product = {'количество': ('количество товара', int)}

auto_inc = 1
products_list = []
next_enter = True

while next_enter:
    product = {}
    for key, value in product_template.items():
        user_value = input(f'{value[0]}\n')
        try:
            user_value = value[1](user_value)
        except ValueError:
            print(f"Не верное значение данных")
            user_value = input(f'{value[0]}\n')
        product[key] = user_value

    for key, value in type_product.items():
        user_value = input(f'{value[0]}\n')
        if user_value in ("принтер", "сканер", "копир"):
            product[key] = user_value == "принтер" or user_value == "сканер" or user_value == "копир"
            product[key] = user_value
        else:
            print(f"Не верное значение данных")
            user_value = input(f'{value[0]}\n')

    products_list.append((auto_inc, product))
    auto_inc += 1

    while True:
        next_add = input("Добавить еще продукт? да/нет\n")
        if next_add in ("да", "нет"):
            next_enter = next_add == "да"
            break

print(products_list)


class Stock:
    type: str = 'offise_equipment'
    amount: int
    max_count: int = 20

    def __init__(self, amount, type = 'offise_equipment'):
        self.amount = amount
        self.type = type

#  поступление
    def __add__(self, other):
        products_analytics = {}
        for key in count_product:
            amount = []
            for itm in products_list:
                amount.append(itm[1][key])
            products_analytics[key] = amount
        #     self.amount = sum(amount)
        # print(products_analytics)
        self.amount += other.amount
        return self
        # print(self.amount)

# выдача
    def __isub__(self, other):
        self.amount -= other.amount
        # Stock.__isub__(self.amount)
        return self.amount


class Equipment:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(Equipment):
    def __init__(self, name, prise, print_speed):
        super().__init__(name, prise)
        self.print_speed = print_speed


class Scanner(Equipment):
    def __init__(self, name, prise, scanning_speed):
        super().__init__(name, prise)
        self.scanning_speed = scanning_speed


class Copier(Equipment):
    def __init__(self, name, prise, copying_speed):
        super().__init__(name, prise)
        self.copying_speed = copying_speed
