# 30 Days of AWS Serverless Challenge - Day 3

## Taming Data with Amazon DynamoDB

Welcome to Day 3 of our serverless journey! Today, we'll explore Amazon DynamoDB, a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.

### Contents

1. [Theory](#theory)
2. [Practice](#practice)
3. [Mini Project](#mini-project)
4. [Research](#research)
5. [Quiz](#quiz)
6. [Additional Resources](#additional-resources)

### Theory

#### Introduction to NoSQL Databases

- Definition and characteristics of NoSQL databases
- Differences between SQL and NoSQL databases
- Use cases for NoSQL databases

#### DynamoDB Concepts

1. Tables, Items, and Attributes
   - Tables: Similar to tables in relational databases
   - Items: Individual data records (similar to rows)
   - Attributes: Data elements within an item (similar to columns)

2. Primary Keys
   - Partition Key: Distributes data across partitions
   - Sort Key: Optional, allows for efficient querying within a partition

3. Secondary Indexes
   - Global Secondary Index (GSI)
   - Local Secondary Index (LSI)

4. Data Types
   - Scalar Types: String, Number, Binary, Boolean, Null
   - Document Types: List, Map
   - Set Types: String Set, Number Set, Binary Set

5. Read/Write Capacity Modes
   - Provisioned Capacity
   - On-Demand Capacity

6. Consistency Models
   - Eventually Consistent Reads
   - Strongly Consistent Reads

### Practice

1. Creating a DynamoDB Table
   - Use AWS Management Console to create a table
   - Define primary key structure (partition key and optional sort key)
   - Choose capacity mode (provisioned or on-demand)

2. Performing CRUD Operations
   - Using AWS CLI:
     ```bash
     # Put Item
     aws dynamodb put-item --table-name MyTable --item '{"PK": {"S": "123"}, "Data": {"S": "Hello DynamoDB"}}'
     
     # Get Item
     aws dynamodb get-item --table-name MyTable --key '{"PK": {"S": "123"}}'
     
     # Update Item
     aws dynamodb update-item --table-name MyTable --key '{"PK": {"S": "123"}}' --update-expression "SET Data = :newval" --expression-attribute-values '{":newval":{"S":"Updated Data"}}'
     
     # Delete Item
     aws dynamodb delete-item --table-name MyTable --key '{"PK": {"S": "123"}}'
     ```
   
   - Using AWS SDK (Python example):
     ```python
     import boto3

     dynamodb = boto3.resource('dynamodb')
     table = dynamodb.Table('MyTable')

     # Put Item
     table.put_item(Item={'PK': '123', 'Data': 'Hello DynamoDB'})

     # Get Item
     response = table.get_item(Key={'PK': '123'})
     item = response['Item']

     # Update Item
     table.update_item(
         Key={'PK': '123'},
         UpdateExpression="set Data=:d",
         ExpressionAttributeValues={':d': 'Updated Data'}
     )

     # Delete Item
     table.delete_item(Key={'PK': '123'})
     ```

3. Querying and Scanning
   - Practice writing query and scan operations
   - Understand the difference between query and scan

### Mini Project: Serverless Product Catalog

Build a serverless product catalog application using DynamoDB, Lambda, and S3.

#### Components:

1. DynamoDB Table: Store product information
2. S3 Bucket: Store product images
3. Lambda Functions: Handle CRUD operations and search

#### Steps:

1. Create a DynamoDB table with the following structure:
   - Partition Key: ProductID (String)
   - Attributes: Name, Description, Price, Inventory, ImageURL

2. Create an S3 bucket for storing product images

3. Implement Lambda functions for:
   - Adding a product (store data in DynamoDB, upload image to S3)
   - Retrieving product details
   - Updating product inventory
   - Searching for products based on name or description

4. (Optional) Create an API Gateway to expose these functions as RESTful endpoints

#### Sample Lambda Function (Add Product):

```python
import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
table = dynamodb.Table('Products')
bucket_name = 'your-product-images-bucket'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    product_id = str(uuid.uuid4())
    name = body['name']
    description = body['description']
    price = body['price']
    inventory = body['inventory']
    image_data = body['image']  # Base64 encoded image
    
    # Upload image to S3
    image_key = f'products/{product_id}.jpg'
    s3.put_object(Bucket=bucket_name, Key=image_key, Body=image_data.decode('base64'))
    
    # Add product to DynamoDB
    table.put_item(
        Item={
            'ProductID': product_id,
            'Name': name,
            'Description': description,
            'Price': price,
            'Inventory': inventory,
            'ImageURL': f'https://{bucket_name}.s3.amazonaws.com/{image_key}'
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Product added successfully')
    }
    ```
    