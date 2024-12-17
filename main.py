import os
from client import process_csv
from dotenv import load_dotenv

load_dotenv()

# Path to the CSV file
csv_file_path = "data/test_messages.csv"

# Retrieve environment variables
endpoint_url = os.getenv('ENDPOINT_URL')
bearer_token = os.getenv('BEARER_TOKEN')
session_id = os.getenv('SESSION_ID')

if not all([endpoint_url, bearer_token, session_id]):
    raise EnvironmentError("Missing required environment variables.")

# Call the CSV processor
process_csv(csv_file_path, endpoint_url, bearer_token, session_id)
