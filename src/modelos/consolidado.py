from database import BaseDeDatos

from validators.estudianteValidator import EstudianteValidator
from validators.materiaValidator import MateriaValidator



class ConsolidadoInscripciones:
    def __init__(self, base_datos: BaseDeDatos):
        self.base_datos = base_datos
        self.estudiantes = {}
        self.materias = {}
        self.validatorEstudiante = EstudianteValidator()
        self.validatorMateria

    def procesar_linea(self, linea: str):
        try:
            cedula, nombre, codigo_materia, nombre_materia = map(str.strip, linea.split(','))
            # Insertar los datos en los diccionarios para validar datos en formato correcto
            self.estudiantes[cedula] = nombre
            self.materias[codigo_materia] = nombre_materia
            print(f"Estudiante: {cedula} - {nombre}")
            print(f"Materia: {codigo_materia} - {nombre_materia}")
            # llamamos a validators para validar los datos
            # validator estudianteValidator
            # validator materiaValidator
            # validator inscripcionValidator
            boolean_estudiante = self.validatorEstudiante.validar_estudiante(cedula, nombre)
            
            self.base_datos.insertar_estudiante(cedula, nombre)
            self.base_datos.insertar_materia(codigo_materia, nombre_materia)
            self.base_datos.insertar_inscripcion(cedula, codigo_materia)
        except ValueError:
            print(f"Línea inválida ignorada: {linea}")

    def consolidar_archivo(self, ruta: str):
         # Crear una instancia de Lector con la ruta del archivo
            lector = Lector(ruta)
            contenido = lector.lector_archivo_texto()
            print("Contenido del archivo:")
            print(contenido)
            
             # Leer las líneas del archivo
            lineas = lector.obtener_lineas()
            for linea in lineas:
                self.procesar_linea(linea)
            
            
            
            
            
