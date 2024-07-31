class Vehicle:
    def park(self,name):
        print(name,"is parked at vehicle parking")
class Bike(Vehicle):
    def park(self, name):
        print(name,"is parked at two wheeler parking")
class Car(Vehicle):
    def park(self, name):
        print(name,"is parked at four wheeler parking")
class Lorry(Vehicle):
    def park(self, name):
        print(name,"is parked at six wheeler parking")
v = Vehicle()
v.park("Vehicle")
c = Car()
c.park("Car")
b=Bike()
b.park("Bike")
l = Lorry()
l.park("Lorry")