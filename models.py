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
    conn.commit()
    conn.close()
    return data

#Submit
def add_user(name):
    conn, c = get_db()
    c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)""")
    c.execute("SELECT * FROM users WHERE name=?", (name,))

    #SE E GIA PRESENTE NON LO REINSERISCE
    if c.fetchone():
        pass
    else:
         c.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()

#Delete user
def delete_user(card_id):
    conn,c = get_db()
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

#Get user by id
def get_user_by_id(card_id):
    conn,c = get_db()
    c.execute("SELECT * FROM users WHERE id=?", (card_id,))
    user = c.fetchone()
    conn.close()
    return user

def update_user(card_id, name):
    conn,c = get_db()
    # Update the user's name in the database
    c.execute("UPDATE users SET name=? WHERE id=?", (name, card_id))
    conn.commit()
    conn.close()

