
# Reference

## Token bucket

https://en.wikipedia.org/wiki/Token_bucket

```
トークンバケットはデータ転送レートの平均に制限を課して、ある程度のバースト性を許容する。
```

## AWS

https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-request-throttling.html

```
リージョンごとのアカウントレベルのスロットリング
API Gateway はデフォルトで、リージョンごとに AWS アカウント内のすべての API 全体で定常状態のリクエスト/秒 (rps) を制限します。また、リージョンごとに AWS アカウント内のすべての API にわたってバースト (最大バケットサイズ) を制限します。API Gateway では、バースト制限は、API Gateway が 429 Too Many Requests エラーレスポンスを返すことなく、どの時点でも処理できる同時リクエスト送信の最大数に対応します。スロットリングクォータの詳細については、「Amazon API Gateway のクォータと重要な注意点」を参照してください。

これらのスロットリング制限を理解するために、リージョンのバースト制限が 5,000 で、アカウントレベルのレート制限が 10,000 リクエスト/秒の場合の例をいくつか以下に示します。

発信者が、1 秒間に等しく 10,000 リクエストを送信した場合 (たとえば、ミリ秒毎に 10 リクエスト)、API Gateway は 1 つも削除することなくすべてのリクエストを処理します。

発信者が、最初の 1 ミリ秒間で 10,000 リクエストを送信した場合、API Gateway はそのうち 5,000 に対応し、残りは 1 秒間中に調整します。

発信者が 5,000 リクエストを最初の 1 ミリ秒に送信し、さらに 5,000 リクエストを残りの 999 ミリ秒に等しく広げた場合 (たとえば、ミリ秒毎 5 リクエスト)、API Gateway は 429 Too Many Requests エラーレスポンスを返すことなく全 10,000 リクエストを 1 秒間中に処理します。

発信者が 5,000 リクエストを最初の 1 ミリ秒に送信し、次の 5,000 リクエスト を送信するのに 101 ミリ秒目まで待った場合、API Gateway は 6,000 リクエストを処理し、残りを 1 秒間中に調整します。これは、10,000 rps のレートで、API Gateway は最初の 100 ミリ秒後に 1,000 リクエストに対応し、よって同じ量でバケットを空にしたためです。次の 5,000 リクエストのスパイクのうち、1,000 はバケットを埋め、処理待ちとしてキューされます。残りの 4,000 は最大バケット容量を超え、破棄されます。

発信者が 5,000 リクエストを最初の 1 ミリ秒に送信し、101 秒目で 1,000 リクエストを送信して、さらに 4,000 リクエストを残りの 899 ミリ秒に等しく広げると、API Gateway はスロットリングなしで全 10,000 リクエストを 1 秒間中に処理します。

より一般的に、特定の時点で、バケット内のトークン数が b で、バケットの最大容量が B である場合、バケットに追加できるトークンの最大数は Δ=B-b です。この追加トークンの最大数は、クライアントが 429 エラーレスポンスを受け取ることなく送信できる追加の同時リクエストの最大数に対応します。通常、Δ は時間と共に変動します。その値は、バケットが一杯 (b=B) である場合のゼロから、バケットが空 (B) である場合の b=0 までの範囲にわたります。この範囲は、リクエスト処理率 (トークンがバケットから削除されるレート) と、レート制限率 (トークンがバケットに追加されるレート) に依存します。

次の図は、同時リクエストの最大追加数である Δ の一般的な動作を、時間の関数として示します。図は、空のバケットから始まり、バケット内のトークンは 2 つの率を統合した r で減るものとしまていす。
```