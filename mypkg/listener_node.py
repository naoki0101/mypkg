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

        self.levels = [20.0, 15.0, 10.0, 5.0, 4.0, 3.0, 2.0, 1.0]
        self.notified_levels = set()

        self.get_logger().info('Warning listener node started (LEVEL ALERT MODE)')
        self.get_logger().info(f'levels={self.levels}')

        self.sub_percentage = self.create_subscription(Float32, '/battery/warning', self.cb_percentage, 10)

        self.get_logger().info('warning listener started')
    
    def _print_colored(self, msg: str, color_code: str):
        print(f"\033[{color_code}m{msg}\033[0m", flush=True)

    def cb_percentage(self, msg: Float32):
        p = float(msg.data)

        for lvl in self.levels:
            if p <= lvl and lvl not in self.notified:
                self.notified.add(lvl)
                code = "1;33" if lvl >= 20.0 else "1;31"
                self._print_colored(f"[ALART] Battery <= {lvl:.0f}% (now {p:.1f}%)", code)


    def cb_warning(self, msg: String):
        self._print_colored(f"[WARNING TOPIC] {msg.data}", "1;31")

def main():
    rclpy.init()
    node = WarningListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


