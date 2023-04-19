
# data = set()
# for i in range(5):
#     data.add(int(input('Введите числа: ')))
# print(data)
# print('Самое маленькое число:', min(data))

# sum = int(input('Введите сумму: '))
# if sum >= 50000:
#     a = sum * 3.47 / 100
#     print(round(a, 2))
# elif sum < 50000:
#     print('Сумма должна быть от 50000')

# my_file = open('people.txt', 'w')
# name = input('Введите имя: ')
# my_file.write(name)
# my_file.close()   

# my_file = open('people.txt', 'r')
# data = my_file.read()
# my_file.close()
# print(data)

# with open('user.txt', 'w') as my_file:
#     login = input()
#     password = input()
#     my_file.write(login + '' + password)

# file = open('people.txt','r')
# data = file.read()
# if 'w' in data:
#     print('yes')
# else:
#     print('no')

# file = open('python.txt', 'w')
# txt = input('Введите текст: ')
# file.write(txt)
# file.close()

# Python is a widely used high-level programming language for general-purpose

# programming, created by Guido van Rossum and first released in 1991. An interpreted

# language, Python has a design philosophy that emphasizes code readability (notably

# using whitespace indentation to delimit code blocks rather than curly brackets or

# keywords), and a syntax that allows programmers to express concepts in fewer lines of

# code than might be used in languages such as C++ or Java.

# file = open('python.txt', 'w')
# txt = input('Введите текст: ')
# file.write(txt)
# file.close()

# file = open('python.txt', 'r')
# data = file.read()
# t_words = []
# for i in data:
#     if 't' in i:
#         t_words.append(i)
#         print(t_words)

# Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя войти 
# или зарегистрироваться. 
# Спросите его логин и пароль. Если такой логин уже есть скажите ему что логин уже существует
# и предложите зарегистрироваться спросив пароль. 
# Если такого логина неоказалось среди уже существющих продолжайте регистрацию.
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.

a = 'dastan 123  ilan 321  ulan 456'
with open('database.txt', 'w') as f:
    f.write(a)

with open('database.txt', 'r') as f:
    data = f.read()

users = data.split('  ')
print(users)

login = input()
password = input()
for i in users:
    if login == i.split(' ')[0]:
        print('user already exist, input password')
        password1 = int(input())
        while True:
            if password == password and password1 == i.split(' ')[1]:
                print('password accepted')
                break
            else:
                print('try again')
        break
else:
    password2 = input()
    if password == password2:
        with open('database.txt', 'a') as f:
            f.write('  ' + login + ' ' + password)
            print('Регистрация прошла успешно')


