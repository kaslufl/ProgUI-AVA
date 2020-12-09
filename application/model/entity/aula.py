class Aula:
    def __init__(self, codigo, titulo):
        self._codigo = codigo
        self.titulo = titulo
        self.materiais = []

    def get_codigo(self):
        return self._codigo

    def get_titulo(self):
        return self.titulo
    
    def get_materiais(self):
        return self.materiais
    
    def set_materiais(self, lista):
        self.materiais = lista