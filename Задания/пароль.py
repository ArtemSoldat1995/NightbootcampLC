password = input('Введите пароль: ')
password_1 = input('Подтвердите пароль: ')
while password != password_1:
    print('Пароли не совпадают')
    print('Введите снова')
    password = input('Введите пароль: ')
    password_1 = input('Подтвердите пароль: ')
print('Все верно!')