class Inscripcion:
    def __init__(self, estudiante, materia):
        self.estudiante = estudiante
        self.materia = materia

    def __str__(self):
        return f'Alumno: {self.estudiante}, Curso: {self.materia}'

    def __repr__(self):
        return str(self)