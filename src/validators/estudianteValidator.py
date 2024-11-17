class estudianteValidator:
    def __init__(self):
        
    def validar_estudiante(self, cedula, nombre):
       # la cedula debe ser un número, debe tener 7 dígitos y no debe empezar por 0
        if not cedula.isdigit() or len(cedula) != 7 or cedula.startswith('0'):
            return False
        # el nombre no debe estar vacío
        if not nombre:
            return False
        return True