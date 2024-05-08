#!/bin/bash

# >>> OakD camera usb connection requirements
# [2024-04-29 09:06:18.279] [depthai] [warning] USB protocol not available - If running in a container, make sure that the following is set: "-v /dev/bus/usb:/dev/bus/usb --device-cgroup-rule='c 189:* rmw'"

show_help() {
    echo " "
    echo "usage: Starts the Docker container and runs a user-specified command"
    echo " "
    echo "   ./docker/run.sh --container DOCKER_IMAGE"
    echo "                   --volume HOST_DIR:MOUNT_DIR"
    echo "                   --ros ROS_DISTRO"
    echo "                   --run RUN_COMMAND"
    echo " "
    echo "args:"
    echo " "
    echo "   --help                       Show this help text and quit"
    echo " "
    echo "   --dev  Runs the container in development mode, where the source"
    echo "          files are mounted into the container dynamically, so they"
    echo "          can more easily be edited from the host machine."
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
        # -c|--container)  # takes an option argument; ensure it has been specified.
        #     if [ "$2" ]; then
        #         CONTAINER_IMAGE=$2
        #         shift
        #     else
        #         die 'ERROR: "--container" requires a non-empty option argument.'
        #     fi
        #     ;;
        # --container=?*)
        #     CONTAINER_IMAGE=${1#*=} # delete everything up to "=" and assign the remainder.
        #     ;;
        # --container=)  # handle the case of an empty flag
        #     die 'ERROR: "--container" requires a non-empty option argument.'
        #     ;;
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
        # --ros)
        #     if [ "$2" ]; then
        #         ROS_DISTRO=$2
        #         shift
        #     else
        #         ROS_DISTRO="foxy"
        #     fi
        #     ;;
        # --ros=?*)
        #     ROS_DISTRO=${1#*=}
        #     ;;
        # --ros=)
        #     die 'ERROR: "--ros" requires a non-empty option argument.'
        #     ;;
        # -r|--run)
        #     if [ "$2" ]; then
        #         shift
        #         USER_COMMAND=" $@ "
        #     else
        #         die 'ERROR: "--run" requires a non-empty option argument.'
        #     fi
        #     ;;
        # --)
        #     shift
        #     break
        #     ;;
        # -?*)
        #     printf 'WARN: Unknown option (ignored): %s\n' "$1" >&2
        #     ;;
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