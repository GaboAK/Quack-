import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'port': 3306,
    'database': 'monedero_db'
}

def inicializar_base_de_datos():
    try:
        conexion_servidor = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            port=DB_CONFIG['port']
        )

        if conexion_servidor.is_connected():
            cursor = conexion_servidor.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            cursor.close()
            conexion_servidor.close()

        conexion = obtener_conexion()
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            query_tabla = """
            CREATE TABLE IF NOT EXISTS cajas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                categoria VARCHAR(100) NOT NULL,
                nombre_moneda VARCHAR(100) NOT NULL,
                cantidad INT NOT NULL,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(query_tabla)
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Base de datos y tabla 'cajas' listas.")

    except Error as e:
        print(f"Error al inicializar la base de datos: {e}")

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except Error as e:
        print(f"Error de conexion a MySQL: {e}")
        return None

def insertar_caja(categoria, nombre_moneda, cantidad):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
            INSERT INTO cajas (categoria, nombre_moneda, cantidad)
            VALUES (%s, %s, %s);
            """
            cursor.execute(query, (categoria, nombre_moneda, cantidad))
            conexion.commit()
            return True
        except Error as e:
            print(f"Error al insertar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()
    return False

def listar_cajas_alfanumerico():
    conexion = obtener_conexion()
    registros = []
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            query = "SELECT * FROM cajas ORDER BY categoria ASC, nombre_moneda ASC;"
            cursor.execute(query)
            registros = cursor.fetchall()
        except Error as e:
            print(f"Error al consultar: {e}")
        finally:
            cursor.close()
            conexion.close()
    return registros

if __name__ == "__main__":
    inicializar_base_de_datos()
    conexion_test = obtener_conexion()
    if conexion_test and conexion_test.is_connected():
        print(f"Conexion exitosa a MySQL en localhost ({conexion_test.server_info})")
        conexion_test.close()
    else:
        print("No fue posible conectar.")
