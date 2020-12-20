from application import app
from flask import render_template, request
# importar as classes que são usadas na página

@app.route("/")
@app.route("/home")
def home(): 
    return render_template("home.html")