# gazebo_world_gen/shapes.py

class Shape:
    _id_counter = 0  # Class-level counter to track shape instances

    def __init__(self, x, y, z=0, color='0.5 0.5 0.5 1.0'):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.id = Shape._id_counter  # Assign unique ID to the shape
        Shape._id_counter += 1  # Increment the counter for the next shape
        self.name = f"{self.__class__.__name__}_{self.id}"  # Generate unique name

class Box(Shape):
    def __init__(self, width, height, depth, x=0, y=0, z=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, color)
        self.width = width
        self.height = height
        self.depth = depth
        self.type = "Box"

    def get_gz_xml(self):
        return f"""
<model name="{self.name}">
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
        <ambient>{self.color}</ambient>
        <diffuse>{self.color}</diffuse>
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
    def __init__(self, radius, x=0, y=0, z=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, color)
        self.radius = radius
        self.type = "Sphere"

    def get_gz_xml(self):
        return f"""
<model name="{self.name}">
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
        <ambient>{self.color}</ambient>
        <diffuse>{self.color}</diffuse>
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
    def __init__(self, radius, length, x=0, y=0, z=0, color='0.5 0.5 0.5 1.0'):
        super().__init__(x, y, z, color)
        self.radius = radius
        self.length = length
        self.type = "Cylinder"

    def get_gz_xml(self):
        return f"""
<model name="{self.name}">
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
        <ambient>{self.color}</ambient>
        <diffuse>{self.color}</diffuse>
        <script>
          <uri>file://media/materials/scripts/gazebo.material</uri>
          <name>Gazebo/Grey</name>
        </script>
      </material>
    </visual>
  </link>
</model>
"""
