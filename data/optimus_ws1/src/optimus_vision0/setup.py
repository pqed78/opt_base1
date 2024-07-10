#!/usr/bin/env python3

import glob
import os

from setuptools import find_packages
from setuptools import setup


package_name = 'optimus_vision0'
util = 'optimus_vision0/util'   # if additional classes are added.

setup(
    name=package_name,
    version='0.0.0',
    # packages=find_packages(exclude=['test']),
    packages=[package_name, util],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name+'/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='optimus',
    maintainer_email='taekyong.hwang@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'streaming_node=optimus_vision0.streaming_node:main',
            'publication_node=optimus_vision0.publication_node:main',
        ],
    },
)