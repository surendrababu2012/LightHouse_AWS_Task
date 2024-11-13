import json
import os
import uuid
import boto3
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb')
table_name = os.getenv("TABLE_NAME") 
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    data = json.loads(event['body'])
    task_id = str(uuid.uuid4())
    
    item = {
        'taskId': task_id,
        'title': data.get('title'),
        'description': data.get('description'),
        'status': data.get('status', 'pending')
    }
    
    table.put_item(Item=item)
    
    return {
        'statusCode': 201,
        'body': json.dumps(item)
    }
