# Класс который называется парковка
# С конструктором инит 
# Принимает аттрибуты(макс кол-во мест, )
# аттрибуты- кол-во мест, список машин[пустой] который принимает в себе объекты экземпляра класса car, 
# записи - dictinary {в котором будут все таллоны и информация о том какая машина заехала и когда уехала,
#  булиан которая обозначает находится на парковке машина или нет },  талоны должны быть сгенерированны
# рандомно и должны быть уникальны
# методы - 1. Вызывается addCar принимает в себя аргумент класса Car, метод должен добавить в наш
# аттрибут 'Машины' и добавляет новый элемент в записи талон и если машина не уехала, то поле когда
# уехала машина возвращает  none
# метод - 2 Вызывается out_car(«talon») вы ищите талон и в записях добавляете время выхода машины
#  а также булиан ставите фалс о том что машины нет в парковке, а также удилите машину из списка Машины
# Добавьте также разные методы чтобы просмотреть детально запись о машине итд
class Parking:
    def __init__(self);
        self.amt = 