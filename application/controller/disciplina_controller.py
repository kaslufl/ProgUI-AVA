from application import app
from flask import render_template, request
from application import avaDAO
# importar as classes que são usadas na página

@app.route("/disciplina/<codigo_disciplina>")
def disciplina(codigo_disciplina):
    disciplina = avaDAO.get_disciplina_by_id(int(codigo_disciplina))
    aulas = disciplina.get_aulas()
    return render_template("disciplina.html", disciplina = disciplina, aulas = aulas)