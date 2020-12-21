from application.model.entity.disciplina import Disciplina
from application.model.entity.aula import Aula
from application.model.entity.material import Material

class AvaDAO:
    def __init__(self):
        pdf = Material(1, "Artigo", "pdf")
        slide = Material(2, "Aula", "slide")
        video = Material(3, "Aula Gravada", "video")

        lista_materiais = [pdf, slide, video]

        aula1 = Aula(1, "Aula 1")
        aula1.set_materiais(lista_materiais)
        aula2 = Aula(2, "Aula 2")
        aula2.set_materiais(lista_materiais)
        aula3 = Aula(3, "Aula 3")
        aula3.set_materiais(lista_materiais)

        lista_aulas = [aula1, aula2, aula3]

        disciplina1 = Disciplina(1, "Lab. de Programação de Interface com Usuário")
        disciplina1.set_aulas(lista_aulas)
        disciplina2 = Disciplina(2, "Modelagem de Banco de Dados")
        disciplina2.set_aulas(lista_aulas)
        disciplina3 = Disciplina(3, "Gestão Estratégica de Pessoas")
        disciplina3.set_aulas(lista_aulas)
        disciplina4 = Disciplina(4, "Legislação Aplicada à Informática")
        disciplina4.set_aulas(lista_aulas)
        disciplina5 = Disciplina(5, "Sistemas Operacionais")
        disciplina5.set_aulas(lista_aulas)

        self.lista_disciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5]

    def listar_todas_disciplinas(self):
        return self.lista_disciplinas

    def get_disciplina_by_id(self, codigo):
        disciplina = list(filter(lambda disciplina : disciplina.get_codigo() == codigo, self.lista_disciplinas))
        if len(disciplina) == 0:
            return None
        return disciplina[0]

    def get_disciplina_by_name(self, titulo):
        disciplina = list(filter(lambda disciplina : disciplina.get_titulo() == titulo, self.lista_disciplinas))
        if len(disciplina) == 0:
            return None
        return disciplina[0]       