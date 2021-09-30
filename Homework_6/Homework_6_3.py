# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def total_income(self):  # дохода с учетом премии
        return self._income.get("wage") + self._income.get("bonus")


class Position(Worker):

    def get_full_name(self):  # полное имя сотрудника
        print(f"{self.name} {self.surname}")

    def get_total_income(self):  # дохода с учетом премии
        print(f'{self.total_income()}')


employee1 = Position('Иван', 'Иванов', 'электрик', 25000, 5000)
employee1.get_full_name()
employee1.get_total_income()
