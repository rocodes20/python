from flask import Flask,request,jsonify

app = Flask(__name__)

users = []

@app.route('/data',methods = ["GET"])
def get_users():
    return jsonify(users)

@app.route('/data',methods = ["POST"])
def post_users():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "user added"}),201

@app.route('/data/<int:id>',methods = ["PUT"])
def update_users(id):
    data = request.get_json()
    users[id].update(data)
    return jsonify({"message": "user updated"})

@app.route('/data/<int:id>',methods = ["DELETE"])
def delete_users(id):
    users.pop(id)
    return jsonify({"message": "user deleted"})


if __name__ == "__main__":
    app.run(debug=True)