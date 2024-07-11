#!/bin/bash

#This code is to start docker images, modified from run.sh in dusty-nv/jetson-inference/docker/run.sh

# >>> OakD camera usb connection requirements
# [2024-04-29 09:06:18.279] [depthai] [warning] USB protocol not available - If running in a container, make sure that the following is set: "-v /dev/bus/usb:/dev/bus/usb --device-cgroup-rule='c 189:* rmw'"

show_help() {
    echo " "
    echo "usage: Starts the Docker container and runs a user-specified command"
    echo " "
    echo "   ./docker/run.sh "
    echo "                   --volume HOST_DIR:MOUNT_DIR"
    echo " "
    echo "args:"
    echo " "
    echo "   --help                       Show this help text and quit"
    echo " "
    echo " "
    echo "   -v, --volume HOST_DIR:MOUNT_DIR Mount a path from the host system into"
    echo "                                   the container.  Should be specified as:"
    echo " "
    echo "                                      -v /my/host/path:/my/container/path"
    echo " "
    echo "                                   These should be absolute paths, and you"
    echo "                                   can specify multiple --volume options."
    echo " "
}





DOCKER_ROOT="/"
DETECTION_DIR="python/training/detection/ssd"
USER_VOLUME=""
CONTAINER_IMAGE="pqed78/opt_base1:V1"
DEV_VOLUME=""
DATA_VOLUME=""

# generate mount commands
DATA_VOLUME=" \
--volume $PWD/data:$DOCKER_ROOT/data \
--volume $PWD/$DETECTION_DIR/data:$DOCKER_ROOT/$DETECTION_DIR/data \
--volume $PWD/$DETECTION_DIR/models:$DOCKER_ROOT/$DETECTION_DIR/models "

while :; do
    case $1 in
        -h|-\?|--help)
            show_help
            exit
            ;;
        --dev)
            DEV_VOLUME=" --volume $PWD:$DOCKER_ROOT "
            ;;
        -v|--volume)
            if [ "$2" ]; then
                USER_VOLUME="$USER_VOLUME --volume $2 "
                shift
            else
                die 'ERROR: "--volume" requires a non-empty option argument.'
            fi
            ;;
        --volume=?*)
            USER_VOLUME="$USER_VOLUME --volume ${1#*=} "
            ;;
        --volume=)
            die 'ERROR: "--volume" requires a non-empty option argument.'
            ;;
        *)   # default case: No more options, so break out of the loop.
            break
    esac

    shift
done

# check for V4L2 devices
V4L2_DEVICES=""

for i in {0..9}
do
	if [ -a "/dev/video$i" ]; then
		V4L2_DEVICES="$V4L2_DEVICES --device /dev/video$i "
	fi
done


# check for display
DISPLAY_DEVICE=""

if [ -n "$DISPLAY" ]; then
	sudo xhost +si:localuser:root
	DISPLAY_DEVICE=" -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix "
fi

# print configuration
print_var() 
{
	if [ -n "${!1}" ]; then                                                # reference var by name - https://stackoverflow.com/a/47768983
		local trimmed="$(echo -e "${!1}" | sed -e 's/^[[:space:]]*//')"   # remove leading whitespace - https://stackoverflow.com/a/3232433    
		printf '%-17s %s\n' "$1:" "$trimmed"                              # justify prefix - https://unix.stackexchange.com/a/354094
	fi
}


print_var "CONTAINER_IMAGE"
print_var "ROS_DISTRO"
print_var "DATA_VOLUME"
print_var "DEV_VOLUME"
print_var "USER_VOLUME"
print_var "USER_COMMAND"
print_var "V4L2_DEVICES"
print_var "DISPLAY_DEVICE"





# run the container
# /proc or /sys files aren't mountable into docker
cat /proc/device-tree/model > /tmp/nv_jetson_model

sudo docker run --runtime nvidia -it --rm \
    --network host \
    --privileged \
    -v /tmp/argus_socket:/tmp/argus_socket \
    -v /etc/enctune.conf:/etc/enctune.conf \
    -v /etc/nv_tegra_release:/etc/nv_tegra_release \
    -v /tmp/nv_jetson_model:/tmp/nv_jetson_model \
    -v /var/run/dbus:/var/run/dbus \
    -v /var/run/avahi-daemon/socket:/var/run/avahi-daemon/socket \
    -v /dev/bus/usb:/dev/bus/usb --device-cgroup-rule='c 189:* rmw' \
    $DISPLAY_DEVICE $V4L2_DEVICES \
    $DATA_VOLUME $USER_VOLUME $DEV_VOLUME \
    $CONTAINER_IMAGE \

    ## -- privileged is for use of GPIO port"
    # # $DATA_VOLUME $USER_VOLUME $DEV_VOLUME \
    # # # >>> OakD camera usb connection requirements
    # # [2024-04-29 09:06:18.279] [depthai] [warning] USB protocol not available - If running in a container, make sure that the following is set: "-v /dev/bus/usb:/dev/bus/usb --device-cgroup-rule='c 189:* rmw'"
    # -v /dev/bus/usb:/dev/bus/usb --device-cgroup-rule='c 189:* rmw'

echo 'source /data/optimus_ws1/install/local_setup.bash' 