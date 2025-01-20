# SPDX-FileCopyrightTest: 2024 Yuta Kannaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import String

class OmikujiPublisher(Node):
    def __init__(self):
        super().__init__('omikuji_publisher')
        self.publisher_ = self.create_publisher(String, 'omikuji', 10)
        self.timer = self.create_timer(1.0, self.publish_omikuji)
        self.get_logger().info('Omikuji Publisher ノードが起動しました！')

        # 結果のカウント用変数
        self.result_counts = {
            '大吉': 0,
            '中吉': 0,
            '小吉': 0,
            '吉': 0,
            '末吉': 0,
            '凶': 0
        }
        self.total_count = 0

    def publish_omikuji(self):
        # 確率に基づいてランダムに結果を選択
        result = self.generate_random_omikuji()
        self.result_counts[result] += 1
        self.total_count += 1

        # 結果をトピックに配信
        message = String()
        message.data = f'結果: {result}, 一言: {self.get_message_by_result(result)}'
        self.publisher_.publish(message)
        self.get_logger().info(f'{self.total_count} 回目のおみくじをトピック "omikuji" にパブリッシュしました: {message.data}')

    def generate_random_omikuji(self):
        # おみくじの結果とそれぞれの割合（実際の割合を参考に）
        results = ['大吉', '中吉', '小吉', '吉', '末吉', '凶']
        probabilities = [0.23, 0.10, 0.13, 0.24, 0.19, 0.11]

        # 確率に基づいてランダムに結果を選択
        return random.choices(results, probabilities)[0]

    def get_message_by_result(self, result):
        # おみくじ結果に応じたメッセージを返す
        messages = {
            '大吉': '今日は最高の一日になります！',
            '中吉': '今日はいいことが起こるかもしれません！',
            '小吉': '少しだけ良いことがあります。',
            '吉': '良い運勢です！',
            '末吉': '少し運が味方します。',
            '凶': '今日は慎重に行動しましょう。'
        }
        return messages[result]

    def display_statistics(self):
        # 確率分布を計算して表示
        self.get_logger().info("=== おみくじ結果の統計 ===")
        for result, count in self.result_counts.items():
            percentage = (count / self.total_count) * 100 if self.total_count > 0 else 0
            self.get_logger().info(f'{result}: {count} 回 ({percentage:.2f}%)')
        self.get_logger().info("=========================")


def main(args=None):
    rclpy.init(args=args)
    node = OmikujiPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        # ノード停止時に統計を表示
        node.display_statistics()
        node.get_logger().info('Omikuji Publisher ノードを停止します。')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

