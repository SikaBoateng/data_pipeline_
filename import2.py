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
    'deliveries2_data': 'update_mk2_del.csv',
    'orders2_data': 'update_mk2_orders.csv',

}


# Function to import CSV data into MySQL table


# Function to import CSV data into MySQL table
def import_csv_to_mysql(csv_file, table_name, conn):
    df = pd.read_csv(csv_file)

    # Generate CREATE TABLE SQL statement
    columns = ', '.join([f'`{col}` VARCHAR(255)' for col in df.columns])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    print("SQL query:", create_table_sql)  # Print SQL query

    # Create table in MySQL
    cursor = conn.cursor()
    try:
        cursor.execute(create_table_sql)
    except mysql.connector.Error as err:
        print("Error creating table:", err.msg)  # Print error message
        return

    # Insert DataFrame records into MySQL table
    for _, row in df.iterrows():
        values = tuple(row)
        try:
            cursor.execute(
                f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})", values)
        except mysql.connector.Error as err:
            print("Error inserting data:", err.msg)  # Print error message
            continue
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
