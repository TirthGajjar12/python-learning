from flask import Flask, jsonify


app = Flask(__name__)


print(__name__)

@app.route('/')
def hello_world():
    return "hello world"

app.run(debug=True)