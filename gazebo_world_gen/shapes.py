import uuid

class Shape:
    def __init__(self, x=0, y=0, z=0,roll=0, pitch=0,yaw=0, color='0.5 0.5 0.5 1.0'):
        self.x = x
        self.y = y
        self.z = z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.color = color
        self.name = self.__class__.__name__.lower() + '_' + str(uuid.uuid4())

    def get_geometry_xml(self):
        """
        This method should be overridden by subclasses to provide the specific geometry XML.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_gz_xml(self):
        geometry_xml = self.get_geometry_xml()
        return f"""
<model name="{self.name}">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} {self.roll} {self.pitch} {self.yaw}</pose>
  <link name="link">
    <collision name="collision">
      {geometry_xml}
    </collision>
    <visual name="visual">
      {geometry_xml}
      <material>
        <ambient>{self.color}</ambient>
        <diffuse>{self.color}</diffuse>
      </material>
    </visual>
  </link>
</model>
"""


class Box(Shape):
    def __init__(self, width, height, depth, x=0, y=0, z=0, roll=0, pitch=0,yaw=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, roll, pitch, yaw, color)
        self.width = width
        self.height = height
        self.depth = depth
        self.type = "Box"

    def get_geometry_xml(self):
        return f"""
      <geometry>
        <box>
          <size>{self.width} {self.height} {self.depth}</size>
        </box>
      </geometry>
"""


class Sphere(Shape):
    def __init__(self, radius, x=0, y=0, z=0, roll=0, pitch=0,yaw=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, roll, pitch, yaw, color)
        self.radius = radius
        self.type = "Sphere"

    def get_geometry_xml(self):
        return f"""
      <geometry>
        <sphere>
          <radius>{self.radius}</radius>
        </sphere>
      </geometry>
"""


class Cylinder(Shape):
    def __init__(self, radius, length, x=0, y=0, z=0, roll=0, pitch=0,yaw=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, roll, pitch, yaw, color)
        self.radius = radius
        self.length = length
        self.type = "Cylinder"

    def get_geometry_xml(self):
        return f"""
      <geometry>
        <cylinder>
          <radius>{self.radius}</radius>
          <length>{self.length}</length>
        </cylinder>
      </geometry>
"""


class Ellipsoid(Shape):
    def __init__(self, radius_x, radius_y, radius_z, x=0, y=0, z=0, roll=0, pitch=0,yaw=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, roll, pitch, yaw, color)
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.radius_z = radius_z
        self.type = "Ellipsoid"

    def get_geometry_xml(self):
        return f"""
      <geometry>
        <mesh>
          <uri>model://ellipsoid/meshes/ellipsoid.dae</uri>
          <scale>1 1 1</scale>
        </mesh>
      </geometry>
"""


class Tetrahedron(Shape):
    def __init__(self, width, depth, height, x=0, y=0, z=0, roll=0, pitch=0,yaw=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, roll, pitch, yaw, color)
        self.width = width
        self.depth = depth
        self.height = height
        self.type = "Tetrahedron"

    def get_geometry_xml(self):
        return f"""
      <geometry>
        <mesh>
          <uri>model://tetrahedron/meshes/tetrahedron.dae</uri>
          <scale>1 1 1</scale>
        </mesh>
      </geometry>
"""


class SquarePyramid(Shape):
    def __init__(self, width, depth, height, x=0, y=0, z=0, roll=0, pitch=0,yaw=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, roll, pitch, yaw, color)
        self.width = width
        self.depth = depth
        self.height = height
        self.type = "SquarePyramid"

    def get_geometry_xml(self):
        return f"""
      <geometry>
        <mesh>
          <uri>model://square_pyramid/meshes/square_pyramid.dae</uri>
          <scale>1 1 1</scale>
        </mesh>
      </geometry>
"""


class Cone(Shape):
    def __init__(self, radius, height, x=0, y=0, z=0, roll=0, pitch=0,yaw=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, roll, pitch, yaw, color)
        self.radius = radius
        self.height = height
        self.type = "Cone"

    def get_geometry_xml(self):
        return f"""
      <geometry>
        <mesh>
          <uri>model://cone/meshes/cone.dae</uri>
          <scale>1 1 1</scale>
        </mesh>
      </geometry>
"""
