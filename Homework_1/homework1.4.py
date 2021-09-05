# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

value = int(input("Введите число: "))
max_number = value % 10
value = value // 10
while value > 0:
    if value % 10 > max_number:
        max_number = value % 10
    value = value // 10
print("Самая большая цифра в числе: ", max_number)

