# 41 Basics of class variables [03:45:15]--------------------------------------
from car import Car
car_1=Car("Chevy","Corvett",2021,"Blue")
car_2=Car("Ford","Mustang",2022,"Black-Blue")
car_1.wheels=2
# Car.wheels=2
print("Both car_1 and car_2 has "+str(car_1.wheels)+" Wheels and "+str(car_2.wheels)+" wheels")
print(car_2.model)
print(car_2.year)
print(car_1.make)
print(car_1.year)
car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()