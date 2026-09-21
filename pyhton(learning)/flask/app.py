from flask import Flask , render_template,request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")



@app.route("/submit",methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "tirth123" and password == '12345678':
    #     return render_template("welcome.html", name = username) what if we have to check multiple password this was just one

    vaild_users = {
        'admin' :'1234',
        'tirth' :'45tirth',
        'daksh' : 'ad123'
    }

    if username in vaild_users and password == vaild_users[username]:
        return render_template("welcome.html",name = username)

    else:
        return "invaild credentials"