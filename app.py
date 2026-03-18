import os
import sqlite3
from flask import Flask, request, jsonify, json
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    return "Zdravo brate"
@app.route("/primer-string")
def string():
    return "Neki ne preterano dugacak tekst"
@app.route("/primer-broj")
def broj():
    return 265
@app.route("/primer-niz")
def niz():
    nekiNiz = [1,2,3,4,5]
    return nekiNiz
@app.route("/primer-json")
def primerJson():
    data = {
        "message": "This is a JSON response", 
        "status": "successs"
    }
