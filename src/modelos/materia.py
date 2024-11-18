class Materia:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.inscripciones = []

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'