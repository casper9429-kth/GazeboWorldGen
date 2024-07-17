# tests/test_shapes.py

import unittest
from gazebo_world_gen.shapes import Polygon, Circle, Rectangle

class TestShapes(unittest.TestCase):
    def test_polygon(self):
        polygon = Polygon(points=[(0,0), (1,0), (1,1), (0,1)])
        self.assertEqual(len(polygon.points), 4)

    def test_circle(self):
        circle = Circle(radius=5)
        self.assertEqual(circle.radius, 5)

    def test_rectangle(self):
        rectangle = Rectangle(width=4, height=2)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 2)

if __name__ == '__main__':
    unittest.main()
