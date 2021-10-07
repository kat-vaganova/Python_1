# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    date_string: str

    def __init__(self, date_string):
        self.data_string = date_string

    @classmethod
    def convert_date(cls, date_string):
        day, month, year = map(int, date_string.split("-"))
        Date.validation_data(day, month, year)

    @staticmethod
    def validation_data(d, m, y):
        if (0 < d <= 31) and (0 < m <= 12) and (0 < y <= 9999):
            print(f"{d} {m} {y}")
        else:
            print(f"Неверная дата!")


Date.convert_date("01-55-2021")
Date.convert_date("01-12-2001")

