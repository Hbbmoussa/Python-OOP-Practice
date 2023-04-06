class Vehicle():
    color = 'white'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

#modelX = Vehicle("Tesla",234, 10)
#print(modelX.max_speed,modelX.mileage)

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

car = Car('School bus',300,20 )
print('Bus name:',car.name,',Speed:',car.max_speed,',mileage:',car.mileage, ',color:',car.color)
    
