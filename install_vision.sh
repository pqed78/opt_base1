#!/bin/bash


#/env/bin/python -m pip install --extra-index-url https://artifacts.luxonis.com/artifactory/luxonis-python-snapshot-local/ depthai
sudo python -mpip install depthai
sudo python -mpip install ultralytics[export]
# /env/bin/python -m pip install ultralytics[export]
/env/bin/python -m pip uninstall torch opencv-python -y
/env/bin/python -m pip install opencv-python==4.9.0.80


