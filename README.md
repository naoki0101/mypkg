# バッテリー監視パッケージ                                                                                                                                                                                                                                      

![test](https://github.com/naoki0101/mypkg/actions/workflows/test.yml/badge.svg)

ROS2を用いてバッテリー残量を監視し一定残量以下で警告を出すノードと、その警告を受信するノードを実装したパッケージです。 

## 機能概要

### monitor
- バッテリー残量を周期的に取得し、残量を `/battery/percentage` に送る。また、残量がしきい値以下になると `/battery/warning` に警告を出す。

### listener_node

- `/battery/warning` を受け、警告をログに表示する。

## 実行方法

### 2つの端末を使い実行

  - バッテリー監視ノード
    
     ```python
     ros2 run mypkg battery_monitor
     ```

    起動すると以下のようなログが表示されます

     [battery_monitor]: Battey monitor node started

     [battery_monitor]: Battery: 55.0%

### launchで実行
  - デフォルト実行

    ```bash
    ros2 launch mypkg battery_system.launch.py
    ```

  - しきい値を指定して実行
 
    ```python
    ros2 launch mypkg battery_system.launch.py warning_threshold:=30.0
    ```

## トピックの確認

   - バッテリー残量の表示

   ```bash
   ros2 topic echo /battery/percentage
   ```
     
   出力例

   data: 56.0

## 必要なソフトウェア

  - ubuntu 24.04

  - ros2 Jazzy

  - python 3.12

## ライセンス

  - このソフトウェアパッケージは3条項BSDライセンスのもと使用再頒布できます。

    詳しくはLICENSE欄を見てください。

## 参考文献

[1] ロボットシステム学（講義資料）, Ryuichi Ueda, 2025

   https://github.com/ryuichiueda/slides_marp/blob/master/robosys2025/README.md

[2] “[Python]ファイル操作まとめ” , @yasagureprog, 2025

   https://qiita.com/yasagureprog/items/69c140aecf325783fcca

[3] “Python例外処理入門” , Keisuke Tanabe, 2025  

   https://frkz.jp/study/python/exception

[4] “ROS2でPythonノードを作る”　, @mol, 2023　

   https://zenn.dev/mol0921/articles/f8b789d90abb35

[5] “Bashシェルとは何か？基本文法と実践例” , Seiji Takami, 2025

   https://atnettec.com/2026/01/08/what-is-the-bash-shell/

© 2025 Naoki Otsubo
