import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Pass123!",
        database = "test"
    )
    print("Db connected")
except mysql.connector.Error as err:
    print(err)