# タイトル：年金受給額の限界に挑むサイト
カート機能を利用することにより最大の年金の受給額を追求しつつ各種年金についても学べるサイト。

![image](https://user-images.githubusercontent.com/105050060/220826944-3ebb39d2-7047-4156-93f3-881f4f61d0a3.png)

## URL:  https://nennsaito.pythonanywhere.com/home/

## 使用技術
・Python 3.8.10
・Django 4.1.3
・SQLite
・Ubuntu
・PythonAnywhere

## 構造  
saito/models.py = テーブル作成のためのモデルクラス　カートに追加できる各種年金のデータを格納。  
saito/tests.py = 正規の手順を踏まないとカートに年金を追加できないことを確認するためのテストプログラム。  
saito/views.py = メインとなるプログラム。カートへの追加・削除・他のページへの遷移等。  

sekai/views.py = 用意されている中からランダムにURLをページに出力するためのプログラム。  

templates/home.html = ホーム画面　各種年金を確認できるページもここ。  
templates/cart.html = カート画面。受給金額の合計等を表示。  
templates/kennsakusuru.html = 上記sekai/views.pyのURLが表示されるページ  
templates/product_detail.html = 各種年金の説明と追加が可能なページ。ただし趣旨に合わないため説明のみで追加できない年金あり。  
