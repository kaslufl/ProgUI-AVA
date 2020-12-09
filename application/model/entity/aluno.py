class Aluno:
    def __init__(self, codigo, nome):
        self._codigo = codigo
        self.nome = nome

    def get_codigo(self):
        return self._codigo   

    def get_nome(self):
        return self.nome