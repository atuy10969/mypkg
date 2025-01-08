#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class OmikujiPublisher(Node):
    def __init__(self):
        super().__init__('omikuji_publisher')  # ノード名
        self.publisher_ = self.create_publisher(String, 'omikuji', 10)  # トピック名 'omikuji'
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1秒ごとにコールバック実行
        self.fortunes = ['大吉', '中吉', '小吉', '吉', '末吉', '凶']  # おみくじの種類

    def timer_callback(self):
        result = random.choice(self.fortunes)  # ランダムにおみくじを選択
        msg = String()
        msg.data = result
        self.get_logger().info(f"トピック 'omikuji' に配信中: {result}")
        self.publisher_.publish(msg)  # メッセージをトピックに配信

def main(args=None):
    rclpy.init(args=args)
    node = OmikujiPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

