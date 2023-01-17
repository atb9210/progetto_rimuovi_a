from flask import Flask, render_template, request, redirect, url_for,jsonify
import sqlite3
from models import *

app = Flask(__name__, template_folder='templates', static_folder='static')



#TEST VUE
@app.route('/api/route', methods=['GET'])
def get_value():
    value = request.args.get('value')
    response = "Risposta Ricevuta Reazione!!!"
    print(response)
    return value

# INDEX PAGE
@app.route("/")
def form():
    data=get_all_users()
    return render_template("base.html",data=data)

# ADD USER FROM INPUT
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    add_user(name) 
    data=get_all_users() 
    return render_template("base.html",data=data)

# DELETE (Jquery)
@app.route('/card/<int:card_id>', methods=['DELETE'])
def delete(card_id):
     return delete_user(card_id)

# OPEN MODAL EDIT
@app.route('/edit/<card_id>')
def edit_card(card_id):
    user = get_user_by_id(card_id)
    return jsonify(user)

# SUMBIT AND SAVE EDIT
@app.route('/update', methods=["POST"])
def update_card():
    card_id = request.form['id']
    new_name = request.form['name']
    update_user(card_id, new_name)
    return redirect(url_for('form'))