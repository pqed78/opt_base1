FROM pqed78/opt_base0:latest

# ENV SHELL /bin/bash
WORKDIR /

RUN echo 'source env/bin/activate' >> ~/.bashrc &&\
    echo 'source /data/optimus_ws1/install/local_setup.bash' >> ~/.bashrc  &&\
    source ~/.bashrc 




