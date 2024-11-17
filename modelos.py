from typing import List


class Materia:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre


class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre
        self.materias: List[Materia] = []

    def adicionar_materia(self, codigo: str, nombre: str):
        if not any(materia.codigo == codigo for materia in self.materias):
            self.materias.append(Materia(codigo, nombre))
