#!/bin/bash

# テストスクリプトの開始
echo "=== おみくじシステムテスト開始 ==="

# デフォルトディレクトリ
dir=~
[ "$1" != "" ] && dir="$1"

# ROS 2 ワークスペースへ移動
cd $dir/ros2_ws || { echo "指定されたディレクトリが存在しません: $dir/ros2_ws"; exit 1; }

# ビルドと環境設定
echo "ワークスペースをビルド中..."
colcon build || { echo "ビルドに失敗しました"; exit 1; }
source $dir/ros2_ws/install/setup.bash

# テスト用にノードを一定時間起動
echo "Omikuji Publisher ノードを起動します..."
timeout 10 ros2 run mypkg omikuji_publisher | tee /tmp/mypkg_test.log

# ログファイルの内容を確認
echo "ログファイルの結果を解析中..."
cat /tmp/mypkg_test.log | grep -E '回目のおみくじをパブリッシュしました。'

# テスト結果表示
if [ $? -eq 0 ]; then
    echo "=== おみくじシステムテスト成功！ ==="
else
    echo "=== おみくじシステムテスト失敗 ==="
    echo "ログを確認してください: /tmp/mypkg_test.log"
fi

