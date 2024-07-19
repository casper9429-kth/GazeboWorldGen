import numpy as np
import trimesh
import os

# Directory to save models
output_dir = "gazebo_models"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_model_directory(model_name):
    directory = os.path.join(output_dir, model_name, "meshes")
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def write_model_config(model_name, parent_directory):
    config_content = f"""<?xml version="1.0" ?>
<model>
  <name>{model_name}</name>
  <version>1.0</version>
  <sdf version="1.6">model.sdf</sdf>
  <author>
    <name>Your Name</name>
    <email>your.email@example.com</email>
  </author>
  <description>
    {model_name} model
  </description>
</model>
"""
    with open(os.path.join(parent_directory, 'model.config'), 'w') as f:
        f.write(config_content)

def write_model_sdf(model_name, parent_directory, dae_file, scale=[1,1,1], color='0.5 0.5 0.5 1.0'):
    sdf_content = f"""<?xml version="1.0" ?>
<sdf version="1.6">
  <model name="{model_name}">
    <static>true</static>
    <link name="link">
      <visual name="visual">
        <geometry>
          <mesh>
            <uri>model://{model_name}/meshes/{dae_file}</uri>
            <scale>{' '.join(map(str, scale))}</scale>
          </mesh>
        </geometry>
        <material>
          <ambient>{color}</ambient>
          <diffuse>{color}</diffuse>
        </material>
      </visual>
      <collision name="collision">
        <geometry>
          <mesh>
            <uri>model://{model_name}/meshes/{dae_file}</uri>
            <scale>{' '.join(map(str, scale))}</scale>
          </mesh>
        </geometry>
      </collision>
    </link>
  </model>
</sdf>
"""
    with open(os.path.join(parent_directory, 'model.sdf'), 'w') as f:
        f.write(sdf_content)

def save_collada(mesh, directory, name):
    dae_file = f'{name}.dae'
    mesh.export(os.path.join(directory, dae_file))
    return dae_file

def create_ellipsoid(rx, ry, rz, name="ellipsoid", scale=[1,1,1], color='0.5 0.5 0.5 1.0'):
    directory = create_model_directory(name)
    parent_directory = os.path.dirname(directory)
    u = np.linspace(0, 2 * np.pi, 32)
    v = np.linspace(0, np.pi, 16)
    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones(np.size(u)), np.cos(v))

    vertices = np.stack((x.flatten(), y.flatten(), z.flatten()), axis=-1)
    faces = []

    for i in range(len(u) - 1):
        for j in range(len(v) - 1):
            idx = lambda i, j: i * len(v) + j
            faces.append([idx(i, j), idx(i + 1, j), idx(i + 1, j + 1)])
            faces.append([idx(i, j), idx(i + 1, j + 1), idx(i, j + 1)])

    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    dae_file = save_collada(mesh, directory, name)
    write_model_config(name, parent_directory)
    write_model_sdf(name, parent_directory, dae_file, scale, color)

def create_tetrahedron(width, depth, height, name="tetrahedron", scale=[1,1,1], color='0.5 0.5 0.5 1.0'):
    directory = create_model_directory(name)
    parent_directory = os.path.dirname(directory)
    vertices = np.array([
        [0, 0, height],
        [width / 2, depth / 2, 0],
        [-width / 2, depth / 2, 0],
        [0, -depth / 2, 0]
    ])
    faces = [[0, 1, 2], [0, 2, 3], [0, 3, 1], [1, 2, 3]]

    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    dae_file = save_collada(mesh, directory, name)
    write_model_config(name, parent_directory)
    write_model_sdf(name, parent_directory, dae_file, scale, color)

def create_square_pyramid(width, depth, height, name="square_pyramid", scale=[1,1,1], color='0.5 0.5 0.5 1.0'):
    directory = create_model_directory(name)
    parent_directory = os.path.dirname(directory)
    vertices = np.array([
        [0, 0, height],
        [width / 2, depth / 2, 0],
        [-width / 2, depth / 2, 0],
        [-width / 2, -depth / 2, 0],
        [width / 2, -depth / 2, 0]
    ])
    faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 1], [1, 2, 3], [3, 4, 1]]

    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    dae_file = save_collada(mesh, directory, name)
    write_model_config(name, parent_directory)
    write_model_sdf(name, parent_directory, dae_file, scale, color)

def create_cone(radius, height, name="cone", scale=[1,1,1], color='0.5 0.5 0.5 1.0'):
    directory = create_model_directory(name)
    parent_directory = os.path.dirname(directory)
    mesh = trimesh.creation.cone(radius=radius, height=height, sections=32)
    dae_file = save_collada(mesh, directory, name)
    write_model_config(name, parent_directory)
    write_model_sdf(name, parent_directory, dae_file, scale, color)

# Create models
create_ellipsoid(1.0, 1.0, 1.0, "ellipsoid", scale=[1, 1, 1], color='1 1 1 1')
create_tetrahedron(1.0, 1.0, 1.0, "tetrahedron", scale=[1, 1, 1], color='1 1 1 1')
create_square_pyramid(1.0, 1.0, 1.0, "square_pyramid", scale=[1, 1, 1], color='1 1 1 1')
create_cone(1.0, 1.0, "cone", scale=[1, 1, 1], color='1 1 1 1')
