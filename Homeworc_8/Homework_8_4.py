# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Stock:
    pass


class Equipment:

    def __init__(self, color, price):
        self.color = color
        self.price = price


class Printer(Equipment):
    def __init__(self, color, prise, print_speed):
        super().__init__(color, prise)
        self.print_speed = print_speed


class Scanner(Equipment):
    def __init__(self, color, prise, scanning_speed):
        super().__init__(color, prise)
        self.scanning_speed = scanning_speed


class Copier(Equipment):
    def __init__(self, color, prise, copying_speed):
        super().__init__(color, prise)
        self.copying_speed = copying_speed
