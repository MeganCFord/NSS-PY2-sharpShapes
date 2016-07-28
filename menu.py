from sharpshapes import *

class Sharp_Shapes:
    def __init__(self):
        self.current_shape = None

    # Initial Start Menu with two options. TODO: error handle inputs.
    def start_menu(self):
        intro = "==========SHARP SHAPES==========\ncalculate the area of a shape or volume of a solid!"
        print(intro)
        intro_input = input("would you like to calculate for 1. a 2D shape, or 2. a 3D solid? ")
        if intro_input not in ("1", "2"):
            print("please press 1 for a 2d shape or 2 for a 3d solid.")
        elif intro_input == "1":
            self.shape_menu()
        elif intro_input == "2":
            self.solid_menu()

    # secondary menu for (2D) shapes. TODO: Error handle inputs.
    def shape_menu(self):
        shape_string = "1. Rectangle\n2. Square\n3. Rhombus\n4. Parallelogram\n5. Triangle\n6. Circle\n7. Go Back"
        print(shape_string)
        instantiation_input = input()
        if instantiation_input not in ("1", "2", "3", "4", "5", "6", "7"):
            print("please type the number of the shape you'd like to calculate.")
        elif instantiation_input == "1":
            # for each of these options, first input for the required size-finding measurements is requested.
            # Then the shape class is instantiated with the measurements passed in.
            # Then the area is calculated, which is then printed-
            # then the start menu is re-displayed to start again.
            length = int(input("enter the length of your rectangle. "))
            width = int(input("enter the width of your rectangle. "))
            self.current_shape = Rectangle(length, width)

        elif instantiation_input == "2":
            side = int(input("enter the length of the sides of your square. "))
            self.current_shape = Square(side)

        elif instantiation_input == "3":
            diagonal_one = int(input("enter the first diagonal of your rhombus. "))
            diagonal_two = int(input("enter the second diagonal of your rhombus. "))
            self.current_shape = Rhombus(diagonal_one, diagonal_two)

        elif instantiation_input == "4":
            base = int(input("enter the base of your parallelogram. "))
            height = int(input("enter the height of your parallelogram. "))
            self.current_shape = Parallelogram(base, height)

        elif instantiation_input == "5":
            base = int(input("enter the base of your triangle. "))
            height = int(input("enter the height of your triangle. "))
            self.current_shape = Triangle(base, height)

        elif instantiation_input == "6":
            radius = int(input("enter the radius of your circle. "))
            self.current_shape = Circle(radius)

        elif instantiation_input == "7":
                self.start_menu()

        self.current_shape.calculate_area()
        print(self.current_shape.__str__())
        self.start_menu()

    # secondary menu for (2D) shapes. TODO: Error handle inputs
    def solid_menu(self):
        solid_string = "1. Pyramid\n2. Cone\n3. Cylinder\n4. Sphere\n5. Block\n6. Cube\n7. Go Back"
        print(solid_string)
        instantiation_input = input()
        if instantiation_input not in ("1", "2", "3", "4", "5", "6", "7"):
            print("please type the number of the solid you'd like to calculate.")
            # This exits the program which I don't want.
        elif instantiation_input == "1":
            # for each of these options, first: input for the required size-finding measurements is requested.
            # Then the shape class is instantiated with the measurements passed in.
            # Then the area is calculated, which is then printed-
            # then the start menu is re-displayed to start again.
            base_length = int(input("enter the base length of your pyramid. "))
            base_width = int(input("enter the base width of your pyramid. "))
            height = int(input("enter the height of your pyramid. "))
            self.current_shape = Pyramid(base_length, base_width, height)

        elif instantiation_input == "2":
            base_radius = int(input("enter the base radius of your cone. "))
            height = int(input("enter the height of your cone. "))
            self.current_shape = Cone(base_radius, height)

        elif instantiation_input == "3":
            base_radius = int(input("enter the base radius of your cylinder. "))
            height = int(input("enter the height of your cylinder. "))
            self.current_shape = Cylinder(base_radius, height)

        elif instantiation_input == "4":
            radius = int(input("enter the radius of your sphere. "))
            self.current_shape = Sphere(radius)

        elif instantiation_input == "5":
            base_length = int(input("enter the base length of your block. "))
            base_width = int(input("enter the base width of your block. "))
            height = int(input("enter the height of your block. "))
            self.current_shape = Block(base_length, base_width, height)

        elif instantiation_input == "6":
            side = int(input("enter the length of the sides of your cube. "))
            self.current_shape = Cube(side)

        elif instantiation_input == "7":
                self.start_menu()

        self.current_shape.calculate_volume()
        print(self.current_shape.__str__())
        self.start_menu()
