import sqlite3

connection = sqlite3.connect("dbsuenios.db")

# Crear tabla
CREA_TABLA = '''
CREATE TABLE IF NOT EXISTS suenios (
    suenio TEXT, 
    fecha TEXT
);
'''

# Insertar un sueño
INSERTA_SUENIO = "INSERT INTO suenios VALUES (?, ?);"

def crear_tabla():
    with connection:
        connection.execute(CREA_TABLA)

def agregar_suenio(suenio, fecha):
    with connection:
        connection.execute(INSERTA_SUENIO, (suenio, fecha))

# Obtener todos los sueños
def obtener_suenios():
    with connection:
        cursor = connection.execute("SELECT rowid, suenio, fecha FROM suenios;")
        return cursor.fetchall()

# Buscar por palabra clave
def buscar_por_palabra(palabra):
    with connection:
        cursor = connection.execute("SELECT rowid, suenio, fecha FROM suenios WHERE suenio LIKE ?;", (f"%{palabra}%",))
        return cursor.fetchall()

# Buscar por fecha exacta
def buscar_por_fecha(fecha):
    with connection:
        cursor = connection.execute("SELECT rowid, suenio, fecha FROM suenios WHERE fecha = ?;", (fecha,))
        return cursor.fetchall()

def cierra_conexion():
    connection.close()


