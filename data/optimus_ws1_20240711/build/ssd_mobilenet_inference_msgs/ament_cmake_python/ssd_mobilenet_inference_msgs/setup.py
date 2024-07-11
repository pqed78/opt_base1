from setuptools import find_packages
from setuptools import setup

setup(
    name='ssd_mobilenet_inference_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('ssd_mobilenet_inference_msgs', 'ssd_mobilenet_inference_msgs.*')),
)
