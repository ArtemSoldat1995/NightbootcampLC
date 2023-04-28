class Ractangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
#Длинна и шарина прямоугольника
    def data(self):
        return f'Длинна: {self.length}\nШирина: {self.width}'

#Площадь Прямоугольника
    def aria_ractangle(self):
        s = self.length * self.width
        return f'\nПлощадь прямоугольника: {s}'

#Периметр прямоугольника    
    def perimeter(self):
        p = (self.length + self.width) * 2
        return f'\nПериметр прямоугольника: {p}'


s = Ractangle(40, 20)
print(s.data(), s.aria_ractangle(), s.perimeter())

  
           
        