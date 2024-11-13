import json
import boto3,os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb')
table_name = os.getenv("TABLE_NAME") 
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    task_id = event['pathParameters']['taskId']
    data = json.loads(event['body'])

    response = table.update_item(
        Key={'taskId': task_id},
        UpdateExpression="set title=:t, description=:d, status=:s",
        ExpressionAttributeValues={ 
            ':t': data['title'],
            ':d': data['description'],
            ':s': data['status']
        },
        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response['Attributes'])
    }
