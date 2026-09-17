#this is a main file consider this as brain of our server in flask

from flask import Flask,request,redirect,url_for,session,Response

app = Flask(__name__) #__name__ is means that it is telling the python that the application is created in this module(means that the file is where the flask app is created)
app.secret_key = "supersecret"

# @app.route("/")
# def home():
#     return "Hello user this is my first flask app!" 

# @app.route("/about")
# def about():
#     return "this is about page"

# @app.route("/contact")
# def contact():
#     return "this is contact us page"

# @app.route("/submit",methods=["GET","POST"])
# def submit():
#     if request.method == "POST":
#         return "you sent data"
#     else:
#         return "your only viewing the from"


#small project login page home page

@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password =="123":
            session["user"] = username #store in session (it is an dictionary)
            return redirect(url_for("welcome"))
        else:
            return Response("Invaild credentials.try again",mimetype="text/plain")

    return '''
    <h2>Login page</h2>
    <form method="POST">
    username : <input type="text" name="username"></br>
    password : <input type="text" name="password"></br>
    <input type="submit" value="Login">
    </form>
'''

#welcome page after login
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome , {session["user"]}!</h2>
        <a href={url_for('logout')}>Logout</a>
    """

    return redirect(url_for("login"))


#logout
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))