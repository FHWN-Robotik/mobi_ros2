"""
Author: Mustafa Algan
Date: 11.03.2024

Describer:  Launch RVIZ and Gazebo with the mobi Model
"""

import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import Command
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # robot model to option m1013 or a0912

    robot_model = 'mobi_4wd'
    # robot_model = 'm1013'

    xacro_file = get_package_share_directory('mobi_ros2') + '/description/' + robot_model + '.urdf.xacro'

    # Robot State Publisher
    robot_state_publisher = Node(package='robot_state_publisher',
                                 executable='robot_state_publisher',
                                 name='robot_state_publisher',
                                 output='both',
                                 parameters=[{'robot_description': Command(['xacro', ' ', xacro_file])
                                              }])
                                            
    # RVIZ Configuration
    rviz_config_dir = os.path.join(get_package_share_directory("mobi_tri"), 'rviz', 'urdf_vis.rviz')

    rviz_node = Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            name='rviz_node',
            parameters=[{'use_sim_time': True}],
            arguments=['-d', rviz_config_dir])

    # Spawn the robot in Gazebo
    spawn_entity_robot = Node(package='gazebo_ros',
                              executable='spawn_entity.py',
                              arguments=['-entity', 'mobi', '-topic', 'robot_description'],
                              output='screen')

    # Start Gazebo with my empty world
    world_file_name = 'empty.world'
    world = os.path.join(get_package_share_directory('mobi_tri'), 'worlds', world_file_name)
    gazebo_node = ExecuteProcess(cmd=['gazebo', '--verbose', world, '-s', 'libgazebo_ros_factory.so'], output='screen')

    return LaunchDescription([robot_state_publisher, rviz_node, spawn_entity_robot, gazebo_node])
