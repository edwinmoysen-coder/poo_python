
import mysql.connector

# Datos de simulación para El Puerto de Liverpool
# El host se pone sin 'https://'
config = {
    "host": "elpuertodeliverpool.mx",
    "user": "Admin",
    "password": "Admin",
    "database": "liverpool_db_produccion",
    "port": 3306  # El puerto estándar de MySQL
}

try:
    print("Intentando conectar con el servidor de Liverpool...")
    conexion = mysql.connector.connect(**config)
    
    if conexion.is_connected():
        print("¡Conexión establecida con éxito!")
        cursor = conexion.cursor()
        
        # Ejemplo: Consultar versión del servidor
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Versión del servidor: {version}")
        
        conexion.close()
        
except mysql.connector.Error as err:
    print(f"No se pudo conectar. Error: {err}")
