#!/bin/bash

# テスト用スクリプト: omikuji_publisher の動作確認

# ROS 2 ワークスペースのディレクトリ
ws_dir=~/ros2_ws

# ワークスペースへ移動
cd $ws_dir || { echo "ワークスペースが見つかりません: $ws_dir"; exit 1; }

# ワークスペースをビルド
colcon build || { echo "ビルドに失敗しました"; exit 1; }

# ROS 2 環境をソース
source install/setup.bash || { echo "セットアップに失敗しました"; exit 1; }

# omikuji_publisher を起動して 5 秒間実行
timeout 5s ros2 run mypkg omikuji_publisher > /tmp/omikuji_test.log 2>&1 || {
    echo "ノードの起動に失敗しました";
    exit 1;
}

# 結果の確認: 発行されたメッセージをチェック
if grep -q "おみくじ結果を発行しました: 結果: \\(大吉\\|中吉\\|小吉\\|末吉\\|凶\\), 一言:" /tmp/omikuji_test.log; then
    echo "テスト成功: おみくじの結果が正しく出力されました"
    cat /tmp/omikuji_test.log
else
    echo "テスト失敗: 出力内容が期待通りではありません"
    exit 1
fi

