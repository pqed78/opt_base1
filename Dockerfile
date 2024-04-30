# FROM localhost:5000/jetpack5.1.1-humble-pytorch2
FROM dustynv/ros:humble-pytorch-l4t-r35.3.1

# ENV SHELL /bin/bash
WORKDIR /

COPY install_vision.sh /

RUN pip install virtualenv &&\
    virtualenv --system-site-packages env

RUN echo 'source env/bin/activate' >> ~/.bashrc &&\
    source ~/.bashrc 

RUN chmod +x install_vision.sh &&\
    ./install_vision.sh



