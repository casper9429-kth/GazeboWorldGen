# gazebo_world_gen/shapes.py

class Shape:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

class Polygon(Shape):
    def __init__(self, points, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.points = points  # List of tuples (x, y)
        self.type = "polygon"

    def get_gz_xml(self):
        points_str = " ".join(f"{p[0]} {p[1]}" for p in self.points)
        return f"""
<model name="polygon">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} 0 0 0</pose>
  <link name="link">
    <collision name="collision">
      <geometry>
        <polyline>
          <height>0.1</height>
          <point>{points_str}</point>
        </polyline>
      </geometry>
    </collision>
    <visual name="visual">
      <geometry>
        <polyline>
          <height>0.1</height>
          <point>{points_str}</point>
        </polyline>
      </geometry>
      <material>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""

class Circle(Shape):
    def __init__(self, radius, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.radius = radius
        self.type = "circle"

    def get_gz_xml(self):
        return f"""
<model name="circle">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} 0 0 0</pose>
  <link name="link">
    <collision name="collision">
      <geometry>
        <cylinder>
          <radius>{self.radius}</radius>
          <length>0.1</length>
        </cylinder>
      </geometry>
    </collision>
    <visual name="visual">
      <geometry>
        <cylinder>
          <radius>{self.radius}</radius>
          <length>0.1</length>
        </cylinder>
      </geometry>
      <material>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""

class Rectangle(Shape):
    def __init__(self, width, height, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.width = width
        self.height = height
        self.type = "rectangle"

    def get_gz_xml(self):
        return f"""
<model name="rectangle">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} 0 0 0</pose>
  <link name="link">
    <collision name="collision">
      <geometry>
        <box>
          <size>{self.width} {self.height} 0.1</size>
        </box>
      </geometry>
    </collision>
    <visual name="visual">
      <geometry>
        <box>
          <size>{self.width} {self.height} 0.1</size>
        </box>
      </geometry>
      <material>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""

class Block(Shape):
    def __init__(self, width, height, depth, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.width = width
        self.height = height
        self.depth = depth
        self.type = "block"

    def get_gz_xml(self):
        return f"""
<model name="block">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} 0 0 0</pose>
  <link name="link">
    <collision name="collision">
      <geometry>
        <box>
          <size>{self.width} {self.height} {self.depth}</size>
        </box>
      </geometry>
    </collision>
    <visual name="visual">
      <geometry>
        <box>
          <size>{self.width} {self.height} {self.depth}</size>
        </box>
      </geometry>
      <material>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""

class Sphere(Shape):
    def __init__(self, radius, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.radius = radius
        self.type = "sphere"

    def get_gz_xml(self):
        return f"""
<model name="sphere">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} 0 0 0</pose>
  <link name="link">
    <collision name="collision">
      <geometry>
        <sphere>
          <radius>{self.radius}</radius>
        </sphere>
      </geometry>
    </collision>
    <visual name="visual">
      <geometry>
        <sphere>
          <radius>{self.radius}</radius>
        </sphere>
      </geometry>
      <material>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""

class Ellipsoid(Shape):
    def __init__(self, radius_x, radius_y, radius_z, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.radius_z = radius_z
        self.type = "ellipsoid"

    def get_gz_xml(self):
        return f"""
<model name="ellipsoid">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} 0 0 0</pose>
  <link name="link">
    <collision name="collision">
      <geometry>
        <mesh>
          <uri>file://media/models/ellipsoid.dae</uri>
        </mesh>
      </geometry>
    </collision>
    <visual name="visual">
      <geometry>
        <mesh>
          <uri>file://media/models/ellipsoid.dae</uri>
        </mesh>
      </geometry>
      <material>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""

class Pyramid(Shape):
    def __init__(self, width, height, depth, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.width = width
        self.height = height
        self.depth = depth
        self.type = "pyramid"

    def get_gz_xml(self):
        return f"""
<model name="pyramid">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} 0 0 0</pose>
  <link name="link">
    <collision name="collision">
      <geometry>
        <mesh>
          <uri>file://media/models/pyramid.dae</uri>
        </mesh>
      </geometry>
    </collision>
    <visual name="visual">
      <geometry>
        <mesh>
          <uri>file://media/models/pyramid.dae</uri>
        </mesh>
      </geometry>
      <material>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""

class Cylinder(Shape):
    def __init__(self, radius, length, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.radius = radius
        self.length = length
        self.type = "cylinder"

    def get_gz_xml(self):
        return f"""
<model name="cylinder">
  <static>true</static>
  <pose>{self.x} {self.y} {self.z} 0 0 0</pose>
  <link name="link">
    <collision name="collision">
      <geometry>
        <cylinder>
          <radius>{self.radius}</radius>
          <length>{self.length}</length>
        </cylinder>
      </geometry>
    </collision>
    <visual name="visual">
      <geometry>
        <cylinder>
          <radius>{self.radius}</radius>
          <length>{self.length}</length>
        </cylinder>
      </geometry>
      <material>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""
