# 43 Multi level inheritance [03:55:40]--------------------------------------------------
class Organism: 
    alive=True
class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")
dog=Dog()
print(dog.alive)
dog.bark()
dog.eat()