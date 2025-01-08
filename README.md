# Omikuji Publisher (ROS 2)
宿題２

## 概要
このプロジェクトは ROS 2 を使用して、おみくじの結果をトピックに配信するノード「Omikuji Publisher」を作成しました。ランダムに生成したおみくじの結果をトピック /omikuji に配信します。

[![test](https://github.com/atuy10969/mypkg/actions/workflows/test.yml/badge.svg)]
(https://github.com/atuy10969/mypkg/actions/workflows/test.yml)
## ソースコードの場所

- おみくじパブリッシャーのメインスクリプト:
  `src/mypkg/mypkg/omikuji_publisher.py`

- テストスクリプト:
  `src/mypkg/mypkg2/test.bash`

mypkgがsubmoduleになってしまい、何度も試して変更を試みたのですがgithub上から作成したものを見ることができないので、お手数をおかけしますが上記のファイルを参照してください。

## コマンドと実行例

**端末1**
~~~
$ ros2 run mypkg omikuji_publisher
~~~

**端末2**
~~~
$ ros2 topic echo /omikuji
~~~

## 実行例
~~~
data: '結果: 末吉, 一言: 少し運が味方します。'
---
data: '結果: 小吉, 一言: 少しだけ良いことがあります。'
---
data: '結果: 末吉, 一言: 少し運が味方します。'
---
data: '結果: 大吉, 一言: 今日は最高の一日になります！'
---
data: '結果: 小吉, 一言: 少しだけ良いことがあります。'
---
data: '結果: 大吉, 一言: 今日は最高の一日になります！'
---
data: '結果: 末吉, 一言: 少し運が味方します。'
---
data: '結果: 大吉, 一言: 今日は最高の一日になります！'
~~~

### ノード名: omikuji_publisher

概要: おみくじの結果をランダムに生成し、トピックに配信する ROS 2 ノードです。

役割: トピック omikuji に、おみくじの結果（例: 大吉、中吉）と関連する一言メッセージを送信します。

## システム環境

- **OS:** Ubuntu 20.04.6 LTS (Focal Fossa)
- **ROS 2 Distribution:** Foxy

## テスト環境
- ubuntu-20.04
## 作成者
23C1041 甘中雄太
未来ロボティクス学科所属
## ライセンスや著作権
 - このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可される

 - このパッケージのコードは、下記のスライド　(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html)

-2025 Yuta Kannaka


