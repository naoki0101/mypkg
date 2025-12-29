import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from pathlib import Path

class BatteryMonitor(Node):
    def __init__(self):
        super().__init__('battery_monitor')
        self.pub_percentage = self.create_publisher(Float32, 'battery/percentge', 10)
        self.pub_warning = self.create_publisher(String, 'battery/warning', 10)
        self.declare_parameter('battery_path', '/sys/class/power_supply/BAT1/capacity')
        self.declare_parameter('warning_threshold', 20.0)
        self.battery_path = Path(self.get_parameter('battery_path').value)
        self.threshold = float(self.get_parameter('warning_threshold').value)
        self.create_timer(5.0, self.timer_callback)
        self.get_logger().info('Battey monitor node started')

    
    def read_battery_percentage(self):
        try:
            with self.battery_path.open() as f:
                return float(f.read().strip())
        except Exception as e:
            self.get_logger().error(f'Battery read failed: {e}')
            return None

    def timer_callback(self):
        percentage = self.read_battery_percentage()
        if percentage is None:
            return

        msg = Float32()
        msg.data = percentage
        self.pub_percentage.publish(msg)
        self.get_logger().info(f'Battery: {percentage:.1f}%')

        if percentage <= self.threshold:
            warn = String()
            warn.data = f'WARNING: Battery low ({percentage:.1f}%)'
            self.pub_warning.publish(warn)
            self.get_logger().warn(warn.data)

def main():
    rclpy.init()
    node = BatteryMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

