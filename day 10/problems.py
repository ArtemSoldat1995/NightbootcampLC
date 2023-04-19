# import os
# name = os.name
# print(name)
import random
try:
    correct_answer = 0
    wrong_answer = 0
    while True:
        max_value = int(input('Привет, выбери максимальное значение: '))
        x = random.randint(0, max_value)
        y = random.randint(0, max_value)
        print('Сколько будет:', x, "*", y)
        answer = int(input())
        if answer == x * y:
            correct_answer += 1
            print('Верно!')
        elif answer != x * y:
            print('Неправильно!')
            wrong_answer += 1
            break
    print('Правельных ответов: ', correct_answer, 'Непрвельных ответов: ', wrong_answer)
except:
    print('Введите только числа')


