# GazeboWorldGen

GazeboWorldGen is a library for generating Gazebo worlds through few lines of python code. It is a work in progress and is not yet ready for use.

The goal of this project is to provide a fast way to generate Gazebo worlds for robotics simulations. 

## TODO
  - [x] Ad a few basic shapes
  - [x] Add world parameters, such as gravity etc.
  - [ ] Be able to add terrain to the world through heightmaps created by the user as numpy arrays
  - [ ] Add a collison sahpe of the actual objects in the world, not only the visual shape
  - [ ] Be able to give properties to the objects in the world, like friction, mass, follow gravity, follow terrain or a path, etc. Might be revisited multiple times.
  - [ ] Be able to cluster object in the world, through a subclass. That can rotate and move together.
  - [ ] Give the object more advanced colors, like textures or materials or even animations, being a light source, etc.
  - [ ] Add support to fly simulated drones in the world, either through ROS or ardupilot, px4, etc. maybe all of them
  - [ ] Add support for adding sensors in the world.