from flask import Flask,request,jsonify
from db import get_connection
app = Flask(__name__)

@app.route('/all',methods=["GET"])
def get_all():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM crop_data")
        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as db_err:
        print(db_err)
        return jsonify({"message":"dbError"})
    except Exception as E:
        print(E)
        return jsonify({"message":"Unexpected err"})
    finally:
        if cursor in locals():
            cursor.close()
        if conn in locals():
            conn.close()


@app.route('/market',methods = ["GET"])
def get_markets():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT city from crop_data")
        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as db_err:
        print(db_err)
        return jsonify({"message":"dbError"})
    except Exception as E:
        print(E)
        return jsonify({"message":"Unexpected err"})
    finally:
        if cursor in locals():
            cursor.close()
        if conn in locals():
            conn.close()

@app.route('/commodity',methods=["GET"])
def get_commodity():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT commodity FROM crop_data ")
        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as db_err:
        print(db_err)
        return jsonify({"message":"dbError"})
    except Exception as E:
        print(E)
        return jsonify({"message":"Unexpected err"})
    finally:
        if cursor in locals():
            cursor.close()
        if conn in locals():
            conn.close()

@app.route('/add',methods = ["POST"])
def add_data():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = request.get_json()
        state = data.get('state')
        city = data.get('city')
        commodity = data.get('commodity')
        variety = data.get('variety')
        arrival_date = data.get('arrival_date')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        modalPrice = data.get('modalPrice')
        code = data.get('code')
        sql = "INSERT INTO crop_data (state,city,commodity,variety,arrival_date,minPrice,maxPrice,modalPrice,code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (state,city,commodity,variety,arrival_date,minPrice,maxPrice,modalPrice,code)
        cursor.execute(sql,val)
        conn.commit()
        return jsonify({"message":"added"})
    except mysql.connector.Error as db_err:
        print(db_err)
        return jsonify({"message":"dbError"})
    except Exception as E:
        print(E)
        return jsonify({"message":"Unexpected err"})
    finally:
        if cursor in locals():
            cursor.close()
        if conn in locals():
            conn.close()


@app.route('/update/<int:id>',methods = ["PUT"])
def update_data(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = request.get_json()
        state = data.get('state')
        city = data.get('city')
        commodity = data.get('commodity')
        variety = data.get('variety')
        arrival_date = data.get('arrival_date')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        modalPrice = data.get('modalPrice')
        code = data.get('code')

        sql = """UPDATE crop_data SET state = %s,city = %s,commodity = %s,variety = %s,arrival_date = %s,minPrice = %s,maxPrice = %s,
modalPrice = %s,code = %s WHERE id = %s"""

        val = (state,city,commodity,variety,arrival_date,minPrice,maxPrice,modalPrice,code,id)

        cursor.execute(sql,val)
        conn.commit()
        return jsonify({"message":"added"})
    except mysql.connector.Error as db_err:
        print(db_err)
        return jsonify({"message":"dbError"})
    except Exception as E:
        print(E)
        return jsonify({"message":"Unexpected err"})
    finally:
        if cursor in locals():
            cursor.close()
        if conn in locals():
            conn.close()

@app.route('/delete/<int:id>',methods  = ["DELETE"])
def delete_data(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM crop_data WHERE id = %s",(id,))
        conn.commit()
        return jsonify({"message":"deleted"})
    except mysql.connector.Error as db_err:
        print(db_err)
        return jsonify({"message":"dbError"})
    except Exception as E:
        print(E)
        return jsonify({"message":"Unexpected err"})
    finally:
        if cursor in locals():
            cursor.close()
        if conn in locals():
            conn.close()
        





if __name__ == "__main__":
    app.run(debug=True)