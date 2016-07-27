import math
from menu import *

class Shape():
    def __init__(self):
        # self.name = "shape"
        self.area = 0

    def __str__(self):
        return("the area of your " + self.name + " is " + str(self.area) + ".")



class Solid():
    def __init__(self):
        # self.name = "solid"
        self.volume = 0

    def __str__(self):
        return("the volume of your " + self.name + " is " + str(self.volume) + ".")

    
##########SHAPES##########

class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.name = "rectangle"

    def calculate_area(self):
        self.area = round((self.length * self.width), 2)
        print(self.__str__())

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "square"


class Rhombus(Shape):
    def __init__(self, diagonal_one, diagonal_two):
        super().__init__()
        self.diagonal_one = diagonal_one
        self.diagonal_two = diagonal_two
        self.name = "rhombus"

    def calculate_area(self):
        self.area = round((self.diagonal_one * self.diagonal_two), 2)
        print(self.__str__())


class Parallelogram(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        self.name = "parallelogram"

    def calculate_area(self):
        self.area = round((self.base * self.height), 2)
        print(self.__str__())


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        self.name = "triangle"

    def calculate_area(self):
        self.area = round(((self.base * self.height) / 2), 2)
        print(self.__str__())


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.name = "circle"

    def calculate_area(self):
        self.area = round(((self.radius **2) * math.pi), 2)
        print(self.__str__())


#######SOLIDS#######

class Pyramid(Solid):
    def __init__(self, base_length, base_width, height):
        super().__init__()
        self.base_length = base_length
        self.base_width = base_width
        self.height = height
        self.name = "pyramid"

    # NOTE: this calculation works for a rectangular pyramid only
    def calculate_volume(self):
        self.volume = round(((self.base_length * self.base_width * self.height) / 3), 2)
        print(self.__str__())


class Cone(Solid):
    def __init__(self, base_radius, height):
        super().__init__()
        self.name = "cone"
        self.base_radius = base_radius
        self.height = height

    def calculate_volume(self):
        self.volume = round((((self.base_radius **2) * self.height * math.pi)/3), 2)
        print(self.__str__())


class Cylinder(Solid):
    def __init__(self, radius, height):
        super().__init__()
        self.name = "cylinder"
        self.radius = radius
        self.height = height

    def calculate_volume(self):
        self.volume = round(((self.radius **2)*self.height * math.pi), 2)
        print(self.__str__())


class Sphere(Solid):
    def __init__(self, radius):
        super().__init__()
        self.name = "sphere"
        self.radius = radius

    def calculate_volume(self):
        self.volume = round((((self.radius **3)*math.pi*4)/3), 2)
        print(self.__str__())


class Block(Solid):
    def __init__(self, base_length, base_width, height):
        super().__init__()
        self.length = base_length
        self.width = base_width
        self.height = height
        self.name = "block"

    def calculate_volume(self):
        self.volume = round((self.length * self.width * self.height), 2)
        print(self.__str__())


class Cube(Block):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.name = "cube"

if __name__ == '__main__':
    app = Sharp_Shapes()
