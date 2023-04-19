# list_1 = ['name', 'age', '1', '19']


# def reverse_list():
#     my_list1 = list_1[0:len(list_1)//2]
#     my_list2 = list_1[len(list_1)//2:len(list_1)]
#     total = my_list1[::-1] + my_list2[::-1]
#     print(total)

# reverse_list()
    
# Фибонначи

# def num_fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# print(list(num_fib(10)))

# def sum():
#     a = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))
#     c = a + b
#     print(c)

# # sum()

# def sumx():
#     r = int(input('Введите первое число: '))
#     f = int(input('Введите второе число: '))
#     v = r - f
#     print(v)

# sumx()

# def sum_2():
#     sum()
#     sumx()

# sum_2()

# name_file = input('Введите имя файла: ')
# def my_file():
#     with open(name_file, 'a+') as f:
#         f.read()

# my_file()

# a = my_file()
# print(a)


from random import choice

def gen_number():
    list = [1,4,5,7,9,0]
    list_2 = []
    
    for i in range(0, 6):
        a = choice(list)
        list_2.append(str(a))
    print(f'0444 {("".join(list_2))}')

gen_number()

# from random import choice

# def gen_number():
#     list = [1,4,5,7,9,0]
#     list_1 = []

#     for i in range(0,6):
#         digits = choice(list)
#         list_1.append(str(digits))

#     print(f'0444 {("".join(list_1))}')

# gen_number()