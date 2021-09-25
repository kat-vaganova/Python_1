
# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.


from random import randrange
list = [randrange(1, 100) for i in range(7)]

with open("text_5.txt", "x") as text:
    print(*list, file=text)

with open("text_5.txt", "r") as text:
    data = text.read()
    total = sum(int(i) for i in data.split(" "))
    print(f"Сумма чисел {total}")
