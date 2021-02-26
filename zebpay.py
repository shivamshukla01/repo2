import urllib3
import json
import boto3
import time
import math

def zebpay():
#http client initialisation
    http = urllib3.PoolManager()
#result dict object
    res={
      "exchangeUID": 2,
      "exchangeName": "ZebPay",
      "updateTimestamp": 0,
      "coins":[
      ]
    }
    # coinlist array, sequentially add all required coins to this
    coinlist=[]
    time= math.floor(time.time())
    #update time of updateTimestamp ( only once in whole routine)
    res["updateTimestamp"]=time
    #get database
    response= http.request('GET', 'https://www.zebapi.com/pro/v1/market/')
    coindata = response.data.decode("utf-8")
    coindata = json.loads(coindata)
    #=============================
    #coinuid=1 BTC
    # update btc values and update timestamp;
    coin = {
          "coinUID": 1,
          "coinName": "BTC",
          "coinbuyprice": float(coindata[20]["buy"]),
          "coinsellprice": float(coindata[20]["sell"])
    }
    coinlist.append(coin)
    #=================================
    #coinuid=2 ETH
    # update eth values and update timestamp;
    coin = {
          "coinUID": 2,
          "coinName": "ETH",
          "coinbuyprice": float(coindata[27]["buy"]),
          "coinsellprice": float(coindata[27]["sell"])
    }
    coinlist.append(coin)
    #=================================
    #coinuid=3 LTC
    # update ltc values and update timestamp;

    coin = {
          "coinUID": 3,
          "coinName": "LTC",
          "coinbuyprice": float(coindata[32]["buy"]),
          "coinsellprice": float(coindata[32]["sell"])
    }

    coinlist.append(coin)

    #=================================
    #coinuid=5 TRX
    # update ltc values and update timestamp;

    coin = {
          "coinUID": 5,
          "coinName": "TRX",
          "coinbuyprice": float(coindata[37]["buy"]),
          "coinsellprice": float(coindata[37]["sell"])
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
                'exchnum': 2,
                'data': s
            }
        )
    return {
         'statusCode': 200,
     }
