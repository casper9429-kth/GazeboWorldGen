from enum import Enum
from typing import Tuple, Dict, Any

class PhysicsEngine(Enum):
    ODE = "ode"
    BULLET = "bullet"
    SIMBODY = "simbody"
    DART = "dart"

class AtmosphereType(Enum):
    ADIABATIC = "adiabatic"

class SurfaceModel(Enum):
    EARTH_WGS84 = "EARTH_WGS84"
    MARS = "MARS"
    MOON = "MOON"
    CUSTOM = "CUSTOM"  # Use CUSTOM for flat earth

class AudioDevice(Enum):
    DEFAULT = "default"
    CUSTOM = "custom"

class World:
    def __init__(self, name: str = "default"):
        self.name = name
        self.objects = []
        self.settings: Dict[str, Any] = {
            "gravity": (0, 0, -9.8),
            "ambient_light": (0.4, 0.4, 0.4, 1),
            "background_color": (0.7, 0.7, 0.7, 1),
            "physics": self.default_physics(),
            "light": self.default_light(),
            "magnetic_field": (6e-06, 2.3e-05, -4.2e-05),
            "atmosphere": AtmosphereType.ADIABATIC.value,
            "audio_device": AudioDevice.DEFAULT.value,
            "spherical_coordinates": self.default_spherical_coordinates()
        }

    def default_light(self) -> Dict[str, Any]:
        return {
            'name': 'sun',
            'type': 'directional',
            'cast_shadows': 1,
            'pose': (0, 0, 10, 0, 0, 0),
            'diffuse': (0.8, 0.8, 0.8, 1),
            'specular': (0.2, 0.2, 0.2, 1),
            'attenuation': {
                'range': 1000,
                'constant': 0.9,
                'linear': 0.01,
                'quadratic': 0.001,
            },
            'direction': (-0.5, 0.1, -0.9),
            'spot': {
                'inner_angle': 0,
                'outer_angle': 0,
                'falloff': 0,
            },
        }

    def default_physics(self) -> Dict[str, Any]:
        return {
            "type": PhysicsEngine.ODE.value,
            "max_step_size": 0.001,
            "real_time_factor": 1,
            "real_time_update_rate": 1000
        }

    def default_spherical_coordinates(self) -> Dict[str, Any]:
        return {
            "surface_model": SurfaceModel.EARTH_WGS84.value,
            "latitude_deg": 0,
            "longitude_deg": 0,
            "elevation": 0,
            "heading_deg": 0
        }

    def set_gravity(self, gravity: Tuple[float, float, float]) -> None:
        self.settings["gravity"] = gravity

    def set_ambient_light(self, ambient_light: Tuple[float, float, float, float]) -> None:
        self.settings["ambient_light"] = ambient_light

    def set_background_color(self, background_color: Tuple[float, float, float, float]) -> None:
        self.settings["background_color"] = background_color

    def set_physics(self, physics_engine: PhysicsEngine = PhysicsEngine.ODE, max_step_size: float = 0.001, real_time_factor: float = 1, real_time_update_rate: int = 1000) -> None:
        self.settings["physics"] = {
            "type": physics_engine.value,
            "max_step_size": max_step_size,
            "real_time_factor": real_time_factor,
            "real_time_update_rate": real_time_update_rate
        }

    def set_light(self, light: Dict[str, Any]) -> None:
        self.settings["light"] = light

    def set_magnetic_field(self, magnetic_field: Tuple[float, float, float]) -> None:
        self.settings["magnetic_field"] = magnetic_field

    def set_atmosphere(self, atmosphere: AtmosphereType = AtmosphereType.ADIABATIC) -> None:
        self.settings["atmosphere"] = atmosphere.value

    def set_audio_device(self, audio_device: AudioDevice = AudioDevice.DEFAULT) -> None:
        self.settings["audio_device"] = audio_device.value

    def set_spherical_coordinates(self, surface_model: SurfaceModel = SurfaceModel.EARTH_WGS84, latitude_deg: float = 0, longitude_deg: float = 0, elevation: float = 0, heading_deg: float = 0) -> None:
        self.settings["spherical_coordinates"] = {
            "surface_model": surface_model.value,
            "latitude_deg": latitude_deg,
            "longitude_deg": longitude_deg,
            "elevation": elevation,
            "heading_deg": heading_deg
        }

    def add_object(self, obj: Any) -> None:
        self.objects.append(obj)

    def remove_object(self, obj: Any) -> None:
        self.objects.remove(obj)

    def get_objects(self) -> list:
        return self.objects

    def get_light_xml(self) -> str:
        light = self.settings["light"]
        return f"""
    <light name='{light['name']}' type='{light['type']}'>
      <cast_shadows>{light['cast_shadows']}</cast_shadows>
      <pose>{' '.join(map(str, light['pose']))}</pose>
      <diffuse>{' '.join(map(str, light['diffuse']))}</diffuse>
      <specular>{' '.join(map(str, light['specular']))}</specular>
      <attenuation>
        <range>{light['attenuation']['range']}</range>
        <constant>{light['attenuation']['constant']}</constant>
        <linear>{light['attenuation']['linear']}</linear>
        <quadratic>{light['attenuation']['quadratic']}</quadratic>
      </attenuation>
      <direction>{' '.join(map(str, light['direction']))}</direction>
      <spot>
        <inner_angle>{light['spot']['inner_angle']}</inner_angle>
        <outer_angle>{light['spot']['outer_angle']}</outer_angle>
        <falloff>{light['spot']['falloff']}</falloff>
      </spot>
    </light>
"""

    def get_environment_xml(self) -> str:
        physics = self.settings["physics"]
        spherical_coordinates = self.settings["spherical_coordinates"]
        return f"""
    <gravity>{' '.join(map(str, self.settings['gravity']))}</gravity>
    <magnetic_field>{' '.join(map(str, self.settings['magnetic_field']))}</magnetic_field>
    <atmosphere type='{self.settings['atmosphere']}'/>
    <physics type='{physics["type"]}'>
      <max_step_size>{physics["max_step_size"]}</max_step_size>
      <real_time_factor>{physics["real_time_factor"]}</real_time_factor>
      <real_time_update_rate>{physics["real_time_update_rate"]}</real_time_update_rate>
    </physics>
    <scene>
      <ambient>{' '.join(map(str, self.settings['ambient_light']))}</ambient>
      <background>{' '.join(map(str, self.settings['background_color']))}</background>
      <shadows>1</shadows>
    </scene>
    <audio>
      <device>{self.settings['audio_device']}</device>
    </audio>
    <wind/>
    <spherical_coordinates>
      <surface_model>{spherical_coordinates['surface_model']}</surface_model>
      <latitude_deg>{spherical_coordinates['latitude_deg']}</latitude_deg>
      <longitude_deg>{spherical_coordinates['longitude_deg']}</longitude_deg>
      <elevation>{spherical_coordinates['elevation']}</elevation>
      <heading_deg>{spherical_coordinates['heading_deg']}</heading_deg>
    </spherical_coordinates>
"""

    def get_gz_xml(self) -> str:
        """
        Exports the world to Gazebo XML format including all objects.
        """
        xml_objects = "\n".join([obj.get_gz_xml() for obj in self.objects])
        light_xml = self.get_light_xml()
        environment_xml = self.get_environment_xml()

        return f"""<?xml version="1.0" ?>
<sdf version="1.7">
  <world name="{self.name}">
    {light_xml}
    {xml_objects}
    {environment_xml}
  </world>
</sdf>
"""

    def save_gz_world(self, filename: str) -> None:
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

    # Configure world settings
    world.set_gravity((0, 0, -9.81))
    world.set_ambient_light((0.3, 0.3, 0.3, 1))
    world.set_background_color((0.8, 0.8, 0.8, 1))
    world.set_physics(physics_engine=PhysicsEngine.BULLET, max_step_size=0.002, real_time_factor=1, real_time_update_rate=500)
    world.set_magnetic_field((1e-06, 2e-05, -3e-05))
    world.set_atmosphere(AtmosphereType.ADIABATIC)
    world.set_audio_device(AudioDevice.CUSTOM)
    world.set_spherical_coordinates(surface_model=SurfaceModel.EARTH_WGS84, latitude_deg=0, longitude_deg=0, elevation=0, heading_deg=0)

    custom_light = {
        'name': 'custom_sun',
        'type': 'directional',
        'cast_shadows': 1,
        'pose': (0, 0, 15, 0, 0, 0),
        'diffuse': (0.7, 0.7, 0.7, 1),
        'specular': (0.3, 0.3, 0.3, 1),
        'attenuation': {
            'range': 1500,
            'constant': 0.8,
            'linear': 0.02,
            'quadratic': 0.002,
        },
        'direction': (-0.6, 0.2, -0.8),
        'spot': {
            'inner_angle': 0,
            'outer_angle': 0,
            'falloff': 0,
        },
    }
    world.set_light(custom_light)

    # Create instances of each shape
    box = Box(width=2, height=1, depth=4, x=1, y=2, z=0, color='1 1 0 1')
    sphere = Sphere(radius=1, x=3, y=4, z=0, color='0 1 1 1')
    cylinder = Cylinder(radius=1, length=2, x=5, y=6, z=0, color='1 0 1 1')
    ellipsoid = Ellipsoid(radius_x=1, radius_y=0.5, radius_z=0.5, x=7, y=8, z=0, color='0 1 0 1')
    tetrahedron = Tetrahedron(width=1, depth=1, height=1.5, x=9, y=10, z=0, color='1 0 0 1')
    square_pyramid = SquarePyramid(width=2, depth=2, height=3, x=11, y=12, z=0, color='0 0 1 1')
    cone = Cone(radius=1, height=3, x=13, y=14, z=0, color='1 1 0 1')

    # Add shapes to the world
    world.add_object(box)
    world.add_object(sphere)
    world.add_object(cylinder)
    world.add_object(ellipsoid)
    world.add_object(tetrahedron)
    world.add_object(square_pyramid)
    world.add_object(cone)

    # Save world to file
    world.save_gz_world("example_world")
    print("example_world.sdf saved successfully.")
