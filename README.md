# README
## 使い方
pip install git+https://github.com/kanegaeyuta/mpc を入力することで実行できる。
もしくは使いたいディレクトリ内にsetup.pyが存在するように配置し、[pip install .]を入力することで実行することが可能になる。


最初はimport mpcによりmpcをインポートし、mpc.mpc()で実行を行うことで簡単に動き方を確認できる。

### mpc.py
#### mpc
自動でいろいろ実行してくれる。

### additive,py
#### secret
入力された２つの秘密情報をシェアに分け、各参加者に分ける。
#### add
各参加者のシェアをすべて足す。

### shamir.py
#### generate_random_polynomial
有限体上の多項式の係数を生成する。
#### evaluate_polynomial
多項式を評価する。
#### generate_shares
秘密をシェアに分割する。
#### plus
シェアから和を計算する。
#### times
シェアから積を計算する。
#### interpolate
シェアから秘密情報を再構築する。

### mt.py
#### make_share
シェアを生成する。
#### make_abc
multiplication triples(以下mt)のa,b,cを作成する。
#### share_de
mtで用いるd,eのシェアを計算する。
#### times
mtを用いた積を計算する。
#### times2
mtを用いた積を計算する。加法的秘密分散を用いる場合、d * eは一回だけでよいのでtimeとtime2の２つ存在する。
#### mts
mtの計算を行う。流れがコメントと一緒に書いてある。
