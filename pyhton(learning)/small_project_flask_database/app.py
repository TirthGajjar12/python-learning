from flask import Flask,render_template,request,redirect,session
import mysql.connector

app = Flask(__name__)

app.secret_key = "super_secret_learning_key"
db = mysql.connector.connect(host="localhost",user="root",password="root",database="db1")
print("Database connected successfully: ",db)


@app.route("/signup",methods=['GET','POST'])
def signup():
    print("Someone visited the route!")
    if request.method == "POST":
        print("The form was submitted!")
        Username = request.form.get("username")
        Email = request.form.get("email")
        password = request.form.get("password")

        cursor = db.cursor()

        sql = "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
        values = (Username,Email,password)

        cursor.execute(sql,values)
        db.commit()

        return redirect('/login')
    return render_template('signup.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        for_email = request.form.get('email')
        for_password = request.form.get('password')

        cursor = db.cursor(dictionary=True)

        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        values = (for_email,for_password)

        cursor.execute(sql,values)

        user = cursor.fetchone()

        if user:

            session['user'] = user['name']

            return redirect('/welcome')

        else:

            return "Invalid email or password please go back and try again"
    return render_template('login.html')

@app.route("/welcome")
def welcome():
    if 'user' in session:
        current_user = session['user']

        return render_template('welcome.html',username=current_user)

    return redirect('/login')


