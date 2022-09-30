import json
from datetime import datetime
def lambda_handler(event, context):
    # TODO implement
    getTimeStamp=datetime.now().isoformat(timespec='seconds')
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps({"messages":
            [{
                "type": "unstructured",
                "unstructured": {
                "text": "Application under development. Search functionality will be implemented in Assignment 2",
                "timestamp": getTimeStamp
            }
            }]
            
        })
    }
