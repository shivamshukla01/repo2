import urllib3
import json
import boto3

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    #result dict object
    res={
      "exchangeUID": 1,
      "exchangeName": "WazirX",
      "updateTimestamp": 0,
      "coins":[
      ]
    }
    # coinlist array, sequentially add all required coins to this
    coinlist=[]
    #=============================
    #coinuid=1 BTC
    # update btc values and update timestamp;

    response= http.request('GET', 'https://api.wazirx.com/api/v2/tickers/btcinr')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)

    #update time of updateTimestamp ( only once in whole routine)
    res["updateTimestamp"]=coindata["at"]

    coin = {
          "coinUID": 1,
          "coinName": "BTC",
          "coinbuyprice": float(coindata["ticker"]["buy"]),
          "coinsellprice": float(coindata["ticker"]["sell"])
    }

    coinlist.append(coin)
    #====================================

    #coinuid=2 ETH
    # update eth values and update timestamp;

    response= http.request('GET', 'https://api.wazirx.com/api/v2/tickers/ethinr')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)

    coin = {
          "coinUID": 2,
          "coinName": "ETH",
          "coinbuyprice": float(coindata["ticker"]["buy"]),
          "coinsellprice": float(coindata["ticker"]["sell"])
    }

    coinlist.append(coin)
    #====================================

    #coinuid=3 LTC
    # update eth values and update timestamp;

    response= http.request('GET', 'https://api.wazirx.com/api/v2/tickers/ltcinr')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)

    coin = {
          "coinUID": 3,
          "coinName": "LTC",
          "coinbuyprice": float(coindata["ticker"]["buy"]),
          "coinsellprice": float(coindata["ticker"]["sell"])
    }

    coinlist.append(coin)
    #====================================

    #coinuid=4 DOGE
    # update eth values and update timestamp;

    response= http.request('GET', 'https://api.wazirx.com/api/v2/tickers/dogeinr')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)

    coin = {
          "coinUID": 4,
          "coinName": "DOGE",
          "coinbuyprice": float(coindata["ticker"]["buy"]),
          "coinsellprice": float(coindata["ticker"]["sell"])
    }

    coinlist.append(coin)
    #====================================

    #coinuid=5 TRX
    # update eth values and update timestamp;

    response= http.request('GET', 'https://api.wazirx.com/api/v2/tickers/trxinr')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)

    coin = {
          "coinUID": 5,
          "coinName": "TRX",
          "coinbuyprice": float(coindata["ticker"]["buy"]),
          "coinsellprice": float(coindata["ticker"]["sell"])
    }

    coinlist.append(coin)
    #====================================

    #coinuid=6 ADA
    # update eth values and update timestamp;

    response= http.request('GET', 'https://api.wazirx.com/api/v2/tickers/adainr')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)

    coin = {
          "coinUID": 6,
          "coinName": "ADA",
          "coinbuyprice": float(coindata["ticker"]["buy"]),
          "coinsellprice": float(coindata["ticker"]["sell"])
    }

    coinlist.append(coin)
    #====================================
    # complete result object
    res["coins"]= coinlist
    s = json.dumps(res)

    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('coin')

    response = table.put_item(
           Item={
                'exchnum': 1,
                'data': s
            }
        )

    return {
        'statusCode': 200
    }
