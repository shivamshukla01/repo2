import urllib3
import json
import boto3
import time
import math

def buyucoin():
    http = urllib3.PoolManager()
    res={
      "exchangeUID": 5,
      "exchangeName": "BuyUcoin",
      "updateTimestamp": 0,
      "coins":[
      ]
    }
    # coinlist array, sequentially add all required coins to this
    coinlist=[]
    response= http.request('GET', 'https://api.buyucoin.com/ticker/v1.0/liveData')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)
    times= math.floor(time.time())
    #update time of updateTimestamp ( only once in whole routine)
    res["updateTimestamp"]=times
    #======coin 1 BTC===
    coin = {
          "coinUID": 1,
          "coinName": "BTC",
          "coinbuyprice": float(coindata['data'][1]['ask']),
          "coinsellprice": float(coindata['data'][1]['bid'])
    }
    coinlist.append(coin)
    #=====================
    #======coin 2 ETH===
    coin = {
          "coinUID": 2,
          "coinName": "ETH",
          "coinbuyprice": float(coindata['data'][3]['ask']),
          "coinsellprice": float(coindata['data'][3]['bid'])
    }
    coinlist.append(coin)

    #======coin 3 LTC===
    coin = {
          "coinUID": 3,
          "coinName": "LTC",
          "coinbuyprice": float(coindata['data'][9]['ask']),
          "coinsellprice": float(coindata['data'][9]['bid'])
    }
    coinlist.append(coin)

    #======coin 5 TRX===
    coin = {
          "coinUID": 5,
          "coinName": "TRX",
          "coinbuyprice": float(coindata['data'][27]['ask']),
          "coinsellprice": float(coindata['data'][27]['bid'])
    }
    coinlist.append(coin)
    #===================
    res["coins"]= coinlist
    s = json.dumps(res)

    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('coin')

    response = table.put_item(
           Item={
                'exchnum': 5,
                'data': s
            }
        )

    return {
        'statusCode': 200
    }
