from application import app
from flask import render_template, request
# importar as classes que são usadas na página

@app.route("/disciplina/<codigo_disciplina>")
def disciplina(codigo_disciplina):

    return render_template("disciplina.html")