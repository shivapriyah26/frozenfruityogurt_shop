import os

def lambda_handler(event, context):
    try:
        # Path to your static HTML file
        file_path = os.path.join(os.path.dirname(__file__), 'index.html')

        # Read HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Return HTML response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html'
            },
            'body': html_content
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error loading website: {str(e)}'
        }
