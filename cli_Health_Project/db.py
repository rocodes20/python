import mysql.connector 

def get_connection():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Pass123!",
            database = "health"
        )
        
        return conn
    except Exception as e:
        print(e)
        return None
