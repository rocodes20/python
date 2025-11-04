from flask import Flask,request,jsonify

app = Flask(__name__)

users = []

@app.route('/add',methods = ["POST"])
def add_users():
    data = request.get_json()
    if not data:
        return jsonify({"message":"No json data"}),400
    name = data.get('name')
    steps = data.get('steps')
    calories = data.get('calories')

    users.append({
        "name":name,
        "steps":steps,
        "calories":calories
    })

    return jsonify({"message":"Data received successfully"}),201

@app.route('/summary',methods =["GET"])
def get_users():
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)