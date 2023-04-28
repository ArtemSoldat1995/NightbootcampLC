# class Zoo:
#     def __init__(self):
#         self.animal_1 = 'Тигр'
#         self.animal_2 = 'Бегемот'
#         self.animal_3 = 'Жираф'

# z = Zoo()

# '''Изменения "Тигр" на "Лев"'''
# z.animal_1 = 'Лев'
# print(z.animal_1)

# '''Добавление нового атрибута list'''
# z.animal_4 = [z.animal_2, z.animal_3]
# print(z.animal_4)

# '''Изменение "Жираф" на "Змея"'''
# z.animal_3 = 'Змея'
# print(z.animal_3)



# class Factory:
#     def __init__(self):
#         self.engine = 'Двигатель создан'
#         self.bridge = 'Ходовая часть создана'
# f = Factory()

# class Toyota(Factory):
#     def __init__(self):
#         self.wheels = 'Колеса готоввы'
#         self.windows = 'Стекла готовы'

# t = Toyota()
# t.list = [f.engine, f.bridge,t.wheels, t.windows]
# print(t.list)