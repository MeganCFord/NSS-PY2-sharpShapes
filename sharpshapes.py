import math
from menu import *


# master class.
class Shape():
    def __init__(self):
        self.area = 0

    def __str__(self):
        return("the area of your " + self.name + " is " + str(self.area) + ".")


# master class.
class Solid():
    def __init__(self):
        self.volume = 0

    def __str__(self):
        return("the volume of your " + self.name + " is " + str(self.volume) + ".")


# #########SHAPES##########
class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.name = "rectangle"

    def calculate_area(self):
        '''
        Calculates the area of a rectangle based on the length and width specified at the time of rectangle class instantiation.

        Arguments: none
        '''
        self.area = round((self.length * self.width), 2)


class Square(Rectangle):
    # note that since square inherits from rectangle, it does not have its own calculate_area method.
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
        '''
        Calculates the area of a Rhombus based on the two diagonal measurements specified at the time of Rhombus class instantiation.

        Arguments: none
        '''
        self.area = round((self.diagonal_one * self.diagonal_two), 2)


class Parallelogram(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        self.name = "parallelogram"

    def calculate_area(self):
        '''
        Calculates the area of a parallelogram based on the base and height specified at the time of parallelogram class instantiation.

        Arguments: none
        '''
        self.area = round((self.base * self.height), 2)


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        self.name = "triangle"

    def calculate_area(self):
        '''
        Calculates the area of a triangle based on the base and height specified at the time of triangle class instantiation.

        Arguments: none
        '''
        self.area = round(((self.base * self.height) / 2), 2)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.name = "circle"

    def calculate_area(self):
        '''
        Calculates the area of a circle based on the radius specified at the time of circle class instantiation.

        Arguments: none
        '''
        self.area = round(((self.radius ** 2) * math.pi), 2)


# ######SOLIDS#######

class Pyramid(Solid):
    def __init__(self, base_length, base_width, height):
        super().__init__()
        self.base_length = base_length
        self.base_width = base_width
        self.height = height
        self.name = "pyramid"

    # NOTE: this calculation works for a rectangular pyramid only
    def calculate_volume(self):
        '''
        Calculates the volume of a pyramid based on the base length, base width, and height specified at the time of pyramid class instantiation.

        Arguments: none
        '''
        self.volume = round(((self.base_length * self.base_width * self.height) / 3), 2)


class Cone(Solid):
    def __init__(self, base_radius, height):
        super().__init__()
        self.name = "cone"
        self.base_radius = base_radius
        self.height = height

    def calculate_volume(self):
        '''
        Calculates the volume of a cone based on the base radius and height specified at the time of cone class instantiation.

        Arguments: none
        '''
        self.volume = round((((self.base_radius ** 2) * self.height * math.pi)/3), 2)


class Cylinder(Solid):
    def __init__(self, radius, height):
        super().__init__()
        self.name = "cylinder"
        self.radius = radius
        self.height = height

    def calculate_volume(self):
        '''
        Calculates the volume of a cylinder based on the base radius and height specified at the time of cylinder class instantiation.

        Arguments: none
        '''
        self.volume = round(((self.radius ** 2)*self.height * math.pi), 2)


class Sphere(Solid):
    def __init__(self, radius):
        super().__init__()
        self.name = "sphere"
        self.radius = radius

    def calculate_volume(self):
        '''
        Calculates the volume of a sphere based on the base radius specified at the time of sphere class instantiation.

        Arguments: none
        '''
        self.volume = round((((self.radius ** 3)*math.pi*4)/3), 2)


class Block(Solid):
    def __init__(self, base_length, base_width, height):
        super().__init__()
        self.length = base_length
        self.width = base_width
        self.height = height
        self.name = "block"

    # NOTE: this shape works for blocks with all right angles only.
    def calculate_volume(self):
        '''
        Calculates the volume of a rectangular based on the base length, base width, and height specified at the time of rectangular class instantiation.

        Arguments: none
        '''
        self.volume = round((self.length * self.width * self.height), 2)


class Cube(Block):
    # note that since cube inherits from block, it does not have its own calculate_area method.
    def __init__(self, side):
        super().__init__(side, side, side)
        self.name = "cube"


if __name__ == '__main__':
    app = Sharp_Shapes()
    app.start_menu()
