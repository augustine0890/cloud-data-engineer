import os

import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database connection details from environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT", "5432")  # Default to 5432 if not set

try:
    # Establish the connection
    connection = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
    )
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a test query
    cursor.execute("SELECT version();")

    # Fetch and print the result
    version = cursor.fetchone()
    print(f"Connected to PostgreSQL version: {version}")

    # Execute a query to list tables
    cursor.execute(
        """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """
    )

    # Fetch all table names
    tables = cursor.fetchall()

    # Print the list of tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Close the cursor and connection
    cursor.close()
    connection.close()
except Exception as e:
    print(f"An error occurred: {e}")
