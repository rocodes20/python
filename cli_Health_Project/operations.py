from db import get_connection

def add_data(name,date,weight,calories,mood):
    conn = get_connection()

    if conn:
        cursor = conn.cursor()
        sql = "insert into logs (name,date,weight,calories,mood) VALUES (%s,%s,%s,%s,%s)"
        val = (name,date,weight,calories,mood)
        cursor.execute(sql,val)
        conn.commit()
        print(cursor.rowcount,"record inserted")

        cursor.close()
        conn.close()

def view_data():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "Select * from logs"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        conn.close()

def update_data(name,weight,calories,mood):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "Update logs SET weight = %s,calories = %s,mood = %s where name = %s"
        val = (weight,calories,mood,name)
        cursor.execute(sql,val)
        conn.commit()
        print("updated")
        cursor.close()
        conn.close()

def delete_data(name):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = "Delete from logs where name = %s"
        val = (name,)
        cursor.execute(sql,val)
        conn.commit()
        print("deleted")
        cursor.close()
        conn.close()