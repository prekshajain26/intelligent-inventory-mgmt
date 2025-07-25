import mysql.connector

import mysql.connector

# Replace with your actual credentials
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="prekshajain26",
    database="myproject"  # optional if you just want to connect to the server
)

if conn.is_connected():
    print("Connection successful!")
else:
    print("Connection failed.")

conn.close()
