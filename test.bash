#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuta Kannaka
# SPDX-License-Identifier: BSD-3-Clause

# テストスクリプトの開始
echo "=== Omikuji Publisher 改良後テスト開始 ==="

# ROS 2 ワークスペースのディレクトリ
ws_dir=~/ros2_ws

# ワークスペースへ移動
cd "$ws_dir" || { echo "ワークスペースが見つかりません: $ws_dir"; exit 1; }

# ワークスペースをビルド
echo "ワークスペースをビルド中..."
colcon build || { echo "ビルドに失敗しました"; exit 1; }

# ROS 2 環境をソース
source install/setup.bash || { echo "ROS 2 環境のセットアップに失敗しました"; exit 1; }

# ログ保存用ディレクトリ
log_dir=/tmp/omikuji_test_logs
mkdir -p "$log_dir"
publisher_log="$log_dir/publisher.log"
subscriber_log="$log_dir/subscriber.log"

# テスト結果の初期化
test_success=true

# **テスト1: Publisher がメッセージを正しく配信しているか**
echo "テスト1: Publisher の配信確認..."
ros2 run mypkg omikuji_publisher > "$publisher_log" 2>&1 &
publisher_pid=$!

# ノードの実行を 10 秒間待機
sleep 10

# ノードを停止
kill "$publisher_pid"
wait "$publisher_pid" 2>/dev/null

# Publisher ログの確認
if grep -q "おみくじ結果を発行しました" "$publisher_log"; then
    echo "  ✅ Publisher は正しくメッセージを配信しています。"
else
    echo "  ❌ Publisher がメッセージを配信していません。ログを確認してください: $publisher_log"
    test_success=false
fi

# **テスト2: Subscriber がメッセージを正しく受信しているか**
echo "テスト2: Subscriber の受信確認..."

# Subscriber をバックグラウンドで実行
ros2 run mypkg omikuji_subscriber > "$subscriber_log" 2>&1 &
subscriber_pid=$!

# Publisher を再度実行して 10 秒間データを送信
ros2 run mypkg omikuji_publisher > "$publisher_log" 2>&1 &
publisher_pid=$!

sleep 10

# ノードを停止
kill "$publisher_pid" "$subscriber_pid"
wait "$publisher_pid" "$subscriber_pid" 2>/dev/null

# Subscriber ログの確認
if grep -q "受信した結果" "$subscriber_log"; then
    echo "  ✅ Subscriber はメッセージを正しく受信しています。"
else
    echo "  ❌ Subscriber がメッセージを受信していません。ログを確認してください: $subscriber_log"
    test_success=false
fi

# **テスト3: 統計の出力が正しいか**
echo "テスト3: 統計出力の確認..."

# Subscriber ログに統計情報が出力されているかチェック
if grep -q "=== おみくじ結果の統計 ===" "$subscriber_log"; then
    echo "  ✅ Subscriber の統計出力を確認しました。"
else
    echo "  ❌ Subscriber の統計出力が確認できません。ログを確認してください: $subscriber_log"
    test_success=false
fi

# テスト結果を出力
if $test_success; then
    echo "=== テスト成功: Omikuji Publisher と Subscriber が正しく動作しました ==="
    exit 0
else
    echo "=== テスト失敗: 上記のエラーを確認してください ==="
    exit 1
fi

