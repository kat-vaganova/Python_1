# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open('salaries.txt') as text:
    # с прочтением
    data = text.read()
    # количество строк (два способа)
    line_count = len(data.splitlines())
    print(f"Количество строк (способ 1): {line_count}")
    line_count_2 = len(data.split("\n"))
    print(f"Количество строк (способ 2): {line_count_2}")

    words_oll = len(data.split())  # количество слов в документе
    print(f"Количество слов во всем документе: {words_oll}")

    # количество слов в каждой строке
    for ind, l in enumerate(data.splitlines(), 1):
        words = len(l.split(" "))
        print(f"Количество слов в {ind} строке: {words}")

with open('salaries.txt') as text:

    # без чтения (если файл большой)
    line_count_3 = 0
    for line in text:
        line_count_3 += 1
    print(f"Количество строк (способ 3): {line_count_3}")




