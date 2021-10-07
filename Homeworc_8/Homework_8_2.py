# 2. Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


divider = float(input("Введите делимое: "))
denominator = float(input("Введите делитель: "))


class NullException(Exception):
    delimoe: float
    delitel: float

    def __init__(self, delimoe, delitel):
        self.delimoe = delimoe
        self.delitel = delitel

    def __str__(self):
        return f"На ноль делить нельзя!"


try:
    if denominator == 0:
        raise NullException(divider, denominator)

    print(f"Частное = {round(divider / denominator, 2)}")

except NullException:
    print("Ноль не может быть делителем.")



