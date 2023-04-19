# def create_coockies(water, flour, sugar = True):
#     if sugar:
#         print('Вы решили приготовитть сладкие печеньки!')
#         if water > flour:
#             raise 'Много воды, чем муки!'
#         else:
#             return water * flour

# create_coockies(4, 2)


def add(a: int, b: int):
    c = a + b
    print(c)
    return


# def substract(a: int, b: int):
#     c = a - b
#     print(c)
#     return c

# # substract(2,7)

# def multiply(a: int, b: int):
#     c = a * b
#     print(c)
#     return c

# def divide(a: int, b: int):
#     c = a / b
#     print(c)
#     return c

# divide(13,2)


# def function_a(text: str):
#     count = 0
#     for i in text:
#         count += 1
#     return count



# a = function_a()
# print(a)

# def add_two_dict(dict1, dict2):
#     dict1.update(dict2)
#     return dict1

# a = add_two_dict({'name': 1},{'age': 2})
# print(a)

def food():
    food_1 = str(input('Назовите еду:'))
    drinks = str(input('Чтобы бы вы выпили?: '))
    menu_1 = food_1 + drinks
    menu_2 = menu_1.split()
    return menu_2


x = food()
print(x)




