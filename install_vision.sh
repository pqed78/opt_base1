#!/bin/bash


/env/bin/python -m pip install --extra-index-url https://artifacts.luxonis.com/artifactory/luxonis-python-snapshot-local/ depthai
/env/bin/python -m pip install ultralytics[export]
/env/bin/python -m pip uninstall torch opencv-python -y
/env/bin/python -m pip install opencv-python==4.9.0.80


# >>> import depthai
# [2024-04-29 09:06:18.279] [depthai] [warning] USB protocol not available - If running in a container, make sure that the following is set: "-v /dev/bus/usb:/dev/bus/usb --device-cgroup-rule='c 189:* rmw'"


