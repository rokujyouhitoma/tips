# このコマンドは一回目実行のみcronにスクリプトを登録する。2回目実行の場合は、crontab -lの結果を確認し、実行しない
COUNT=`crontab -l | grep "echo hello" | wc -l | sed 's/ //g'`

# 条件: $COUNTが"0"でなければ
if [[ $COUNT -ne "0" ]]; then
    # 処理を打ち切る
    exit 0
fi

crontab -l > mycron
echo "00 09 * * 1-5 echo hello" >> mycron
crontab mycron
rm mycron
