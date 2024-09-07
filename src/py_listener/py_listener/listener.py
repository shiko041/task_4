import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):

    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(String,'topic',self.call,10)
        self.subscription

    def call(self, msg):
        self.get_logger().info(f'shiko heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    l = Listener()
    rclpy.spin(l)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
