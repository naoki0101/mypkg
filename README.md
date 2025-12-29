# バッテリー監視パッケージ                                                                                                                                                                                                                                      

![test](https://github.com/naoki0101/mypkg/actions/workflows/test.yml/badge.svg

ROS2を用いてバッテリー残量を監視し一定残量以下で警告を出すノードと、その警告を受信するノードを実装したパッケージです。 

## 機能概要

### monitor.py（Publisher）
- バッテリー残量を周期的に取得し、残量を `/battery/percentage` に送る。また、残量がしきい値以下になると `/battery/warning` に警告を出す。

### listener_node.py（Subscriber）
- `/battery/warning` をだし、警告をログに表示する。


## 必要なソフトウェア
　python    テスト済み： 3.11～3.14

## テスト環境

　Ubuntu 24.04


## ライセンス

  このソフトウェアパッケージは３乗項BSDライセンスのもと使用再頒布できます。

  詳しくはLICENSE欄を見てください。

