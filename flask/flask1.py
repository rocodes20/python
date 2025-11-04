from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello World"

@app.route('/home/<name>')
def home(name):
    return f"this is home page {name}"

if __name__ == '__main__':
    app.run(debug = True)