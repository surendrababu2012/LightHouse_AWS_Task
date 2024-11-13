import json
import boto3,os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb')
table_name = os.getenv("TABLE_NAME") 
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    task_id = event['pathParameters']['taskId']
    
    response = table.get_item(Key={'taskId': task_id})
    if not response:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Task not found', 'response': response})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps({"message": response})
    }
