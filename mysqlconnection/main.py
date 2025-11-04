from flask import Flask, jsonify,request
from db import get_connection

app = Flask(__name__)

@app.route('/users',methods = ["GET"])
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    sql = "SELECT * FROM custs"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/users',methods = ["POST"])
def post_users():
    conn = get_connection()
    cursor = conn.cursor()
    data = request.get_json()
    
    name,age,weight = data.get('name'),data.get('age'),data.get('weight')
    if not all[name,age,weight]:
        return jsonify({"Error":"NOT ALL VALUES PRESENT"})
    sql = "INSERT INTO custs (name,age,weight) VALUES (%s, %s, %s)"
    val = (name,age,weight)
    cursor.execute(sql,val)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message":"added"})

@app.route('/users/<int:id>',methods = ["PUT"])
def update_users(id):
    conn = get_connection()
    cursor = conn.cursor()
    data = request.get_json()
    name,age,weight = data.get('name'),data.get('age'),data.get('weight')
    sql = ("UPDATE  custs SET name = %s,age= %s,weight = %s WHERE id = %s")
    val = (name,age,weight,id)
    cursor.execute(sql,val)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message":"updated"})


@app.route('/users/<int:id>',methods=["DELETE"])
def delete_user(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM custs WHERE id = %s",(id,))
        conn.commit()
    except mysql.connector.Error as db_err:
        print(db_err)
        return jsonify({"error":"DB issue"})
    except Exception as e:
        print(e)
        return jsonify({"error":"Unexpected issue"})
    finally:
        cursor.close()
        conn.close()
    return jsonify({"message":"deleted"})


if __name__ == "__main__":
    app.run(debug=True)