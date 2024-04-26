from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import logging
import boto3
import uuid

app = FastAPI()

# Connecting with DynamoDB
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

table_name = 'Inventory'
table = dynamodb.Table(table_name)

# Defined model for items with Pydantic model
class Item(BaseModel):
    Name: str
    Quantity: int
    Price: int
    Description: str

# Error logging set up
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def read_root():
    return {"message": "Server is on!"}

# CRUD operations
# Post method to create an item
@app.post('/items/')
async def create_item(item: Item):
    try:
        # Generate a unique SKU
        sku = str(uuid.uuid4())

        # Set DateAdded to current date and time
        date_added = datetime.now()

        # Put item in db
        table.put_item(
            Item={
                'SKU': sku,
                'DateAdded': date_added.strftime("%d/%m/%Y"),
                'Name': item.Name,
                'Quantity': item.Quantity,
                'Price': item.Price,
                'Description': item.Description
            }
        )
        return {'message': 'Item created successfully', 'SKU': sku}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET method to retrieve an item by SKU
@app.get('/items/{sku}')
async def read_item(sku: str):
    try:
        # Read item from db based on SKU
        response = table.get_item(Key={'SKU': sku})
        if 'Item' not in response:
            # If the item is not found, return 404 error
            raise HTTPException(status_code=404, detail='Item not found')

        # Extract item data from the response
        item_data = response['Item']

        # Reordering the attributes
        reordered_item = {
            'SKU': item_data['SKU'],
            'DateAdded': item_data['DateAdded'],
            'Name': item_data['Name'],
            'Quantity': item_data['Quantity'],
            'Price': item_data['Price'],
            'Description': item_data['Description']
        }

        return reordered_item
    except Exception as e:
        logger.exception("An error occurred while retrieving item with SKU: %s", sku)
        raise HTTPException(status_code=500, detail=str(e))

# PUT method for updating an item by SKU
@app.put('/items/upd/{sku}')
async def update_item(sku: str, item: Item):
    try:
        # Update the item in db
        response = table.update_item(
            Key={'SKU': sku},
            UpdateExpression='SET #name = :n, #quantity = :q, #price = :p, #description = :d',
            ExpressionAttributeNames={
                '#name': 'Name',
                '#quantity': 'Quantity',
                '#price': 'Price',
                '#description': 'Description'
            },
            ExpressionAttributeValues={
                ':n': item.Name,
                ':q': item.Quantity,
                ':p': item.Price,
                ':d': item.Description
            },
            ReturnValues='UPDATED_NEW'
        )
        return response['Attributes']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# DELETE method
@app.delete('/items/del/{sku}')
async def delete_item(sku: str):
    try:
        # Deleting the item from db based on SKU
        response = table.delete_item(Key={'SKU': sku})
        if 'ResponseMetadata' in response and response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {'message': f'Item with SKU {sku} deleted successfully'}
        else:
            raise HTTPException(status_code=404, detail='Item not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))