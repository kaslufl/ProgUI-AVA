class Disciplina:
    def __init__(self, codigo, titulo):
        self._codigo = codigo
        self.titulo = titulo
        self.aulas = []

    def get_codigo(self):
        return self._codigo

    def get_titulo(self):
        return self.titulo

    def get_aulas(self):
        return self.aulas
    
    def set_aulas(self, lista):
        self.aulas = lista
    