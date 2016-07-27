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
        self.area = round((diagonal_one * diagonal_two), 2)


class Parallelogram(Shape):
    def calculate_area(self, base, height):
        self.area = round((base * height), 2)


class Triangle(Shape):
    def calculate_area(self, base, height):
        self.area = round(((base * height) / 2), 2)


class Circle(Shape):
    def calculate_area(self, radius):
        self.area = round(((radius * radius) * math.pi), 2)


#######SOLIDS#######

class Pyramid(Solid):
    # NOTE: this calculation works for a rectangular pyramid only
    def calculate_volume(self, base_length, base_width, height):
        self.volume = round(((base_length * base_width * height) / 3), 2)


class Cone(Solid):

    def calculate_volume(self, radius, height):
        self.volume = round(((radius * radius * height * math.pi)/3), 2)


class Cylinder(Solid):

    def calculate_volume(self, radius, height):
        self.volume = round((radius*radius*height * math.pi), 2)


class Sphere(Solid):
    def calculate_volume(self, radius):
        self.volume = round(((radius*radius*radius*math.pi*4)/3), 2)


class Block(Solid):
    def calculate_volume(self, length, width, height):
        self.volume = round((length * width * height), 2)


class Cube(Block):
    def calculate_volume(self, side):
        super().calculate_volume(side, side, side)
