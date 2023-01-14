from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='templates')

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)""")
    c.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    #query to retrieve the data from the table
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return render_template("form.html",data=data)