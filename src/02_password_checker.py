"""
Пример программы для работы с условиями

Данные
- переменная со значением пароля password = 123123
- пользователь вводит строку с паролем

Сделать
- если пароль верный, вывести строку "Пароль верный"
- если пароль неверный, вывести строку "Ошибка"
"""
password = "hello"

user_pass = input("Пароль >>> ")

if password == user_pass:  # >, < , !=, is not, ...
    print("Ok")
    print('Password recognized')
else:
    print('Not ok')
