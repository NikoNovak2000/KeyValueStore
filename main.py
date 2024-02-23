from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
import boto3

app = FastAPI()

# Definiranje modela podataka pomoću Pydantic
class Item(BaseModel):
    SKU: str
    DateAdded: datetime
    Name: str
    Quantity: int
    Price: int
    Description: str

# Postavljanje AWS pristupnih ključeva i regiona
aws_access_key_id = ""
aws_secret_access_key = ""
region_name = "eu-north-1"

# Stvaranje povezivanja s DynamoDB-om
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

table_name = 'Inventory'
table = dynamodb.Table(table_name)

@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}

# CRUD operacije

# Create (Stvaranje)
@app.post("/items/")
async def create_item(item: Item):
    try:
        # Convert DateAdded to timestamp
        item.DateAdded = int(item.DateAdded.timestamp())

        # Put the item into the DynamoDB table
        table.put_item(Item=item.dict())

        return {"message": "Item created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Read (Čitanje)
@app.get("/items/{sku}")
def read_item(sku: str):
    try:
        # Reading an item from the table based on SKU
        response = table.get_item(Key={'SKU': sku})
        if 'Item' not in response:
            # If the item is not found, return a 404 error
            raise HTTPException(status_code=404, detail="Item not found")
        return response['Item']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))