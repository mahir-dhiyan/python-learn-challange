# 49. Pass Objects as Arguments [04:19:20]---------------------------------------------------
class Car: 
    color=None

class Bike: 
    color=None
def change_color(vehicle,color):
    vehicle.color=color
car_1=Car()
car_2=Car()
car_3=Car()
bike_1=Bike()
change_color(car_1,"Red")
change_color(car_2,"Blue")
change_color(car_3,"Yello")
change_color(bike_1,"Pink")
print(car_1.color )
print(car_2.color)
print(car_3.color)
print(bike_1.color)