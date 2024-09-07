#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
class EvenOdd(Node):
    def __init__(self):
        super().__init__("DataCollection")
        self.get_logger().info("Data collection has started")
        self.create_timer(1,self.weather)
    def weather(self):
        temp=random.randint(1, 40)
        humidity=random.randint(1,100)
        pressure=random.randint(100,1050)
        self.get_logger().info("temperature: "+str(temp)+" Humidity: "+str(humidity)+" pressure: "+str(pressure))
def main(args=None):
    rclpy.init(args=args)
    node=EvenOdd()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()