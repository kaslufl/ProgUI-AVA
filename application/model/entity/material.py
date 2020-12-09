class Material:
    def __init__(self, codigo, titulo, tipo, material_URL):
        self._codigo = codigo
        self.titulo = titulo
        self.tipo = tipo
        self.url = material_URL

    def get_codigo(self):
        return self._codigo

    def get_titulo(self):
        return self.titulo
    
    def get_tipo(self):
        return self.tipo
    