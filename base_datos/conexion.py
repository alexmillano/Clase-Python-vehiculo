import sqlite3

class Conexion:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()
    
    def crear_tabla(self):
        # Crea la tabla vehiculo si no existe
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehiculo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT,
            aceleracion REAL,
            color TEXT,
            velocidad REAL,
            ruedas INTEGER,
            anio TEXT,
            modelo TEXT
        )
        ''')
        self.conexion.commit()

    def crear(self, marca, aceleracion, color, velocidad, ruedas, anio, modelo):
        self.cursor.execute('''
        INSERT INTO vehiculo (marca, aceleracion, color, velocidad, ruedas, anio, modelo)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (marca, aceleracion, color, velocidad, ruedas, anio, modelo))
        self.conexion.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM vehiculo')
        return self.cursor.fetchall()

    def modificar(self, id, marca=None, aceleracion=None, color=None, velocidad=None, ruedas=None, anio=None, modelo=None):
        query = "UPDATE vehiculo SET "
        parametros = []
        if marca:
            query += "marca = ?, "
            parametros.append(marca)
        if aceleracion:
            query += "aceleracion = ?, "
            parametros.append(aceleracion)
        if color:
            query += "color = ?, "
            parametros.append(color)
        if velocidad:
            query += "velocidad = ?, "
            parametros.append(velocidad)
        if ruedas:
            query += "ruedas = ?, "
            parametros.append(ruedas)
        if anio:
            query += "anio = ?, "
            parametros.append(anio)
        if modelo:
            query += "modelo = ?, "
            parametros.append(modelo)
        
        query = query.rstrip(', ') + " WHERE id = ?"
        parametros.append(id)

        self.cursor.execute(query, parametros)
        self.conexion.commit()

    def eliminar(self, id):
        self.cursor.execute('DELETE FROM vehiculo WHERE id = ?', (id,))
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()
