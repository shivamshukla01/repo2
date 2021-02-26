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
    response= http.request('GET', 'https://api.wazirx.com/api/v2/tickers/btcinr')
