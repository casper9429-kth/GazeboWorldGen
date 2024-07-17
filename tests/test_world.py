# tests/test_world.py

import unittest
from gazebo_world_gen.world import World
from gazebo_world_gen.shapes import Circle

class TestWorld(unittest.TestCase):
    def test_add_object(self):
        world = World()
        circle = Circle(radius=5)
        world.add_object(circle)
        self.assertIn(circle, world.get_objects())

    def test_remove_object(self):
        world = World()
        circle = Circle(radius=5)
        world.add_object(circle)
        world.remove_object(circle)
        self.assertNotIn(circle, world.get_objects())

if __name__ == '__main__':
    unittest.main()
