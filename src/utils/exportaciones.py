import json
import csv

def exportar_a_json(base_datos):
    estudiantes = base_datos.conexion.execute("SELECT * FROM estudiantes").fetchall()
    materias = base_datos.conexion.execute("SELECT * FROM materias").fetchall()
    inscripciones = base_datos.conexion.execute("SELECT * FROM inscripciones").fetchall()


    datos = {"estudiantes": [], "materias": [], "inscripciones": []}

    for estudiante in estudiantes:
        datos["estudiantes"].append({"cedula": estudiante[0], "nombre": estudiante[1]})

    for materia in materias:
        datos["materias"].append({"codigo": materia[0], "nombre": materia[1]})

    for inscripcion in inscripciones:
        datos["inscripciones"].append({"cedula_estudiante": inscripcion[0], "codigo_materia": inscripcion[1]})

    with open("inscripciones.json", "w", encoding="utf-8") as json_file:
        json.dump(datos, json_file, ensure_ascii=False, indent=4)

    print("Datos exportados a inscripciones.json")

def exportar_a_csv(base_datos):
    inscripciones = base_datos.conexion.execute("""
        SELECT estudiantes.cedula, estudiantes.nombre, materias.codigo, materias.nombre
        FROM inscripciones
        JOIN estudiantes ON inscripciones.cedula_estudiante = estudiantes.cedula
        JOIN materias ON inscripciones.codigo_materia = materias.codigo
    """).fetchall()

    with open("inscripciones.csv", "w", encoding="utf-8", newline="") as csv_file:
        escritor = csv.writer(csv_file)
        escritor.writerow(["Cédula", "Nombre Estudiante", "Código Materia", "Nombre Materia"])
        escritor.writerows(inscripciones)

    print("Datos exportados a inscripciones.csv")
