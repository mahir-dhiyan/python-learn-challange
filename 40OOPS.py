# 40. Object Oriented Programming[03:35:55]-------------------------------------------------
from car import Car
car_1=Car("Chevy","Corvett",2021,"Blue")
car_2=Car("Ford","Mustang",2022,"Black-Blue")
print(car_2.model)
print(car_2.year)
print(car_1.make)
print(car_1.year)
car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()