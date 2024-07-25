# 42. Heritance [03:49:03]---------------------------------------------
class Animal:

    alive = True

    def eat(self): 
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This Rabbit is running")
class Fish(Animal):
    def swim(self):
        print("this fish is swiming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")
rabbit = Rabbit()
fish=Fish()
hawk=Hawk()
print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()