from enum import Enum

class PhysicsEngine(Enum):
    ODE = "ode"
    BULLET = "bullet"
    SIMBODY = "simbody"
    DART = "dart"

class AtmosphereType(Enum):
    ADIABATIC = "adiabatic"
    CONSTANT = "constant"
    IRRADIANCE = "irradiance"

class SurfaceModel(Enum):
    EARTH_WGS84 = "EARTH_WGS84"
    MARS = "MARS"
    MOON = "MOON"
    CUSTOM = "CUSTOM"

class AudioDevice(Enum):
    DEFAULT = "default"
    CUSTOM = "custom"
