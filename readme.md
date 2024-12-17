Here’s a clean and detailed **README.md** file for your project:
# Chat Bot Tester

## Description
This project is a **Chat Bot Tester** designed to process customer support messages from a CSV file, send them to a specified API endpoint, and record responses back into the same CSV file.

The project is structured into two main components:
1. **client.py**: Handles API communication and CSV processing.
2. **main.py**: Entry point that loads configurations and invokes the processing functions.

Environment variables are used for secure configuration management.

## Features
- Reads messages from a CSV file.
- Sends each message to an API endpoint.
- Writes the API responses back into the CSV file under the "Response" column.
- Skips rows that already contain responses, ensuring efficient re-processing.
- Supports secure configuration via an `.env` file.


## File Structure

```
project/
│
├── client.py         # Contains API and CSV processing logic
├── main.py           # Entry point to run the script
├── .env              # Environment variables file
└── README.md         # Project documentation
```

## Requirements

- **Python 3.8+**
- **Dependencies**:
   - `requests`
   - `python-dotenv`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Alperemrehas/Chat_Bot_Tester.git
   cd chat-bot-tester
   ```

2. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root directory and add the following:

   ```env
   ENDPOINT_URL=http://.....
   BEARER_TOKEN=your_bearer_token_here
   SESSION_ID=your_session_id_here
   CSV_FILE_PATH=/data/csa_messages.csv
   ```

   Replace `your_bearer_token_here` and `your_session_id_here` with your actual credentials.

5. **Prepare CSV File**:
   Ensure the CSV file exists at the path specified in `CSV_FILE_PATH`. Example:

   ```csv
   Line_Number,Message,Response
   1,Hi, I need support for my account,
   2,Can you find part number 30008?,
   ```

## Usage

1. Run the script using:
   ```bash
   python main.py
   ```

2. **Processing**:
   - The script processes the "Message" column in the CSV file.
   - API responses are added under the "Response" column.
   - If the "Response" column already has a value, the row is skipped.

3. **Output**:
   The CSV file will be updated with the responses. Example:

   ```csv
   Line_Number,Message,Response
   1,Hi, I need support for my account,Account support details sent.
   2,Can you find part number 30008?,Part 30008 details provided.
   ```

## Troubleshooting

1. **Missing Environment Variables**:
   - Ensure `.env` file is correctly placed in the root directory.
   - Run `python main.py` and verify output.

2. **CSV File Path**:
   - Ensure the path specified in `CSV_FILE_PATH` exists and is accessible.

3. **API Connection Issues**:
   - Verify the API endpoint is running and accessible.

4. **Dependencies**:
   - If dependencies are missing, reinstall:
     ```bash
     pip install -r requirements.txt
     ```

## License

This project is licensed under the MIT License.

