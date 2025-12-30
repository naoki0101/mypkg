#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Naoki Otsubo
# SPDX-License-Identifier : BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
import subprocess

class WarningListener(Node):
    def __init__(self):
        super().__init__('battery_warning_listener')

        self.declare_parameter('enable_notify', False)
        self.enable_notify = bool(self.get_parameter('enable_notify').value)

        self.create_subscription(String, 'battery/warning', self.cb, 10)
        self.get_logger().info('warning listener started')

    def cb(self, msg: String):
        text = msg.data
        self.get_logger().warn(f'\n=======\n{text}\n=======')

        if self.enable_notify:
            try:
                subprocess.run(['notify-send', 'Battery Warning', text], check=False)
            except Exception as e:
                self.get_logger().error(f'notify-send failed: {e}')


def main():
    rclpy.init()
    node = WarningListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


