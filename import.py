import pandas as pd
import mysql.connector
import os
from datetime import datetime
import time

# MySQL connection parameters
host = 'localhost'
user = 'root'
password = 'Sika@1234'
database = 'assignment5_datapipeline_mk1'

# Function to connect to MySQL


def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Function to import CSV data into MySQL table


def import_csv_to_mysql(conn, csv_file, table_name):
    try:
        # Read CSV file into pandas DataFrame
        df = pd.read_csv(csv_file)

        # Check if table has been processed before
        last_processed_timestamp = get_last_processed_timestamp(table_name)

        # Filter DataFrame for new or modified records since the last execution
        if last_processed_timestamp is not None:
            df = df[df['Created At'] > last_processed_timestamp]

        # Insert DataFrame records into MySQL table
        cursor = conn.cursor()
        for _, row in df.iterrows():
            values = tuple(row)
            cursor.execute(
                f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})", values)
        conn.commit()
        cursor.close()

        # Update last processed timestamp
        update_last_processed_timestamp(table_name, datetime.now())
        print(f"Data imported into {table_name} successfully.")
        return True
    except Exception as e:
        print(f"Error importing data into {table_name}: {e}")
        return False

# Function to get the last processed timestamp for a table


def get_last_processed_timestamp(table_name):
    # Check if the last processed timestamp file exists
    timestamp_file = f"{table_name}_last_processed_timestamp.txt"
    if os.path.exists(timestamp_file):
        with open(timestamp_file, 'r') as file:
            last_timestamp = file.readline().strip()
        return last_timestamp
    else:
        return None

# Function to update the last processed timestamp for a table


def update_last_processed_timestamp(table_name, timestamp):
    # Update the last processed timestamp file
    timestamp_file = f"{table_name}_last_processed_timestamp.txt"
    with open(timestamp_file, 'w') as file:
        file.write(timestamp.strftime('%Y-%m-%d %H:%M:%S'))


# Example usage
if __name__ == "__main__":
    # Attempt to connect to MySQL
    conn = connect_to_mysql()
    if conn:
        csv_files = {
            'customer1_data': 'up_mk1_cus.csv',
            'deliveries1_data': 'update_mk1_del.csv',
            'orders1_data': 'update_mk1_orders.csv',
        }

        for table_name, csv_file in csv_files.items():
            retry_count = 0
            while retry_count < 3:
                if import_csv_to_mysql(conn, csv_file, table_name):
                    break
                else:
                    retry_count += 1
                    print(f"Retrying import for {table_name}...")
                    time.sleep(5)  # Wait for 5 seconds before retrying

        # Close MySQL connection
        conn.close()
