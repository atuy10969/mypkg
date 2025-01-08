# SPDX-FileCopyrightTest: 2024 Yuta Kannaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import logging

# ロガーのセットアップ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("OmikujiPublisher")

class OmikujiPublisher(Node):
    def __init__(self):
        super().__init__('omikuji_publisher')
        self.publisher_ = self.create_publisher(String, 'omikuji', 10)
        self.timer = self.create_timer(1.0, self.publish_omikuji)
        self.counter = 0  # パブリッシュ回数をカウント
        logger.info("Omikuji Publisher ノードが起動しました！")

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
        self.counter += 1
        # ログにはシンプルに「パブリッシュ回数」のみ記録
        logger.info(f"{self.counter} 回目のおみくじをパブリッシュしました。")

def main(args=None):
    rclpy.init(args=args)
    node = OmikujiPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        logger.info('ノードを停止します。')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

