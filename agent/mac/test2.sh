####
# このコマンドは一回目実行のみcronにスクリプトを登録する。2回目実行の場合は、crontab -lの結果を確認し、実行しない
####
COUNT=`crontab -l | grep "echo hello" | wc -l | sed 's/ //g'`

# 条件: $COUNTが"0"でなければ、ステートメントを実行する
if [[ $COUNT -ne "0" ]]; then
    # 処理を打ち切る
    exit 0
fi

# ファイルmycronにcrontabの設定内容を書き出す
crontab -l > mycron

# ファイルmycronに1行追記する
echo "00 09 * * 1-5 echo hello" >> mycron

# crontabにファイルmycronを設定する
crontab mycron

# mycronを削除する
rm mycron
