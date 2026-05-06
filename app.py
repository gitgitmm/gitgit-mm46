import os
import sqlite3
from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite.3.connect('dostavaHrane.db')

    cur = con.cursor()
    cur.execute("SELECT id, naziv FROM restorani LIMIT 10")

    restorani = cur.fetchall()
    return render_template("index.html", naslov="Spisak restorana", spisak=restorani)
    
@app.route("/restoran/<id_rest>")
def meni_restorana(id_rest):
    con = sqlite3.connect('dostavaHrane.db')

    cur = con.cursor()
    query = f"SELECT naziv FROM meni where id_restorana == {id_rest}
    cur.execute(query)

    meni = cur.fetchall()
    return render_template("meni.html", naslov="Pastica", meni=meni)
    
@app.route("/primer-string")
def string():
    return "Neki ne preterano dugacak tekst
@app.route("/primer-broj")
def broj():
    return 265
if __name__=="__main__":
    app.run(debug=True)
