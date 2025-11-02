import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Pass123!",
    database = "test"
)

cursor = db.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS STU(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
marks INT
)
"""
)

print("table created ")