import math

class Shape:
    def __init__(self):
        self.area = 0


class Solid:
    def __init__(self):
        self.volume = 0


class Rectangle(Shape):
    def calculate_rectangle_area(self, length, height):
        self.area = length * height


class Square(Rectangle):
    def calculate_square_area(self, side):
        self.calculate_rectangle_area(side, side)


class Rhombus(Shape):
    def calculate_rhombus_area(self, diagonal_one, diagonal_two):
        self.area = (diagonal_one * diagonal_two) / 2


class Parallelogram(Shape):
    def calculate_parallelogram_area(self, base, height):
        self.area = base * height


class Triangle(Shape):
    def calculate_triangle_area(self, base, height):
        self.area = (base * height) / 2


class Circle(Shape):
    def calculate_circle_area(self, radius):
        self.area = math.pi * (radius * radius)


class Pyramid(Solid):
    def calculate_pyramid_volume(self):
        pass


class Cone(Solid):

    def calculate_cone_volume(self):
        pass


class Cylinder(Solid):

    def calculate_cylinder_volume(self):
        pass


class Sphere(Solid):
    def calculate_sphere_volume(self):
        pass


class Block(Solid):
    def calculate_block_volume(self):
        pass


class Cube(Block):
    def calculate_cube_volume(self):
        pass
