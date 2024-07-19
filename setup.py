# setup.py

from setuptools import setup, find_packages

setup(
    name='GazeboWorldGen',
    version='0.1.0',
    description='A library to generate Gazebo worlds in Python',
    author='Casper Augustsson',
    author_email='casper9429@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    test_suite='tests',
)
