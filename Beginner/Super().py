# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods
#           Function used to give access to the methods of a parent class.



import math


class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled ##### these are the common

    def describe(self):
        print(f"It is {self.color} and { 'filled' if self.is_filled else 'not filled'}")



class Circle(Shape):
    def __init__(self, color, is_filled,radius):
         super().__init__(color,is_filled) ########
         self.radius=radius

    def describe(self):
        print(f"The Area of the circle is {3.14*pow(self.radius,2)}")
        super().describe() ######################################################



class Square(Shape):
    pass

class Triangle(Shape):
    pass

circle=Circle('red',True,5)

print(circle.color)

circle.describe()















