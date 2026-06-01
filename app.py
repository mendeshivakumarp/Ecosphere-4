from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shiva123",
    database="eco"
)

cursor=db.cursor()

@app.route('/')
def home():
    return render_template("contact.html")
@app.route("/submit",methods=["POST"])
def main():

    fullname=request.form["fullname"]
    email=request.form["email"]
    mobilenumber=request.form["mobilenumber"]
    message=request.form["message"]

    sql="INSERT INTO contact_messages (fullname,email,mobilenumber,message) VALUES (%s,%s,%s,%s)"

    values=(fullname, email ,mobilenumber,message)
    cursor.execute(sql,values)
    db.commit()


app.run(debug=True)













