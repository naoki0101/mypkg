# バッテリー監視パッケージ                                                                                                                                                                                                                                      

![test](https://github.com/naoki0101/mypkg/actions/workflows/test.yml/badge.svg)

ROS2を用いてバッテリー残量を監視し一定残量以下で警告を出すノードと、その警告を受信するノードを実装したパッケージです。 

## 機能概要

### monitor.py（Publisher）
- バッテリー残量を周期的に取得し、残量を `/battery/percentage` に送る。また、残量がしきい値以下になると `/battery/warning` に警告を出す。

### listener_node.py（Subscriber）
- `/battery/warning` をだし、警告をログに表示する。

### ビルド方法

   cd ~/ros2_ws2025

   colcon build --symlink-install

   source install/setup.bash

### 実行方法

  バッテリー監視ノード

ros2 run mypkg battery_monitor

  警告受信ノード

  ros2 run mypkg warning_listener

## 必要なソフトウェア

-ubuntu 24.04

-ros2 Jazzy

-python 3.12

## ライセンス

  このソフトウェアパッケージは３乗項BSDライセンスのもと使用再頒布できます。

  詳しくはLICENSE欄を見てください。

