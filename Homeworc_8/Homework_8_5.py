# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие
# за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

product_template = {
    'название': ("имя товара", str),
    'цена': ('стоимость товара', int)
                    }

count_product = {'количество': ('количество товара', int)}
type_product = {'тип': ('тип оргтехники (принтер, сканер, копир)', str)}

products_list = [
                (1, {"название": "Bruther", "цена": 20000, "количество": 5, "тип": "принтер"}),
                (2, {"название": "Xserox", "цена": 6000, "количество": 2, "тип": "копир"}),
                (3, {"название": "HP", "цена": 2000, "количество": 7, "тип": "сканер"})
                ]

# print(products_list)
#
# products_analytics = {}
#
# # собираем словарь аналитики
# for key in count_product:
#     result = []
#     for itm in products_list:
#         result.append(itm[1][key])
#     products_analytics[key] = result
#
#     # products_analytics[key] = [itm[1][key] for itm in products_list]
# print(products_analytics)


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
