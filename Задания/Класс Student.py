class Student:
    def __init__(self, name, lastname, departament, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.departament = departament
        self.year_of_entrance = year_of_entrance

#Отформатированный вид
    def data(self):
        return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} {self.departament}'
    
st = Student('Вася', 'Иванов', 'на факультет', 2017)
print(st.data())
