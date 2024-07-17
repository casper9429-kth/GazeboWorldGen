from gazebo_world_gen.world import World
from gazebo_world_gen.shapes import Circle, Rectangle
from gazebo_world_gen.export import Exporter

# Create a new world
world = World()

# Add objects to the world
circle = Circle(radius=5, x=10, y=10)
rectangle = Rectangle(width=4, height=2, x=20, y=20)
world.add_object(circle)
world.add_object(rectangle)

# Export the world to Gazebo format
exporter = Exporter(world)
exporter.to_gazebo_format('world.sdf')