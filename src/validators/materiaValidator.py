class materiaValidator:
    def __init__(self):
        pass
        
    def validar_materia(self, codigo, nombre):
        # el código debe ser una cadena de 4 caracteres
        if len(codigo) != 4:
            return False
        # el nombre no debe estar vacío
        if not nombre:
            return False
        return True