import mysql.connector

# Connect to MySQL database
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ahmed@6602",
)

print(myconn)
