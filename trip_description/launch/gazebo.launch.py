import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command

from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_trip = get_package_share_directory('trip_description')
    urdf_file = os.path.join(pkg_trip, 'urdf', 'trip.urdf')

    # gazebo_model_path = SetEnvironmentVariable(
    #     name='GAZEBO_MODEL_PATH',
    #     value=os.path.join(pkg_trip, 'meshes')
    # )

    gazebo_model_path = SetEnvironmentVariable(
        name='GAZEBO_MODEL_PATH',
        value=get_package_share_directory('trip_description')
    )

    # Launch Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ),
        launch_arguments={'verbose': 'true'}.items()
    )

    # robot_state_publisher publishes TF for URDF
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command(['xacro ', urdf_file])
        }]
    )

    # Spawn the robot in Gazebo using robot_description at desired position
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'trip',
            '-x', '0.0',    # x in meters
            '-y', '0.0',    # y in meters
            '-z', '0.4',    # z in meters
            '-Y', '0.0'    # yaw in radians
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo_model_path,
        gazebo,
        robot_state_publisher,
        spawn_entity,
    ])
