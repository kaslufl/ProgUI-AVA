from flask import Flask
import os
from application.model.dao.avaDAO import AvaDAO

avaDAO = AvaDAO()

app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/template"))

from application.controller import home_controller, disciplina_controller