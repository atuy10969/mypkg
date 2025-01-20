#!/usr/bin/env python3
import sys
import os

# omikuji_publisher.py がこのファイルと同じディレクトリにあると仮定してパスを追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from unittest.mock import MagicMock
from omikuji_publisher import OmikujiPublisher


class TestOmikujiPublisher(unittest.TestCase):

    def setUp(self):
        # OmikujiPublisherのインスタンスを作成
        self.node = OmikujiPublisher()

    def test_generate_random_omikuji(self):
        # ランダムに結果が生成されるかをテスト
        random.seed(42)  # 再現性のあるテストのためにシードを固定
        result = self.node.generate_random_omikuji()
        self.assertIn(result, ['大吉', '中吉', '小吉', '吉', '末吉', '凶'])

    def test_publish_omikuji(self):
        # publish_omikuji メソッドが正しく動作するかをテスト
        self.node.publisher_ = MagicMock()  # publisherをモック
        self.node.publish_omikuji()  # 実行

        # publisherが一度呼ばれたかを確認
        self.node.publisher_.publish.assert_called_once()

    def test_display_statistics(self):
        # 統計表示のメソッドが正しく動作するかをテスト
        self.node.result_counts = {
            '大吉': 10,
            '中吉': 5,
            '小吉': 2,
            '吉': 3,
            '末吉': 0,
            '凶': 1
        }
        self.node.total_count = 21

        # ログ出力をモックして、表示される内容を確認
        with self.assertLogs(self.node.get_logger(), level='INFO') as log:
            self.node.display_statistics()

        self.assertIn('大吉: 10 回 (47.62%)', log.output[0])
        self.assertIn('中吉: 5 回 (23.81%)', log.output[1])
        self.assertIn('小吉: 2 回 (9.52%)', log.output[2])
        self.assertIn('吉: 3 回 (14.29%)', log.output[3])
        self.assertIn('末吉: 0 回 (0.00%)', log.output[4])
        self.assertIn('凶: 1 回 (4.76%)', log.output[5])

if __name__ == '__main__':
    unittest.main()

