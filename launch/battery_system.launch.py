#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Naoki Otsubo
# SPDX-License-Identifier : BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration 

def generate_launch_description():

    warning_threshold = LaunchConfiguration('warning_threshold')

    battery_monitor = launch_ros.actions.Node(
            package='mypkg',
            executable='battery_monitor',
            output='screen',
            parameters=[{
                'warning_threshold': warning_threshold,
            }],    
    )

    warning_listener = launch_ros.actions.Node(
            package='mypkg',
            executable='warning_listener',
            output='screen',
    )

    return launch.LaunchDescription([
        DeclareLaunchArgument(
            'warning_threshold',
            default_value='20.0',
            description='warning_threshold (%)'
        ),
        battery_monitor,
        warning_listener
    ])
