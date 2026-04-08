import os
import sqlite3
from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(index.html)
@app.route("/primer-string")
def string():
    return "Neki ne preterano dugacak tekst"
@app.route("/primer-broj")
def broj():
    return 265
if __name__=="__main__":
    app.run(debug=True)
