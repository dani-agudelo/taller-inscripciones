class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre
        self.inscripciones = []

    def __str__(self):
        return f"{self.cedula} - {self.nombre}"