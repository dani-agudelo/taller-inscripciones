import sqlite3


class BaseDeDatos:
    def __init__(self, nombre_bd: str = "inscripciones.db"):
        self.conexion = sqlite3.connect(nombre_bd)
        self.crear_tablas()

    def crear_tablas(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                cedula TEXT PRIMARY KEY,
                nombre TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS materias (
                codigo TEXT PRIMARY KEY,
                nombre TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inscripciones (
                cedula_estudiante TEXT,
                codigo_materia TEXT,
                PRIMARY KEY (cedula_estudiante, codigo_materia),
                FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula),
                FOREIGN KEY (codigo_materia) REFERENCES materias(codigo)
            )
        """)
        self.conexion.commit()

    def insertar_estudiante(self, cedula: str, nombre: str):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT OR IGNORE INTO estudiantes (cedula, nombre) VALUES (?, ?)", (cedula, nombre))
        self.conexion.commit()

    def insertar_materia(self, codigo: str, nombre: str):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT OR IGNORE INTO materias (codigo, nombre) VALUES (?, ?)", (codigo, nombre))
        self.conexion.commit()

    def insertar_inscripcion(self, cedula: str, codigo: str):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT OR IGNORE INTO inscripciones (cedula_estudiante, codigo_materia) VALUES (?, ?)",
                       (cedula, codigo))
        self.conexion.commit()

    def obtener_materias_por_estudiante(self, cedula: str):
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT materias.codigo, materias.nombre
            FROM inscripciones
            JOIN materias ON inscripciones.codigo_materia = materias.codigo
            WHERE inscripciones.cedula_estudiante = ?
        """, (cedula,))
        return cursor.fetchall()

    def obtener_estudiantes_por_materia(self, codigo: str):
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT estudiantes.cedula, estudiantes.nombre
            FROM inscripciones
            JOIN estudiantes ON inscripciones.cedula_estudiante = estudiantes.cedula
            WHERE inscripciones.codigo_materia = ?
        """, (codigo,))
        return cursor.fetchall()
    
    def obtener_estudiante_por_cedula(self, cedula: str):
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT cedula, nombre
            FROM estudiantes
            WHERE cedula = ?
        """, (cedula,))
        return cursor.fetchall()

