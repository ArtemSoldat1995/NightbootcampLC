class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def info(self):
        return f'Number - {self.number}\nModel - {self.model}\nWeight - {self.weight}'


#Отправляет сообщение на номер
    def sendMessage(self,number):
        self.number = number
        return f'На {self.number} сообщение отправлено'

ph = Phone(3110, 'Nokia', 123)
print(ph.info())
print(ph.sendMessage(3110))