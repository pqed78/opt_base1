# Start from the docker image (pqed78/opt_base0:latest) 
- Image works with Jetpack 5.1.1. installed in Jetson Orin NX and nano, and includes Ultralytics, Depthai, Pytorch. and Opencv for object detection

#Usage 
1. Build: docker build -t pqed78/opt_base1:V1 . 
2. Run: docker run -it --rm --runtime nvidia --name op_base pqed78/opt_base1:V1

# Pip list (FYI)
- OpenCV 4.9.0 installed here is not built with gstreamer.