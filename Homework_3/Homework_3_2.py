# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(first_name, last_name, year_berthday, sity, email, thone_number):
    print(f'{first_name}, {last_name}, {year_berthday}, {sity}, {email}, {thone_number}')


user(first_name='Ivan', last_name='Ivanov', year_berthday = '01.01.2001', sity = 'Moskow', email='123@yandex.ru', thone_number = '89112335656')

