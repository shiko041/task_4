#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
class EvenOdd(Node):
    def __init__(self):
        super().__init__("EvenOdd")
        self.get_logger().info("Even and odd checker started")
        self.create_timer(1,self.checkEven)
    def checkEven(self):
        num=random.randint(1, 1000)
        if num%2==0:
            self.get_logger().info(str(num)+" is Even")
        else:
            self.get_logger().info(str(num)+ " is Odd")
def main(args=None):
    rclpy.init(args=args)
    node=EvenOdd()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()