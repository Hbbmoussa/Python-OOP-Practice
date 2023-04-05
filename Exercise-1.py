class Vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle("Tesla",234, 10)
#print(modelX.max_speed,modelX.mileage)

class Bus(Vehicle):
    pass

schoolBus = Bus('School bus',300,20 )
print('Bus name:',schoolBus.name,',Speed:',schoolBus.max_speed,',mileage:',schoolBus.mileage)
    