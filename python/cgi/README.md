CGI

point

1. 最初に必ず使うプログラム名を明記する
   例えばpythonを用いるならば which pythonを用いて検索する。

#!/usr/bin/python
#!/usr/bin/python3

2. utf-8を指定する

3. http://hogehoge.com?nippon
   のように ? のあとに続く文字を取得する場合は os moduleにあるenvironを用いる
   os.environ['QUERY_STRING']
   ?以降の文字をstring型として値が帰ってくる

4. ?以降の文字列は基本的に
   ?name=tanaka&age=15
   等
   name = value
   が&で繋がっている。
   これをdict型にparseするのは
   parse.parse_qs(txt)
   でdict型で帰ってくる
   {"name":"tanaka", "age":15}

calculator.py: URL?3+5+22 とかするやつ
stocker.py: データベース管理を行うやつ
addstock + name + (amount):在庫追加　amountの指定がない場合1個 在庫
checkstock + (name): 在庫出力　名前指定ない場合すべて
sell name (amount) (price): 販売　amountの指定がない場合1個 priceの指定がない場合無料
checksales: 売上確認
deleteall:すべて削除


