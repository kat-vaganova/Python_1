# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_rus = {'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'
            }
new_file = []
with open('text_4.txt') as text:
    data = text.readlines()
    for i in data:
        i = i.split(" ", 1)
        new_file.append(dict_rus[i[0]] + ' ' + i[1])
    print(*new_file)

with open("text_4_new.txt", "x") as text:
    print(*new_file, file=text)

