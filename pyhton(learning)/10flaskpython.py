from Flask import Flask,jsonify

app  = Flask(__name__)

@app.route('/')

def home():

    return jsonify({ 
        "status" : "success",
        "message" : "this api is running"
    })


if __name__ == '__main__':
    app.run(debug=True)
