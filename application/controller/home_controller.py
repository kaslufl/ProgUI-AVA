from application import app
from flask import render_template, request
from application.model.entity.disciplina import Disciplina
from application.model.entity.aula import Aula
from application import avaDAO
# importar as classes que são usadas na página

@app.route("/")
@app.route("/home")
def home():
    lista_disciplinas = avaDAO.listar_todas_disciplinas()
    return render_template("home.html", lista_disciplinas = lista_disciplinas)