import mysql.connector

my_db = mysql.connector.connect(host='localhost',user="root",password="root",database='db1')

my_cursor = my_db.cursor()

my_cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ("Tirth", "Tirthgajjar@gmail.com")
)
my_cursor.execute("select * from users")
for i in my_cursor:
    print(i)

my_db.commit()