import os
import sqlite3
from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    naslovSpiska="Restorani"
    spisakRestorana=["Groš", "Bavka", "Nedodjija", "Dits", "ABC"]
    return render_template(index.html, naslov=naslovSpiska, spisak=spisakRestorana)
    
@app.route("/restoran/1")
def index():
    naslovSpiska="Bavka meni"
    spisakJela=["Gulaš", "Suši", "Kineska", "Ramen", "Čimičuri"]
    return render_template(restoran.html, naslov=naslovSpiska, spisak=spisakJela)
    
@app.route("/primer-string")
def string():
    return "Neki ne preterano dugacak tekst
@app.route("/primer-broj")
def broj():
    return 265
if __name__=="__main__":
    app.run(debug=True)
