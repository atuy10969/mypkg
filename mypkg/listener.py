#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')  # ノード名
        self.subscription = self.create_subscription(
            String,
            'omikuji',
            self.listener_callback,
            10)
        self.subscription  # 購読を保持

    def listener_callback(self, msg):
        fortune = msg.data
        comments = {
            '大吉': '今日は最高の日！思い切った行動をしてみよう！',
            '中吉': '良いことが起こる予感！いつも通り過ごして吉。',
            '小吉': '小さな幸せがやってくるかも。身近な人に感謝を。',
            '吉': '穏やかで平和な一日を過ごせそうです。',
            '末吉': '少し我慢が必要な日。でもその先に良いことが！',
            '凶': '慎重に行動しましょう。無理せず休むのも吉。',
        }
        comment = comments.get(fortune, '結果が不明です。')
        self.get_logger().info(f"受信したおみくじの結果: {fortune} - {comment}")

def main(args=None):
    rclpy.init(args=args)
    listener = Listener()
    try:
        rclpy.spin(listener)
    except KeyboardInterrupt:
        pass
    finally:
        listener.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

