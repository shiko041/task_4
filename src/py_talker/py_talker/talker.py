import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(1, self.call)
        self.i = 0

    def call(self):
        msg = String()
        msg.data = f'shiko talked : {self.i}'
        self.publisher_.publish(msg)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    t = Talker()
    rclpy.spin(t)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
