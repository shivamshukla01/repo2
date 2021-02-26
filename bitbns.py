import urllib3
import json
import boto3
import time
import math

def bitbns():
    http = urllib3.PoolManager()
    res={
      "exchangeUID": 4,
      "exchangeName": "BitBNS",
      "updateTimestamp": 0,
      "coins":[
      ]
    }
    # coinlist array, sequentially add all required coins to this
    coinlist=[]
    response= http.request('GET', 'https://bitbns.com/order/getTickerWithVolume/')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)
    times= math.floor(time.time())
    #update time of updateTimestamp ( only once in whole routine)
    res["updateTimestamp"]=times
    #======coin 1 BTC===
    coin = {
          "coinUID": 1,
          "coinName": "BTC",
          "coinbuyprice": coindata['BTC']['highest_buy_bid'],
          "coinsellprice": coindata['BTC']['lowest_sell_bid']
    }
    coinlist.append(coin)
    #=====================

    #======coin 2 ETH===
    coin = {
          "coinUID": 2,
          "coinName": "ETH",
          "coinbuyprice": coindata['ETH']['highest_buy_bid'],
          "coinsellprice": coindata['ETH']['lowest_sell_bid']
    }
    coinlist.append(coin)
    #=====================
    #======coin 3 LTC===
    coin = {
          "coinUID": 3,
          "coinName": "LTC",
          "coinbuyprice": coindata['LTC']['highest_buy_bid'],
          "coinsellprice": coindata['LTC']['lowest_sell_bid']
    }
    coinlist.append(coin)
    #=====================
    #======coin 4 DOGE ===
    coin = {
          "coinUID": 4,
          "coinName": "DOGE",
          "coinbuyprice": coindata['DOGE']['highest_buy_bid'],
          "coinsellprice": coindata['DOGE']['lowest_sell_bid']
    }
    coinlist.append(coin)
    #=====================
    #======coin 5 TRX===
    coin = {
          "coinUID": 5,
          "coinName": "TRX",
          "coinbuyprice": coindata['TRX']['highest_buy_bid'],
          "coinsellprice": coindata['TRX']['lowest_sell_bid']
    }
    coinlist.append(coin)
    #=====================
    #======coin 6 ADA===
    coin = {
          "coinUID": 1,
          "coinName": "ADA",
          "coinbuyprice": coindata['ADA']['highest_buy_bid'],
          "coinsellprice": coindata['ADA']['lowest_sell_bid']
    }
    coinlist.append(coin)
    #=====================
    res["coins"]= coinlist
    s = json.dumps(res)

    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('coin')

    response = table.put_item(
           Item={
                'exchnum': 4,
                'data': s
            }
        )

    return {
        'statusCode': 200
    }
