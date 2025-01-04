# Omikuji Publisher (ROS 2)
宿題２
## 概要
このプロジェクトは ROS 2 を使用して、おみくじの結果をトピックに配信するノード「Omikuji Publisher」を作成しました。トピックに配信されたおみくじの結果は、他のノードから受信することもできます。このプログラムは単体で動作するように設計されています。

## メインノード説明

### omikuji_publisher.py
- **定義**: おみくじの結果をトピックに配信するパブリッシャーノード
- **トピック名**: `omikuji`
- **使用メッセージ**:
  - `std_msgs/String` 型のメッセージを配信
  - 配信内容: おみくじの結果 (`大吉`, `中吉`, `小吉`, etc.)

### setup.py
- パッケージのビルドコンフィグを定義
- **エントリーポイント**:
  - `omikuji_publisher = mypkg.omikuji_publisher:main`

### talk_listen.launch.py
- **定義**: `omikuji_publisher` を含むノードをランチファイルを使って起動

## 使用手順

### 1. ビルド
ROS 2 ワークスペースをビルドします:
```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### 2. ノード実行
`omikuji_publisher` を実行:
```bash
ros2 run mypkg omikuji_publisher
```

### 3. トピック内容の確認
トピック配信内容を確認:
```bash
ros2 topic echo /omikuji
```

## ノート
- このノードは教育用のサンプルであり、コードを抽象化した環境での使用を仮定しています。
- サブスクライバーが存在しない場合でも、パブリッシャーとして正常に動作します。

