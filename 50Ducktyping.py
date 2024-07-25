# 50. Duck Typing [04:23:25]----------------------------------------------------------------------
class Duck: 
    def walk(self):
        print("The Duck is walking")

    def talk(self):
        print("The Duck is Quacking")
class Chicken: 
    def walk(self):
        print("The Chicken is walking")

    def talk(self):
        print("The Chicken is Quacking")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caugth the critter!")
chicken=Chicken()
duck=Duck()
person=Person()
person.catch(chicken)
