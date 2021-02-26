import boto3

def createtables():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.create_table(
        TableName='coin',
        KeySchema=[
            {
                'AttributeName': 'exchnum',
                'KeyType': 'HASH'  #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'exchnum',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'data',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    #api table
    table = dynamodb.create_table(
        TableName='api',
        KeySchema=[
            {
                'AttributeName': 'list',
                'KeyType': 'HASH'  #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'list',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'data',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return {
        'statusCode': 200
    }
