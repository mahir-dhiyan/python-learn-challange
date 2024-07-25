# 47 Super Function [04:08:15]------------------------------------------------------------
class Rectangle: 
    def __init__(self,length,width):
        self.length=length
        self.width=width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height=height
    def volume(self):
        return self.length*self.width*self.height
    
cube=Cube(3,4,5)
square=Square(6,9)
print(cube.volume())
print(square.area())