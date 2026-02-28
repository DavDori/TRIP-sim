import os

from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription,
    RegisterEventHandler,
    DeclareLaunchArgument,
)
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.event_handlers import OnProcessExit

def generate_launch_description():

    pkg_trip = get_package_share_directory('trip_description')
    urdf_file = os.path.join(pkg_trip, 'urdf', 'trip.urdf.xacro')
    use_rviz = LaunchConfiguration('use_rviz')

    declare_use_rviz = DeclareLaunchArgument(
        'use_rviz',
        default_value='false',
        description='Launch RViz'
    )

    robot_controllers = PathJoinSubstitution(
        [
            pkg_trip,
            "config",
            "controllers.yaml",
        ]
    )

    # Launch Gazebo Classic
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
        parameters=[
            {'use_sim_time': True},
            {'robot_description': Command(['xacro ', urdf_file])}
        ],
        output='screen',
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
    )

    lidar_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["lidar_roll_joint_velocity_controller", "--param-file", robot_controllers],
        output="screen",
    )

    wheels_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["wheels_velocity_controller", "--param-file", robot_controllers],
        output="screen",
    )

    # Vizualization of the TF and point cloud from the simulated robot. Note that it 
    # will not show the model while running with Gazebo because of compatibility issues
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', os.path.join(pkg_trip, 'rviz', 'display.rviz')],
        output='screen',
        condition=IfCondition(use_rviz)
    )

    # Spawn the robot in Gazebo using robot_description at desired position
    spawn_trip = Node(
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

    controller_spawners = RegisterEventHandler(
        OnProcessExit(
            target_action=spawn_trip,
            on_exit=[
                joint_state_broadcaster_spawner,
                lidar_spawner,
                wheels_spawner,
            ],
        )
    )

    return LaunchDescription([
        declare_use_rviz,
        gazebo,
        robot_state_publisher,
        spawn_trip,
        controller_spawners,
        rviz,
    ])