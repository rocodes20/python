import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Pass123!",
        database = "TEST"
    )

    cursor = mydb.cursor()

    #create
    # sql = "insert into stu (name,marks) VALUES (%s,%s)"
    # val = ("Rohit",99)

    # cursor.execute(sql,val)
    # mydb.commit()
    # print(cursor.rowcount,"record inserted")

    #read

    cursor.execute("SELECT * FROM STU")
    result = cursor.fetchall()

    for row in result:
        print(row)

    # #update 

    # sql = "UPDATE STU SET MARKS = %s WHERE NAME = %s"
    # val = (100,"Rohit")

    # cursor.execute(sql,val)
    # mydb.commit()
    # print("updated")

    #delete

    sql = "DELETE FROM STU WHERE NAME = %s"
    val = ("Rohit",)

    cursor.execute(sql,val)
    mydb.commit()
    print("deleted")

except Exception as err:
    print(err)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("connection closed")