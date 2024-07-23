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