import requests
import csv
import os

# Function to send a message and get a response
def get_response(endpoint_url, bearer_token, session_id, message):
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "session_id": session_id,
        "Content-Type": "application/json"
    }
    try:
        # Send the request
        response = requests.post(endpoint_url, json={"message": message}, headers=headers)
        response.raise_for_status()  # Raise exception for 4xx/5xx errors
        response_json = response.json()
        return response_json.get("message", "No 'message' field in response")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Function to process and update the CSV file
def process_csv(csv_file_path, endpoint_url, bearer_token, session_id):
    try:
        # Read the existing CSV
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = list(csv.reader(infile))  # Load rows into memory
            header = reader[0]

            # Ensure "Response" column exists
            if "Response" not in header:
                header.append("Response")
                response_index = len(header) - 1
            else:
                response_index = header.index("Response")

            # Process each row
            for i in range(1, len(reader)):
                row = reader[i]
                if len(row) > 1:  # Valid rows
                    if len(row) <= response_index or not row[response_index].strip():  
                        message = row[1]  
                        print(f"Processing: {message}")
                        response = get_response(endpoint_url, bearer_token, session_id, message)
                        print(f"Response: {response}")
                        row.extend([""] * (response_index - len(row) + 1))  
                        row[response_index] = response
                else:
                    print(f"Skipping invalid row: {row}")

        # Write the updated CSV back
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(reader)
            print("CSV file updated successfully.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
