# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.
#

with open("test.txt", "x") as text_1:
    while True:
        text = input("Введите текст: ")
        if text:
            text_1.write(text + '\n')
        else:
           break

with open("test.txt") as text_1:
    print(text_1.read())





