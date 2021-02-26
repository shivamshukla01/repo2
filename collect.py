import json
import boto3
import time
import sys
import math

def collect():
    res= [
     {
      "coinUID": 1,
      "coinName": "BTC",
      "imageURL": "http://url",
      "exchanges": []
      },
      {
      "coinUID": 2,
      "coinName": "ETH",
      "imageURL": "http://url",
      "exchanges": []
      },
      {
      "coinUID": 3,
      "coinName": "LTC",
      "imageURL": "http://url",
      "exchanges": []
      },
      {
      "coinUID": 4,
      "coinName": "DOGE",
      "imageURL": "http://url",
      "exchanges": []
      },
      {
      "coinUID": 5,
      "coinName": "TRX",
      "imageURL": "http://url",
      "exchanges": []
      },
      {
      "coinUID": 6,
      "coinName": "ADA",
      "imageURL": "http://url",
      "exchanges": []
      }]

    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('coin')
    temp= table.scan()

    for i in temp['Items']:
          r = json.loads(i['data'])
          obj= {
          "exchangeUID": 0,
          "updateTimestamp": 0,
          "exchangeName": "none",
          "coinbuyprice": 0.0,
          "coinsellprice": 0.0,
          "isBest": False
          }
          obj["exchangeUID"]=r["exchangeUID"]
          obj["updateTimestamp"]=r["updateTimestamp"]
          obj["exchangeName"]=r["exchangeName"]
          for item in r["coins"]:
              index= item['coinUID']-1
              obj["coinbuyprice"]=item["coinbuyprice"]
              obj["coinsellprice"]=item["coinsellprice"]
              res[index]["exchanges"].append(obj.copy())

    for i in res:
        best= {
        "exchangeUID": 0,
        "updateTimestamp": 0,
        "exchangeName": "Best Prices",
        "coinbuyprice": 0,
        "coinsellprice": 0,
        "coinBuyFrom": "",
        "coinSellTo": "",
        "isBest": True
        }
        times = math.floor(time.time())
        #update time of updateTimestamp ( only once in whole routine
        best["updateTimestamp"]=times
        sellhigh=0
        buyfrom=""
        sellto=""
        buylow= 9999999999999
        for j in i["exchanges"]:
            if (j['coinsellprice']>sellhigh):
                sellhigh=j['coinsellprice']
                sellto=j['exchangeName']
            if (j['coinbuyprice']<buylow):
                buylow=j['coinbuyprice']
                buyfrom=j['exchangeName']
        best["coinbuyprice"]=buylow
        best["coinsellprice"]=sellhigh
        best["coinBuyFrom"]=buyfrom
        best["coinSellTo"]=sellto
        i["exchanges"].insert(0,best)

    s = json.dumps(res)

    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('api')

    response = table.put_item(
           Item={
                'list': 1,
                'data': s
            }
        )

    return {
        'statusCode': 200
        }
