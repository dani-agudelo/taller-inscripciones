
from src.utils.lector import Lector
def prueba():

    # Crear una instancia de Lector con la ruta del archivo
    lector = Lector('prueba.txt')

    # Leer todo el contenido del archivo
    contenido = lector.lector_archivo_texto()
    print("Contenido del archivo:")
    print(contenido)

    # Leer las líneas del archivo
    lineas = lector.obtener_lineas()
    print("\nLíneas del archivo:")
    for linea in lineas:
        print(linea, end='')
    
if __name__ == "__main__":
    prueba()
    
