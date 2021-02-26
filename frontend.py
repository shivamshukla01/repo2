import json
import boto3

def lambda_handler(event, context):
    # TODO implement
   dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
   table = dynamodb.Table('api')
   temp= table.scan()
   res= json.loads(temp['Items'][0]['data'])
   return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
