# 1. Реализовать функцию,
# принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def d_calc():
    try:
        value_1 = float(input("Укажите число: "))
        value_2 = float(input("Укажите число: "))
    except ValueError:
        return
    # деление чисел
    try:
        result = value_1 / value_2
    except ZeroDivisionError:
        return
    return result


result_end = d_calc()
print(result_end)