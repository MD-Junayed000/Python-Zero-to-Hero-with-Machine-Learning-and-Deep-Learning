## Polymorphism== to have manny faces
##                poly == many
##               Morphe== form
## 2 types : 1. Inheritance
 #            2.Duck typing


print('######## Inheritance ##################')


class Shape:

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,base,height):
        self.height=height
        self.base=base

    def area(self):
        return 0.5* self.height*self.base



class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)##################
        self.topping=topping


shapes=[Circle(4),Square(5),Triangle(6,7),Pizza('Peperonni',15)]

for shape in shapes:
    print(shape.area())


##################################################
# Duck typing== Another way to achieve polymorphism besides inhertance
#               object must have the minimum necessary attributes / methods

#              'If it looks like a duck and quacks like a duck,it is a duck

class Animal:
    alive= True

class Dog(Animal):
    def speak(self):
        print('Woof!')

class Cat(Animal):
        def speak(self):
            print('Meow!')
class Car:
    def horn(self):
        print('HONK!')


animals =[Dog(),Cat(),Car()] ## CAr really doesnot belong here

for animal in animals:
    animal.speak()



























