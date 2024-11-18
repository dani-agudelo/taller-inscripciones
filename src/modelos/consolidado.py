from src.repository.database import BaseDeDatos
from src.validators.estudianteValidator import estudianteValidator
from src.validators.materiaValidator import materiaValidator
from src.utils.lector import Lector
from src.modelos.estudiante import Estudiante
from src.modelos.materia import Materia
from src.modelos.inscripcion import Inscripcion


class ConsolidadoInscripciones:
    def __init__(self, base_datos: BaseDeDatos):
        self.lector = Lector
        self.base_datos = base_datos
        self.estudiante= Estudiante
        self.materia = Materia
        self.inscripcion = Inscripcion
        self.validatorEstudiante = estudianteValidator()
        self.validatorMateria= materiaValidator()

    def procesar_linea(self, linea: str):
        try:
            cedula, nombre, codigo_materia, nombre_materia = map(str.strip, linea.split(','))
            # Insertar los datos en los diccionarios para validar datos en formato correcto
            boolean_estudiante = self.validatorEstudiante.validar_estudiante(cedula, nombre)
            boolean_materia = self.validatorMateria.validar_materia(codigo_materia, nombre_materia)
                        
            if boolean_estudiante == False:
                print("Error en la validacion de estudiante")
                return
            if boolean_materia == False:
                print("Error en la validacion de materia")
                return
            
            #si las validaciones son correctas insertamos los datos en la base de datos
            if boolean_estudiante == True and boolean_materia == True:
                # creamos los objetos estudiante, materia e inscripcion
                self.estudiante = Estudiante(cedula, nombre)
                self.materia = Materia(codigo_materia, nombre_materia)
                self.inscripcion = Inscripcion(self.estudiante, self.materia)
                print("Datos validados correctamente")
                self.base_datos.insertar_estudiante(self.estudiante.cedula, self.estudiante.nombre)
                self.base_datos.insertar_materia(self.materia.codigo, self.materia.nombre)
                self.base_datos.insertar_inscripcion(self.estudiante.cedula, self.materia.codigo)
                
        except ValueError:
            print(f"Línea inválida ignorada: {linea}")

    def consolidar_archivo(self, ruta: str):
         # Crear una instancia de Lector con la ruta del archivo
            lector = self.lector(ruta)
            contenido = lector.lector_archivo_texto()
            print("Contenido del archivo:")
            print(contenido)
            
             # Leer las líneas del archivo
            lineas = lector.obtener_lineas()
            for linea in lineas:
                self.procesar_linea(linea)
            
            
            
            
            
