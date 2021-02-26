import urllib3
import json
import boto3
import time
import math

def coindcx():
    http = urllib3.PoolManager()
    res={
      "exchangeUID": 3,
      "exchangeName": "CoinDCX",
      "updateTimestamp": 0,
      "coins":[
      ]
    }
    # coinlist array, sequentially add all required coins to this
    coinlist=[]
    response= http.request('GET', 'https://api.coindcx.com/exchange/ticker')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)
    res["updateTimestamp"]=coindata[0]['timestamp']

    #======coin 1 BTC===
    coin = {
          "coinUID": 1,
          "coinName": "BTC",
          "coinbuyprice": float(coindata[0]["bid"]),
          "coinsellprice": float(coindata[0]["ask"])
    }
    coinlist.append(coin)
    #=====================

    #======coin 2 ETH===
    coin = {
          "coinUID": 2,
          "coinName": "ETH",
          "coinbuyprice": float(coindata[15]["bid"]),
          "coinsellprice": float(coindata[15]["ask"])
    }
    coinlist.append(coin)
    #=====================

    #======coin 3 LTC===
    coin = {
          "coinUID": 3,
          "coinName": "LTC",
          "coinbuyprice": float(coindata[67]["bid"]),
          "coinsellprice": float(coindata[67]["ask"])
    }
    coinlist.append(coin)
    #=====================
    #======coin 4 DOGE===
    coin = {
          "coinUID": 4,
          "coinName": "DOGE",
          "coinbuyprice": float(coindata[3]["bid"]),
          "coinsellprice": float(coindata[3]["ask"])
    }
    coinlist.append(coin)
    #=====================
    #======coin 5 TRON===
    coin = {
          "coinUID": 5,
          "coinName": "TRON",
          "coinbuyprice": float(coindata[618]["bid"]),
          "coinsellprice": float(coindata[618]["ask"])
    }
    coinlist.append(coin)
    #=====================
    #======coin 6 ADA===
    coin = {
          "coinUID": 6,
          "coinName": "ADA",
          "coinbuyprice": float(coindata[633]["bid"]),
          "coinsellprice": float(coindata[633]["ask"])
    }
    coinlist.append(coin)
    #=====================
    res["coins"]= coinlist
    s = json.dumps(res)

    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('coin')

    response = table.put_item(
           Item={
                'exchnum': 3,
                'data': s
            }
        )

    return {
        'statusCode': 200
    }
