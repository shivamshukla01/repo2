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
    for i in coindata:
        if(i["market"]=="BTCINR"):
            print("BTCINR found")
    #======coin 1 BTC===
            coin = {
                "coinUID": 1,
                "coinName": "BTC",
                "coinbuyprice": float(i["ask"]),
                "coinsellprice": float(i["bid"])
                }
            coinlist.append(coin)
    #=====================
        elif(i["market"]=="ETHINR"):
            print("ETHINR found")
    #======coin 2 ETH===
            coin = {
                "coinUID": 2,
                "coinName": "ETH",
                "coinbuyprice": float(i["ask"]),
                "coinsellprice": float(i["bid"])
                }
            coinlist.append(coin)
    #=====================
        elif(i["market"]=="LTCINR"):
            print("LTCINR found")
    #======coin 1 BTC===
            coin = {
                "coinUID": 3,
                "coinName": "LTC",
                "coinbuyprice": float(i["ask"]),
                "coinsellprice": float(i["bid"])
                }
            coinlist.append(coin)
    #=====================
        elif(i["market"]=="DOGEINR"):
    #======coin 1 BTC===
            coin = {
                "coinUID": 4,
                "coinName": "DOGE",
                "coinbuyprice": float(i["ask"]),
                "coinsellprice": float(i["bid"])
                }
            coinlist.append(coin)
    #=====================
        elif(i["market"]=="TRXINR"):
    #======coin 1 BTC===
            coin = {
                "coinUID": 5,
                "coinName": "TRX",
                "coinbuyprice": float(i["ask"]),
                "coinsellprice": float(i["bid"])
                }
            coinlist.append(coin)
    #=====================
        elif(i["market"]=="ADAINR"):
    #======coin 1 BTC===
            coin = {
                "coinUID": 6,
                "coinName": "ADA",
                "coinbuyprice": float(i["ask"]),
                "coinsellprice": float(i["bid"])
                }
            coinlist.append(coin)
    #=====================
        else:
            pass
    #=====================
    res["coins"]= coinlist
    print(res)
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
