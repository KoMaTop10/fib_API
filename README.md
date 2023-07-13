# フィボナッチ数を返すAPI

## 概要
n番目のフィボナッチ数を返すAPIです

 ~~vercelでのデプロイがうまくいきませんでした。非同期処理の関数があるからうまくいかなかったのかなと思ってます。~~





## 使用ライブラリ

FastAPI

uvicorn

pytest

## 使用方法

```
uvicorn fib_api:app
``` 

でローカルサーバーを立ち上げます

http://localhost:8000/fib?n=10

にアクセスするとn番目のフィボナッチ数をjson形式で出力します(上のURLは10番目のフィボナッチ数)

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

FastAPIでfibonacciの出力をjson形式で出力させるための関数です。
自然数が入力された際に以下のように出力を返します(n = 99のとき)。

```json
{
  "result":218922995834555169026
}
```


- ZeroException

n=0の時のエラー処理を行うためのクラスです。
0が入力された際に以下のようにして出力をjson形式で返します。

```json
{
  "Status":400,
  "ErrorType":"Zero Error",
  "Message":"Type natural number"
}
```

- NegativeException

nが負の自然数の時のエラー処理を行うためのクラスです。
負の自然数が入力された際に以下のようにして出力をjson形式で返します(n=-10とした時)。

```json
{
  "Status":400,
  "ErrorType":"Negative Number Error",
  "Message":"-10 is negative number. type natural number"
}
```


- validation_exception_handler

型エラーが発生した際にエラー処理を行うためのクラスです。

入力が整数型ではない時に以下のようにして出力をjson形式で返します

```json
{
  "Status":400,
  "ErrorType":"Validation Error",
  "Message":"Type natural number"
}
```

### test_fib_api.py
テスト用のコードです。pytestを用いてテストを行います。

テストケースは以下の5つのシナリオで行いました。

- n=1
- n=99
- n=0
- n=-1
- n=3.14
- n=文字列

```
pytest
```

でテストを実行します

