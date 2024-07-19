# world.py
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
<sdf version="1.7">
  <world name="default">
    <light name='sun' type='directional'>
      <cast_shadows>1</cast_shadows>
      <pose>0 0 10 0 -0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.1 -0.9</direction>
      <spot>
        <inner_angle>0</inner_angle>
        <outer_angle>0</outer_angle>
        <falloff>0</falloff>
      </spot>
    </light>
    {xml_objects}
    <gravity>0 0 -9.8</gravity>
    <magnetic_field>6e-06 2.3e-05 -4.2e-05</magnetic_field>
    <atmosphere type='adiabatic'/>
    <physics type='ode'>
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>1000</real_time_update_rate>
    </physics>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
    </scene>
    <audio>
      <device>default</device>
    </audio>
    <wind/>
    <spherical_coordinates>
      <surface_model>EARTH_WGS84</surface_model>
      <latitude_deg>0</latitude_deg>
      <longitude_deg>0</longitude_deg>
      <elevation>0</elevation>
      <heading_deg>0</heading_deg>
    </spherical_coordinates>
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
    from shapes import *

    world = World()

    # Create instances of each shape
    box = Box(width=2, height=1, depth=4, x=1, y=2, z=0, color='1 1 0 1')
    sphere = Sphere(radius=1, x=3, y=4, z=0, color='0 1 1 1')
    cylinder = Cylinder(radius=1, length=2, x=5, y=6, z=0, color='1 0 1 1')
    ellipsoid = Ellipsoid(radius_x=1, radius_y=0.5, radius_z=0.5, x=7, y=8, z=0, color='0 1 0 1')
    tetrahedron = Tetrahedron(width=1, depth=1, height=1.5, x=9, y=10, z=0, color='1 0 0 1')
    square_pyramid = SquarePyramid(width=2, depth=2, height=3, x=11, y=12, z=0, color='0 0 1 1')
    cone = Cone(radius=1, height=3, x=13, y=14, z=0, color='1 1 0 1')
    box2 = Box(width=2, height=1, depth=4, x=1, y=2, z=0, color='1 1 0 1')
    sphere2 = Sphere(radius=1, x=3, y=4, z=0, color='0 1 1 1')
    cylinder2 = Cylinder(radius=1, length=2, x=5, y=6, z=0, color='1 0 1 1')
    ellipsoid2 = Ellipsoid(radius_x=1, radius_y=0.5, radius_z=0.5, x=7, y=8, z=0, color='0 1 0 1')
    tetrahedron2 = Tetrahedron(width=1, depth=1, height=1.5, x=9, y=10, z=0, color='1 0 0 1')
    square_pyramid2 = SquarePyramid(width=2, depth=2, height=3, x=11, y=12, z=0, color='0 0 1 1')
    cone2 = Cone(radius=1, height=3, x=18, y=14, z=0, color='0 1 0 1')
                 

    # Add shapes to the world
    world.add_object(box)
    world.add_object(sphere)
    world.add_object(cylinder)
    world.add_object(ellipsoid)
    world.add_object(tetrahedron)
    world.add_object(square_pyramid)
    world.add_object(cone)
    world.add_object(box2)
    world.add_object(sphere2)
    world.add_object(cylinder2)
    world.add_object(ellipsoid2)
    world.add_object(tetrahedron2)
    world.add_object(square_pyramid2)
    world.add_object(cone2)

    # Save world to file
    world.save_gz_world("example_world")
    print("example_world.sdf saved successfully.")
