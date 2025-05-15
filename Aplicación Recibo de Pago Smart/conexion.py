import mysql.connector

def conectar():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='smartdb'
    )
    conn.autocommit = True
    return conn

def desconectar(conn):
    conn.close()