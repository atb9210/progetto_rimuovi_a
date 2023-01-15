from flask import Flask, render_template, request, redirect, url_for,jsonify
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='static')


#Funzione connessione al database
def get_db():
    conn = sqlite3.connect("database/database.db")
    c = conn.cursor()
    return conn, c

#estraiamo tutti gli utenti
def get_all_users():
    conn, c = get_db()
    c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)""")
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    return data

#delete a user by id 
def delete_user(card_id):
    conn, c = get_db()
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


