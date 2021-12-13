# "last | more"で Macの起動関連イベントを取得する
# 上記の結果を"result.txt"ファイルに書き込む
last | more > result.txt

# "curl"コマンドでresult.txtファイルを読み込み、対象サーバに送信する
curl -X POST -d @result.txt https://script.google.com/macros/s/xxxxxxxxx/exec
