# navigation_node.py
import rclpy
from rclpy.node import Node

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.get_logger().info('Navigation Node gestartet!')

def main():
    rclpy.init()
    node = NavigationNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()