from database import BaseDeDatos


class ConsolidadorInscripciones:
    def __init__(self, base_datos: BaseDeDatos):
        self.base_datos = base_datos

    def procesar_linea(self, linea: str):
        try:
            cedula, nombre, codigo_materia, nombre_materia = map(str.strip, linea.split(','))
            self.base_datos.insertar_estudiante(cedula, nombre)
            self.base_datos.insertar_materia(codigo_materia, nombre_materia)
            self.base_datos.insertar_inscripcion(cedula, codigo_materia)
        except ValueError:
            print(f"Línea inválida ignorada: {linea}")

    def consolidar_archivo(self, ruta: str):
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                self.procesar_linea(linea)
