from sharpshapes import *
import unittest


class Test_shapes(unittest.TestCase):

    def test_shape_structure(self):
        test_shape = Shape()
        self.assertEqual(test_shape.area, 0)

    def test_solid_structure(self):
        test_solid = Solid()
        self.assertEqual(test_solid.volume, 0)

    def test_rectangle_structure(self):
        test_rectangle = Rectangle()
        self.assertIsInstance(test_rectangle, Rectangle)
        self.assertIsInstance(test_rectangle, Shape)
        self.assertEqual(test_rectangle.area, 0)
        test_rectangle.calculate_area(2, 2)
        self.assertEqual(test_rectangle.area, 4)

    def test_square_structure(self):
        test_square = Square()
        self.assertIsInstance(test_square, Square)
        self.assertIsInstance(test_square, Rectangle)
        self.assertIsInstance(test_square, Shape)
        self.assertEqual(test_square.area, 0)
        test_square.calculate_area(4)
        self.assertEqual(test_square.area, 16)

    def test_rhombus_structure(self):
        test_rhombus = Rhombus()
        self.assertIsInstance(test_rhombus, Rhombus)
        self.assertIsInstance(test_rhombus, Shape)
        self.assertEqual(test_rhombus.area, 0)
        test_rhombus.calculate_area(2, 2)
        self.assertEqual(test_rhombus.area, 4)

    def test_parallelogram_structure(self):
        test_parallelogram = Parallelogram()
        self.assertIsInstance(test_parallelogram, Parallelogram)
        self.assertIsInstance(test_parallelogram, Shape)
        self.assertEqual(test_parallelogram.area, 0)
        test_parallelogram.calculate_area(2, 2)
        self.assertEqual(test_parallelogram.area, 4)

    def test_triangle_structure(self):
        test_triangle = Triangle()
        self.assertIsInstance(test_triangle, Triangle)
        self.assertIsInstance(test_triangle, Shape)
        self.assertEqual(test_triangle.area, 0)
        test_triangle.calculate_area(4, 2)
        self.assertEqual(test_triangle.area, 4)

    def test_circle_structure(self):
        test_circle = Circle()
        self.assertIsInstance(test_circle, Circle)
        self.assertIsInstance(test_circle, Shape)
        self.assertEqual(test_circle.area, 0)
        test_circle.calculate_area(4)
        self.assertEqual(test_circle.area, 50.27)

    # ============solids=============
    def test_pyramid_structure(self):
        test_pyramid = Pyramid()
        self.assertIsInstance(test_pyramid, Pyramid)
        self.assertIsInstance(test_pyramid, Solid)
        self.assertEqual(test_pyramid.volume, 0)
        test_pyramid.calculate_volume(2, 2, 2)
        self.assertEqual(test_pyramid.volume, 2.67)

    def test_cone_structure(self):
        test_cone = Cone()
        self.assertIsInstance(test_cone, Cone)
        self.assertIsInstance(test_cone, Solid)
        self.assertEqual(test_cone.volume, 0)
        test_cone.calculate_volume(2, 2)
        self.assertEqual(test_cone.volume, 8.38)

    def test_cylinder_structure(self):
        test_cylinder = Cylinder()
        self.assertIsInstance(test_cylinder, Cylinder)
        self.assertIsInstance(test_cylinder, Solid)
        self.assertEqual(test_cylinder.volume, 0)
        test_cylinder.calculate_volume(2, 4)
        self.assertEqual(test_cylinder.volume, 50.27)

    def test_sphere_structure(self):
        test_sphere = Sphere()
        self.assertIsInstance(test_sphere, Sphere)
        self.assertIsInstance(test_sphere, Solid)
        self.assertEqual(test_sphere.volume, 0)
        test_sphere.calculate_volume(4)
        self.assertEqual(test_sphere.volume, 268.08)

    def test_block_structure(self):
        test_block = Block()
        self.assertIsInstance(test_block, Block)
        self.assertIsInstance(test_block, Solid)
        self.assertEqual(test_block.volume, 0)
        test_block.calculate_volume(3, 3, 3)
        self.assertEqual(test_block.volume, 27)

    def test_cube_structure(self):
        test_cube = Cube()
        self.assertIsInstance(test_cube, Block)
        self.assertIsInstance(test_cube, Cube)
        self.assertIsInstance(test_cube, Solid)
        self.assertEqual(test_cube.volume, 0)
        test_cube.calculate_volume(3)
        self.assertEqual(test_cube.volume, 27)

if __name__ == '__main__':
    unittest.main()
