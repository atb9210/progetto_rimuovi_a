from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='templates')

@app.route("/")
def form():
    return render_template("form.html")


#Ricevi input modifica parola e ritorna input
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    conn = sqlite3.connect("database/database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)""")
    c.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    #query to retrieve the data from the table
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return render_template("form.html",data=data)


#Aggiunto il DELETE button
@app.route("/card/<int:card_id>/delete", methods=["GET"])
def delete_card(card_id):
    conn = sqlite3.connect("database/database.db")
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (card_id,))
    conn.commit()
    #query to retrieve the data from the table
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return render_template("form.html",data=data)