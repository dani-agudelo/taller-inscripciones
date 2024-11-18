from src.repository.database import BaseDeDatos
from src.modelos.consolidado import ConsolidadoInscripciones
from src.utils.exportaciones import exportar_a_json, exportar_a_csv


def menu():
    base_datos = BaseDeDatos()
    consolidador = ConsolidadoInscripciones(base_datos)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Cargar archivo de inscripciones")
        print("2. Mostrar materias inscritas por estudiante")
        print("3. Mostrar estudiantes inscritos en una materia")
        print("4. Mostrar estudiante")
        print("5. Convertir a JSON/CSV")
        print("6. Salir")

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
                    print(f"- Código: {codigo}, Nombre: {nombre}")
            else:
                print(f"No se encontraron materias para el estudiante {cedula}.")
        elif opcion == "3":
            codigo = input("Ingrese el código de la materia: ")
            estudiantes = base_datos.obtener_estudiantes_por_materia(codigo)
            if estudiantes:
                print(f"\nEstudiantes inscritos en la materia {codigo}:")
                for cedula, nombre in estudiantes:
                    print(f"- Nombre: {nombre}, Cédula: ({cedula})")
            else:
                print(f"No se encontraron estudiantes para la materia {codigo}.")
        elif opcion == "4":
            cedula_estudiante = input("Ingrese la cédula del estudiante: ")
            estudiante = base_datos.obtener_estudiante_por_cedula(cedula_estudiante)
            if estudiante:
                print(f"\nEstudiante con cédula {cedula_estudiante}:")
                for cedula, nombre in estudiante:
                    print(f"- Cédula: {cedula}, Nombre: {nombre}")
            else:
                print(f"No se encontró un estudiante con la cédula {cedula_estudiante}.")
        elif opcion == "5":
            tipo_exportacion = input("¿Desea exportar a JSON o CSV? (j/c): ").lower()
            if tipo_exportacion == "j":
                exportar_a_json(base_datos)
            elif tipo_exportacion == "c":
                exportar_a_csv(base_datos)
            else:
                print("Opción inválida.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    menu()
