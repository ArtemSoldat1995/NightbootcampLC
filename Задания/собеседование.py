lang = input('Ваш яп: ')
age = int(input('Ваш возраст: '))
exp = int(input('Ваш опыт: '))
salary = int(input('Желаемая зарплата: '))
if lang == 'python' or lang == 'java' or lang == 'javascript':
    if 18 < age < 65 and exp >= 3:
        if salary <= 60000:
            print('Вы нам подходите!')
else:
    print('Вы не подходите!')