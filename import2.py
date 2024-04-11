import mysql.connector
import pandas as pd

# MySQL connection parameters
host = 'localhost'
user = 'root'
password = 'Sika@1234'
database = 'assignment5_datapipeline_mk2'

# CSV files and corresponding table names
csv_files = {
    'customer2_data': 'up_mk2_cus.csv',
    'deliveries2_data': 'up_mk2_del.csv',
    'orders2_data': 'update_mk2_orders.csv',

}


# Function to import CSV data into MySQL table


def import_csv_to_mysql(csv_file, table_name, conn):
    df = pd.read_csv(csv_file)

    # Generate CREATE TABLE SQL statement
    columns = ', '.join([f'{col} VARCHAR(255)' for col in df.columns])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"

    # Create table in MySQL
    cursor = conn.cursor()
    cursor.execute(create_table_sql)

    # Insert DataFrame records into MySQL table
    for _, row in df.iterrows():
        values = tuple(row)
        cursor.execute(
            f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})", values)
    conn.commit()
    cursor.close()


# Connect to MySQL
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Example usage
for table_name, csv_file in csv_files.items():
    import_csv_to_mysql(csv_file, table_name, conn)

# Close MySQL connection
conn.close()
