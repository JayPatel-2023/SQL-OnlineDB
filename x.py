#it's working!!

import mysql.connector

# Replace these with your actual database details
hostname = "sql12.freesqldatabase.com"
username = "sql12651137"
password = "YGUSAty7ft"
database = "sql12651137"

# Connect to the database
conn = mysql.connector.connect(
    host=hostname,
    user=username,
    password=password,
    database=database
)

# Check if the connection is successful
if conn.is_connected():
    print("Connected to the database")

    # Create a cursor to interact with the database
    cursor = conn.cursor()

    # Fetch data from the table
    query = "SELECT * FROM students"
    cursor.execute(query)

    # Display the results
    for (student_id, first_name, last_name, age, grade) in cursor:
        print(f"ID: {student_id}, Name: {first_name} {last_name}, Age: {age}, Grade: {grade}")

    # Close the cursor and connection
    cursor.close()
    conn.close()
else:
    print("Connection failed")
