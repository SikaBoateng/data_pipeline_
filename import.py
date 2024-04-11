# my personal work data pipeline

import pandas as pd
import mysql.connector

# MySQL connection parameters
host = 'localhost'
user = 'root'
password = 'Sika@1234'
database = 'assignment5_datapipeline_mk1'

# Connect to MySQL
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Function to import CSV data into MySQL table


def import_csv_to_mysql(csv_file, table_name):
    # Read CSV file into pandas DataFrame
    df = pd.read_csv(csv_file)

    # Insert DataFrame records into MySQL table
    cursor = conn.cursor()
    for _, row in df.iterrows():
        values = tuple(row)
        cursor.execute(
            f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})", values)
    conn.commit()
    cursor.close()


# Example usage
if __name__ == "__main__":
    csv_files = {
        'customer1_data': 'up_mk1_cus.csv',
        'deliveries1_data': 'up_mk1_del.csv',
        'orders1_data': 'update_mk1_orders.csv',

    }

    for table_name, csv_file in csv_files.items():
        import_csv_to_mysql(csv_file, table_name)

# Close MySQL connection
conn.close()
