# SPDX-FileCopyrightTest: 2024 Yuta Kannaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class OmikujiPublisher(Node):
    def __init__(self):
        super().__init__('omikuji_publisher')
        self.publisher_ = self.create_publisher(String, 'omikuji', 10)
        self.timer = self.create_timer(1.0, self.publish_omikuji)
        self.count = 0  # パブリッシュ回数を記録
        self.get_logger().info("Omikuji Publisher ノードが起動しました！")

    def publish_omikuji(self):
        results = [
            ("大吉", "今日は最高の一日になります！"),
            ("中吉", "良いことがありそうです。"),
            ("小吉", "少しだけ良いことがあります。"),
            ("末吉", "少し運が味方します。"),
            ("凶", "注意が必要な一日です。")
        ]
        result = random.choice(results)
        msg = String()
        msg.data = f"結果: {result[0]}, 一言: {result[1]}"
        self.publisher_.publish(msg)
        
        # パブリッシュの回数を増やす
        self.count += 1
        
        # 修正: パブリッシュした内容を直接ログに出さない
        self.get_logger().info(f"{self.count} 回目のおみくじをトピック 'omikuji' にパブリッシュしました。")

        # デバッグレベルで詳細を表示したい場合のみ使用
        self.get_logger().debug(f"パブリッシュされた内容: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = OmikujiPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('ノードを停止します。')
    finally:
        node.destroy_node()
        rclpy.shutdown()

