from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import logging
import boto3

app = FastAPI()

# Define the model for the item with Pydantic model
class Item(BaseModel):
    SKU: str
    DateAdded: datetime
    Name: str
    Quantity: int
    Price: int
    Description: str

# Connection with DynamoDB
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

table_name = 'Inventory'
table = dynamodb.Table(table_name)

@app.get('/')
async def read_root():
    return {"message": "Hello, world!"}

# CRUD operations
# Post method to create an item
@app.post('/items/')
async def create_item(item: Item):
    try:
        # Convert DateAdded to timestamp
        item.DateAdded = int(item.DateAdded.timestamp())

        # Put the item into the DynamoDB table
        table.put_item(Item=item.dict())

        return {'message': 'Item created successfully'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# GET method to retrieve an item by SKU
@app.get('/items/{sku}')
def read_item(sku: str):
    try:
        # Reading an item from the table based on SKU
        response = table.get_item(Key={'SKU': sku})
        if 'Item' not in response:
            # If the item is not found, return 404 error
            raise HTTPException(status_code=404, detail='Item not found')
        return response['Item']
    except Exception as e:
        logger.exception("An error occurred while retrieving item with SKU: %s", sku)
        # If an error occurs, raise a 500 error
        raise HTTPException(status_code=500, detail=str(e))

# PUT method for updating an item by SKU
@app.put('/items/{sku}')
def update_item(sku: str, item: Item):
    try:
        # Convert DateAdded to ISO 8601 string
        date_added_str = item.DateAdded.isoformat()
        # Update the item in the DynamoDB table
        response = table.update_item(
            Key={'SKU': sku},
            UpdateExpression='SET #dateAdded = :da, #name = :n, #quantity = :q, #price = :p, #description = :d',
            ExpressionAttributeNames={
                '#dateAdded': 'DateAdded',
                '#name': 'Name',
                '#quantity': 'Quantity',
                '#price': 'Price',
                '#description': 'Description'
            },
            ExpressionAttributeValues={
                ':da': date_added_str,
                ':n': item.Name,
                ':q': item.Quantity,
                ':p': item.Price,
                ':d': item.Description
            },
            ReturnValues='UPDATED_NEW'
        )
        return response['Attributes']
    except Exception as e:
        logger.exception("An error occurred while updating item with SKU: %s", sku)
        # If an error occurs, raise a 500 error
        raise HTTPException(status_code=500, detail=str(e))