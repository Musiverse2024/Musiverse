import mysql.connector
from mysql.connector import Error

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456789',
            database='musiverseDB'  
        )
        if connection.is_connected():
            print("Conexión a la base de datos exitosa")
        return connection
    except Error as e:
        print(f"Error durante la conexión a la base de datos: {e}")
        return None

def close_db_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Conexión a la base de datos cerrada")

def execute_sql_file(connection, filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            sql_commands = file.read().split(';')
        
        cursor = connection.cursor()
        for command in sql_commands:
            try:
                if command.strip():
                    cursor.execute(command)
                    print(f"Ejecutado: {command.strip()}")
            except Error as e:
                print(f"Error ejecutando el comando: {command.strip()}\nError: {e}")
        connection.commit()
    except Exception as e:
        print(f"Error al leer el archivo SQL: {e}")


def show_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Tablas en la base de datos:")
    for table in tables:
        print(table[0])

if __name__ == "__main__":
    conn = create_db_connection()
    if conn:
        execute_sql_file(conn, 'musiverse.sql')  
        show_tables(conn) 
        close_db_connection(conn)
