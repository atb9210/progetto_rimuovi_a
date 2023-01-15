from flask import Flask, render_template, request, redirect, url_for,jsonify
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='static')

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
    c.execute("SELECT * FROM users WHERE name=?", (name,))

    #SE E GIA PRESENTE NON LO REINSERISCE
    if c.fetchone():
        pass
    else:
         c.execute("INSERT INTO users (name) VALUES (?)", (name,))

    conn.commit()
    #query to retrieve the data from the table
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return render_template("form.html",data=data)


#Aggiunto il DELETE button (vecchio codice con il Refresh)
# @app.route("/card/<int:card_id>/delete", methods=["GET"])
# def delete_card(card_id):
#     conn = sqlite3.connect("database/database.db")
#     c = conn.cursor()
#     c.execute("DELETE FROM users WHERE id=?", (card_id,))
#     conn.commit()
#     #query to retrieve the data from the table
#     c.execute("SELECT * FROM users")
#     data = c.fetchall()
#     conn.close()
#     return render_template("form.html",data=data)


#CODICE AGGIORNATO PER IL DELETE USANDO JQUERY E JS 
@app.route('/card/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    conn = sqlite3.connect("database/database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (card_id,))
    result = c.fetchone()
    if result:
        c.execute("DELETE FROM users WHERE id=?", (card_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Success"}),200
    else:
        conn.close()
        return jsonify({"message": "No item found to delete"}),404