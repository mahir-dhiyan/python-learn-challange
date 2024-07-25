# 45. Method Over Writing [ 04:01:55]-------------------------------------------------------------------
class Animal: 
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("The Rabbit is eating a carrot")
rabbit=Rabbit()
rabbit.eat()