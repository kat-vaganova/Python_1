# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(*numbers):
    list_revers = list(reversed(sorted(numbers)))
    return list_revers[0] + list_revers[1]


print(my_func(4, 2, 8))