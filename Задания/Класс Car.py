class Car:
    def __init__(self, make, model, year, odometer = 0, fuel = 70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel

    def drive(self, km):
        fuel = km / 10
        if self.fuel >= fuel:
            self.__add_distance(km)
            self.__subtract_fuel(fuel)
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')
            
        
    def __add_distance(self, km):
        self.odometer += km
 
    def __subtract_fuel(self, fuel):
        self.fuel -= fuel
        
             