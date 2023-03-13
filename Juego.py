class Juego:
    def __init__(self, codigo, nombre, plataforma):
        self.codigo = codigo
        self.nombre = nombre
        self.plataforma = plataforma

        self.siguiente = None
        self.anterior = None
        