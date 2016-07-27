import math

class Shape:
    def __init__(self):
        self.area = 0
        # TODO: make the 'calculate area function run in the init?'


class Solid:
    def __init__(self):
        self.volume = 0
        # TODO: make the 'calculate area function run in the init?'


##########SHAPES##########

class Rectangle(Shape):
    def calculate_area(self, length, width):
        self.area = length * width


class Square(Rectangle):
    def calculate_area(self, side):
        super().calculate_area(side, side)


class Rhombus(Shape):
    def calculate_area(self, diagonal_one, diagonal_two):
        self.area = diagonal_one * diagonal_two


class Parallelogram(Shape):
    def calculate_area(self, base, height):
        self.area = base * height


class Triangle(Shape):
    def calculate_area(self, base, height):
        self.area = (base * height) / 2


class Circle(Shape):
    def calculate_area(self, radius):
        self.area = round(((radius * radius) * math.pi), 2)


#######SOLIDS#######

class Pyramid(Solid):
    def calculate_volume(self):
        self.volume = 4


class Cone(Solid):

    def calculate_volume(self):
        self.volume = 4


class Cylinder(Solid):

    def calculate_volume(self):
        self.volume = 4


class Sphere(Solid):
    def calculate_volume(self):
        self.volume = 4


class Block(Solid):
    def calculate_volume(self):
        self.volume = 4


class Cube(Block):
    def calculate_volume(self):
        self.volume = 4
