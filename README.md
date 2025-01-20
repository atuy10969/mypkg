# Omikuji Publisher (ROS 2)
宿題２

## 概要
ROS 2 パッケージ mypkg に含まれるノード「Omikuji Publisher」を使用し、おみくじの結果をランダムに生成してトピック /omikuji に配信します。
さらに、このノードは実行終了時に、配信したおみくじ結果の統計を表示します。表示される統計情報は、各結果（大吉、中吉、小吉、吉、末吉、凶）が全体に占める割合をパーセンテージで示します。


[![test](https://github.com/atuy10969/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/atuy10969/mypkg/actions/workflows/test.yml)



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
[INFO] [1737348481.131428031] [omikuji_publisher]: Omikuji Publisher ノードが起動しました！
[INFO] [1737348482.108131107] [omikuji_publisher]: 1 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 凶, 一言: 今日は慎重に行動しましょう。
[INFO] [1737348483.108746624] [omikuji_publisher]: 2 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 末吉, 一言: 少し運が味方します。
[INFO] [1737348484.109040197] [omikuji_publisher]: 3 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 中吉, 一言: 今日はいいことが起こるかもしれません！
[INFO] [1737348485.108353961] [omikuji_publisher]: 4 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 小吉, 一言: 少しだけ良いことがあります。
[INFO] [1737348486.108481012] [omikuji_publisher]: 5 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 小吉, 一言: 少しだけ良いことがあります。
[INFO] [1737348487.109312260] [omikuji_publisher]: 6 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 末吉, 一言: 少し運が味方します。
[INFO] [1737348488.108378678] [omikuji_publisher]: 7 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 吉, 一言: 良い運勢です！
[INFO] [1737348489.108782171] [omikuji_publisher]: 8 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 大吉, 一言: 今日は最高の一日になります！
[INFO] [1737348490.108621773] [omikuji_publisher]: 9 回目のおみくじをトピック "omikuji" にパブリッシュしました: 結果: 大吉, 一言: 今日は最高の一日になります！
・
・
・
停止した時↓

 [omikuji_publisher]: === おみくじ結果の統計 ===
[INFO] [1737348517.540803116] [omikuji_publisher]: 大吉: 4 回 (11.11%)
[INFO] [1737348517.541591551] [omikuji_publisher]: 中吉: 3 回 (8.33%)
[INFO] [1737348517.542298712] [omikuji_publisher]: 小吉: 7 回 (19.44%)
[INFO] [1737348517.543028903] [omikuji_publisher]: 吉: 9 回 (25.00%)
[INFO] [1737348517.543909723] [omikuji_publisher]: 末吉: 9 回 (25.00%)
[INFO] [1737348517.544628001] [omikuji_publisher]: 凶: 4 回 (11.11%)
[INFO] [1737348517.545435465] [omikuji_publisher]: =========================
[INFO] [1737348517.546274734] [omikuji_publisher]: Omikuji Publisher ノードを停止します。

~~~


## テスト環境
- 自動テスト: GitHub Actions を使用
  - テスト内容: パッケージのビルドおよび動作確認
  - [GitHub Actions ワークフローはこちら](https://github.com/atuy10969/mypkg/actions/workflows/test.yml)


## システム環境

- **OS:** Ubuntu 20.04.6 LTS (Focal Fossa)
- **ROS 2 Distribution:** Foxy

## テスト環境
- ubuntu-20.04
- GitHub Actions

## ライセンスや著作権
 - このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可される

 - このパッケージのコードは、下記のスライド　(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html)

- 2025 Yuta Kannaka



