# app/utils/db_utils.py

import mysql.connector
from mysql.connector import Error
from .config import Config
from pathlib import Path

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def close_db_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Conexión cerrada")

def execute_sql_file(connection, filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            # Leer todo el contenido del archivo
            sql_content = file.read()
            
            # Dividir por ; pero ignorando los ; dentro de las declaraciones
            sql_commands = [cmd.strip() for cmd in sql_content.split(';') if cmd.strip()]
        
        cursor = connection.cursor()
        for command in sql_commands:
            try:
                cursor.execute(command)
                # Reducir el output para no saturar la consola
                print(f"Ejecutado comando SQL exitosamente")
            except Error as e:
                # Si el error es por tabla/dato duplicado, lo ignoramos
                if "already exists" in str(e):
                    print(f"Nota: Objeto ya existe, continuando...")
                else:
                    print(f"Error ejecutando SQL: {e}")
        connection.commit()
        print("Todos los comandos SQL fueron procesados")
    except Exception as e:
        print(f"Error al procesar el archivo SQL: {e}")

def show_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Tablas en la base de datos:")
    for table in tables:
        print(table[0])

if __name__ == "__main__":
    # Bloque de prueba
    conn = get_db_connection()
    if conn:
        # Usando Path de pathlib
        sql_path = Path(__file__).parent.parent.parent / 'sql' / 'musiverse.sql'
        
        execute_sql_file(conn, sql_path)
        show_tables(conn)
        close_db_connection(conn)
