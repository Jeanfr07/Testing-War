import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='smartdb'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
