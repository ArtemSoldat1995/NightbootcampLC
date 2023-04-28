# class Phone:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f'phone - {self.name}'


# class SmartPhone(Phone):
#     def __init__(self, name, camera):
#         super().__init__(name)
#         self.camera = camera

#     def photo(self):
#         return 'Снимок сделан'

#     def info(self):
#         return f'Phone - {self.name}\nCamera - {self.camera}'


# class Iphone(SmartPhone):
#     def __init__(self, name, camera, internet):
#         super().__init__(name, camera)
#         self.internet = internet

#     def change_name(self, new_name):
#         self.name = new_name





class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def info(self):
        return f'Number - {self.number}\nModel - {self.model}\nWeight - {self.weight}'



    def sendMessage(self,number):
        self.number = number
        return f'На {self.number} сообщение отправлено'

ph = Phone(3110, 'Nokia', 123)
print(ph.info())
print(ph.sendMessage(3110))
    


    










