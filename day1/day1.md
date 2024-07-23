# Random Quote Lambda Function

This AWS Lambda function retrieves a random quote from the Quotable API and returns it in a formatted message.

## Table of Contents

- [Overview](#overview)
- [Function Details](#function-details)
- [Setup and Deployment](#setup-and-deployment)
- [Usage](#usage)
- [Response Format](#response-format)
- [Error Handling](#error-handling)


## Overview

This Lambda function makes an HTTP request to the Quotable API, fetches a random quote, and returns it along with a "Hello World!" message. It's designed to be triggered by various AWS events or API Gateway requests.

## Function Details

- **Function Name**: `lambda_handler`
- **Runtime**: Python 3.x
- **Trigger**: Configurable (e.g., API Gateway, CloudWatch Events)

### Code

```python
import json
import http.client

def lambda_handler(event, context):
    # Quotable API endpoint
    host = "api.quotable.io"
    conn = http.client.HTTPSConnection(host)
    try:
        # Make the API request
        conn.request("GET", "/random")
        res = conn.getresponse()
        data = res.read()
        # Parse the JSON response
        quote_data = json.loads(data.decode("utf-8"))
        # Extract relevant information
        quote = quote_data['content']
        author = quote_data['author']
        # Construct the response
        message = f"Hello World! Here's a random quote for you:\n\"{quote}\"\n- {author}"
        return {
            'statusCode': 200,
            'body': json.dumps({'message': message})
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to retrieve quote'})
        }
    finally:
        conn.close()

```

## Setup and Deployment

1.Create a new Lambda function in AWS Console.
2.Choose Python 3.x as the runtime.
3.Copy the provided code into the Lambda function.
4.Configure the function's basic settings:

Memory: 128 MB (adjustable)
Timeout: 10 seconds (adjustable)


Set up a trigger for the Lambda function (e.g., API Gateway).
Deploy the function.

## Usage
The function can be invoked through configured AWS triggers. It doesn't require any input parameters.

## Response Format
Success Response

{
    "statusCode": 200,
    "body": {
        "message": "Hello World! Here's a random quote for you:\n\"[Quote content]\"\n- [Author]"
    }
}

Error Response
{
    "statusCode": 500,
    "body": {
        "error": "Failed to retrieve quote"
    }
}

## Error Handling
The function includes error handling to catch exceptions during execution. If an error occurs, it returns a 500 status code with an error message.
Dependencies

json: Built-in Python module for JSON operations.
http.client: Built-in Python module for making HTTP requests.