# バッテリー監視パッケージ                                                                                                                                                                                                                                      

![test](https://github.com/naoki0101/mypkg/actions/workflows/test.yml/badge.svg)

ROS2を用いてバッテリー残量を監視し一定残量以下で警告を出すノードと、その警告を受信するノードを実装したパッケージです。 

## 機能概要

### monitor.py（Publisher）
- バッテリー残量を周期的に取得し、残量を `/battery/percentage` に送る。また、残量がしきい値以下になると `/battery/warning` に警告を出す。

### listener_node.py（Subscriber）
- `/battery/warning` をだし、警告をログに表示する。

## ビルド方法

   cd ~/ros2_ws2025

   colcon build --symlink-install

   source install/setup.bash

## 実行方法

### 2つの端末を使い実行

  - バッテリー監視ノード

     ros2 run mypkg battery_monitor

  - 警告受信ノード

     ros2 run mypkg warning_listener

### launchで実行
　
  - デフォルト実行

　 ros2 launch mypkg battery_system.launch.py

  - しきい値を指定して実行

　 ros2 launch mypkg battery_system.launch.py warning_threshold:=30.0

## 必要なソフトウェア

 - ubuntu 24.04

 - ros2 Jazzy

 - python 3.12

## ライセンス

  - このソフトウェアパッケージは３乗項BSDライセンスのもと使用再頒布できます。

  - 詳しくはLICENSE欄を見てください。

## 参考文献

[1] ロボットシステム学（講義資料）
    https://ryuichiueda.github.io/slides_marp/robosys2025/ 

[2] takanory, “Pythonでファイルの読み書きを行う方法（openの基本）”,
Qiita, 2018. https://qiita.com/takanory/items/8c1b3d7c4f5c2bfb8b6d

[3] nishimura, “Pythonの例外処理（try-except）の基本”,
Qiita, 2019. https://qiita.com/nishimura/items/2f3a4f0b3c2a2e7a1b3e

[4] atsushieno, “ROS2でPythonノードを作ってみる（rclpy入門）”,
Qiita, 2022. https://qiita.com/atsushieno/items/1a7b4e1d1f9a4b6d8e92

[5] KNR109, “ROS2のTopic通信をPythonで試す”,
Qiita, 2021. https://qiita.com/KNR109/items/8a1c0f2bfa4e92c43d1f

[6] matsumoto-r, “bashスクリプトの基本構文まとめ”,
Qiita, 2017. https://qiita.com/matsumoto-r/items/9c6d64c5f5e6c6b7b0d4

© 2025 Naoki Otsubo
