# Omikuji Publisher (ROS 2)
宿題２

## 概要
このプロジェクトは ROS 2 を使用して、おみくじの結果をトピックに配信するノード「Omikuji Publisher」を作成しました。トピックに配信されたおみくじの結果は、他のノードから受信することもできます。このプログラムは単体で動作するように設計されています.
[![test](https://github.com/atuy10969/mypkg/actions/workflows/test.yml/badge.svg)]
(https://github.com/atuy10969/mypkg/actions/workflows/test.yml)
## ソースコードの場所

- おみくじパブリッシャーのメインスクリプト:
  `src/mypkg/mypkg/omikuji_publisher.py`

- テストスクリプト:
  `src/mypkg/mypkg2/test.bash`

上記のファイルを参照してください。

## 実行方法
~~~
$ ros2 run mypkg omikuji_publisher
~~~
結果
~~~
[INFO] [1735976836.660467563] [omikuji_publisher]: トピック 'omikuji' に配信中: 大吉
[INFO] [1735976837.638824056] [omikuji_publisher]: トピック 'omikuji' に配信中: 中吉
[INFO] [1735976838.639043427] [omikuji_publisher]: トピック 'omikuji' に配信中: 凶
[INFO] [1735976839.640024135] [omikuji_publisher]: トピック 'omikuji' に配信中: 大吉
[INFO] [1735976840.639764321] [omikuji_publisher]: トピック 'omikuji' に配信中: 中吉
[INFO] [1735976841.639819600] [omikuji_publisher]: トピック 'omikuji' に配信中: 小吉
[INFO] [1735976842.639284936] [omikuji_publisher]: トピック 'omikuji' に配信中: 大吉
[INFO] [1735976843.638856091] [omikuji_publisher]: トピック 'omikuji' に配信中: 吉
[INFO] [1735976844.639791235] [omikuji_publisher]: トピック 'omikuji' に配信中: 小吉
~~~

### ノード名: omikuji_publisher

概要: おみくじの結果をランダムに生成し、トピックに配信する ROS 2 ノードです。

役割: トピック omikuji に、おみくじの結果（例: 大吉、中吉）と関連する一言メッセージを送信します。

## 必要なソフトウェア
- python
  
- ROS2
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


