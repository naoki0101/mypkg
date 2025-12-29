import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/naoki/ros2_ws2025/src/mypkg/install/mypkg'
