from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_trip = get_package_share_directory('trip_description')
    urdf_file = os.path.join(pkg_trip, 'urdf', 'trip_rviz.urdf.xacro')

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[
            {'use_sim_time': True},
            {'robot_description': Command(['xacro ', urdf_file])}
        ],
        output='screen',
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_trip, 'rviz', 'display.rviz')],
    )

    return LaunchDescription([
        robot_state_publisher,
        rviz,
    ])