import os


from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # param_dir =LaunchConfiguration(
    #     'param_dir',
    #     default=os.path.join(
    #         get_package_share_directory('topic_service_action_rclpy_example'),
    #         'param',
    #         'arithmetic_config.yaml'
    #         )
    #     )
    # ros_namespace = LaunchConfiguration('ros_namespace')
    
    return LaunchDescription([
        # DeclareLaunchArgument(
        #     'param_dir',
        #     default_value=param_dir,
        #     description='Full path of parameter file',

        # ),

        Node(
            package='optimus_vision0',
            executable='streaming_node',
            name='streaming_node',
            # parameters=[param_dir],
            output='screen'

        ),

        Node(
            package='optimus_vision0',
            executable='publication_node',
            name='publication_node',
            # parameters=[param_dir],
            output='screen'

        ),

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node',
            # parameters=[param_dir],
            output='screen'

        ),
    ])