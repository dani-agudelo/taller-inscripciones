from src.repository.database import BaseDeDatos
from src.modelos.consolidado import ConsolidadoInscripciones


def menu():
    base_datos = BaseDeDatos()
    consolidador = ConsolidadoInscripciones(base_datos)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Cargar archivo de inscripciones")
        print("2. Mostrar materias inscritas por estudiante")
        print("3. Mostrar estudiantes inscritos en una materia")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo de inscripciones: ")
            try:
                consolidador.consolidar_archivo(ruta)
                print("Archivo cargado y datos almacenados en la base de datos.")
            except Exception as e:
                print(f"Error al cargar el archivo: {e}")
        elif opcion == "2":
            cedula = input("Ingrese la cédula del estudiante: ")
            materias = base_datos.obtener_materias_por_estudiante(cedula)
            if materias:
                print(f"\nMaterias inscritas por el estudiante {cedula}:")
                for codigo, nombre in materias:
                    print(f"- {codigo}: {nombre}")
            else:
                print(f"No se encontraron materias para el estudiante {cedula}.")
        elif opcion == "3":
            codigo = input("Ingrese el código de la materia: ")
            estudiantes = base_datos.obtener_estudiantes_por_materia(codigo)
            if estudiantes:
                print(f"\nEstudiantes inscritos en la materia {codigo}:")
                for cedula, nombre in estudiantes:
                    print(f"- {nombre} ({cedula})")
            else:
                print(f"No se encontraron estudiantes para la materia {codigo}.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()
