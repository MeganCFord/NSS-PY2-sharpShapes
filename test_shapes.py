from sharpshapes import *
import unittest


class Test_shapes(unittest.TestCase):

    def test_rectangle_structure(self):
        test_rectangle = Rectangle()
        self.assertIsInstance(test_rectangle, Rectangle)
        self.assertIsInstance(test_rectangle, Shape)

    def test_square_structure(self):
        test_square = Square()
        self.assertIsInstance(test_square, Square)
        self.assertIsInstance(test_square, Rectangle)
        self.assertIsInstance(test_square, Shape)

    def test_rhombus_structure(self):
        test_rhombus = Rhombus()
        self.assertIsInstance(test_rhombus, Rhombus)
        self.assertIsInstance(test_rhombus, Shape)

    def test_parallelogram_structure(self):
        test_parallelogram = Parallelogram()
        self.assertIsInstance(test_parallelogram, Parallelogram)
        self.assertIsInstance(test_parallelogram, Shape)

    def test_triangle_structure(self):
        test_triangle = Triangle()
        self.assertIsInstance(test_triangle, Triangle)
        self.assertIsInstance(test_triangle, Shape)

    def test_circle_structure(self):
        test_circle = Circle()
        self.assertIsInstance(test_circle, Circle)
        self.assertIsInstance(test_circle, Shape)

    # ============solids=============
    def test_pyramid_structure(self):
        test_pyramid = Pyramid()
        self.assertIsInstance(test_pyramid, Pyramid)
        self.assertIsInstance(test_pyramid, Solid)

    def test_cone_structure(self):
        test_cone = Cone()
        self.assertIsInstance(test_cone, Cone)
        self.assertIsInstance(test_cone, Solid)

    def test_cylinder_structure(self):
        test_cylinder = Cylinder()
        self.assertIsInstance(test_cylinder, Cylinder)
        self.assertIsInstance(test_cylinder, Solid)

    def test_sphere_structure(self):
        test_sphere = Sphere()
        self.assertIsInstance(test_sphere, Sphere)
        self.assertIsInstance(test_sphere, Solid)

    def test_block_structure(self):
        test_block = Block()
        self.assertIsInstance(test_block, Block)
        self.assertIsInstance(test_block, Solid)
        self.assertIsInstance(test_block, ThreeD)

    def test_cube_structure(self):
        test_cube = Cube()
        self.assertIsInstance(test_cube, Block)
        self.assertIsInstance(test_cube, Cube)
        self.assertIsInstance(test_cube, Solid)

if __name__ == '__main__':
    unittest.main()
