import csv
import mysql.connector

# MySQL database connection parameters
db_config = {
  'host': 'localhost',
  'user': 'root',
  'password': '',
  'database': 'mydb',
}

# Specify the SQL query
query = """SELECT * FROM mydb.usage"""

# Specify the path for the CSV file
csv_path = 'output4.csv'

# Connect to the MySQL database
with mysql.connector.connect(host='localhost', user='root', password='', database='mydb') as connection:
    with connection.cursor() as cursor:
        # Execute the query
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Write the rows to a CSV file
        with open(csv_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write the header
            csv_writer.writerow([desc[0] for desc in cursor.description])

            # Write the data
            csv_writer.writerows(rows)

print(f"Data exported to {csv_path}")
