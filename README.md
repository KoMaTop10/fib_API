# フィボナッチ数を返すAPI

## 概要
n番目のフィボナッチ数を返すAPIです

vercelでのデプロイがうまくいきませんでした。非同期処理の関数があるからうまくいかなかったのかなと思ってます。

簡単な構築のAPIは[こちら][link-1]になります

[link-1]: https://github.com/KoMaTop10/fib_API_test

## 使用ライブラリ

FastAPI

uvicorn

pytest

## 使用方法

`uvicorn fib_api:app` 

でローカルサーバーを立ち上げます

localhost:8000/fib/?n=10

にアクセスするとn番目のフィボナッチ数をjson形式で出力します(上は10番目のフィボナッチ数)

## コード概要

### fib_api.py

FastAPIを使って作成しました。

- fibonacci

n番目のフィボナッチ数を返す関数です。

出力例は以下のようになります
  
```
fibonacci(1)
>>> 1


fibonacci(5)
>>> 5


fibonacci(99)
>>> 218922995834555169026


fibonacci(-1)
>>> 0
```

- get_fib

FastAPIでfibonacciの出力をjson形式で出力させるための関数です

### test_fib_api.py
テスト用のコードです。

テストケースは以下の5つのシナリオで行いました。

- n=1
- n=99
- n=0
- n=-1
- n=文字列

`pytest`

でテストを実行します

