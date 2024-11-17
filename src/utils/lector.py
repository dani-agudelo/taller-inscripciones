class Lector:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def lector_archivo_texto(self):
        with open(self.nombre_archivo, 'r', encoding= 'utf-8') as file:
            return file.read()
        
        
    def obtener_lineas(self):
        with open(self.nombre_archivo, 'r', encoding= 'utf-8') as file:
            return file.readlines()