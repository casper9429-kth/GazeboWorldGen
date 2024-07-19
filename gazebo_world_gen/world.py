# gazebo_world_gen/world.py

class World:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def get_objects(self):
        return self.objects
    
    def get_gz_xml(self):
        """
        Exports the world to Gazebo XML format including all objects.
        """
        xml_objects = "\n".join([obj.get_gz_xml() for obj in self.objects])
        return f"""<?xml version="1.0" ?>
<sdf version="1.6">
  <world name="default">
    {xml_objects}
  </world>
</sdf>
"""
    
    def save_gz_world(self, filename):
        """
        Saves the world to a Gazebo world file.
        """
        filename = filename + ".sdf" if not filename.endswith(".sdf") else filename
        gz_xml_str = self.get_gz_xml()
        with open(filename, "w") as f:
            f.write(gz_xml_str)

# Example usage
if __name__ == "__main__":
    from shapes import Sphere, Box, Cylinder

    world = World()
    # world.add_object(Box(1, 1, 1, 1, 1, 1, color='1 0 0 1'))  # Red block
    world.add_object(Sphere(0.5, 2, 2, 0.5, color='0 1 0 1'))   # Green sphere
    world.add_object(Cylinder(0.3, 1.0, 3, 3, 0.5, color='0 0 1 1'))  # Blue cylinder
    world.add_object(Box(2.0, 1.0, 4, 4, 0.1, color='1 1 0 1')) # Yellow Box
    world.add_object(Box(2.0, 1.0, 4, 7, 0.1, color='1 1 0 1')) # Yellow Box
    world.add_object(Box(2.0, 1.0, 4, 10, 0.1, color='1 1 0 1')) # Yellow Box
    world.add_object(Box(2.0, 1.0, 4, 20, 0.1, color='1 1 0 1')) # Yellow Box
    
    world.save_gz_world("example_world")
    print("example_world.sdf has been generated.")
