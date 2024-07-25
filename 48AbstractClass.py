# 48. Abstract Class[04:12:15]-------------------------------------------------------------------
from abc import ABC , abstractmethod
class Vehicle(ABC): 

    @abstractmethod
    def go(self):
        print("Vehicle is running")
        @abstractmethod
        def stop(self):
            pass
class Car(Vehicle):
    def go(self):
        print("The Car is going")
    def stop(self):
        print("Stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You Ride the Motorcycle")

    def stop(self):
        print("Stop the Motorcycle")

# vehicle=Vehicle()
car=Car()
motorcycle=Motorcycle()
# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()