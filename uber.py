import mysql.connector
from mysql.connector import errorcode

# Simulación de configuración para Uber Technologies Inc.
config = {
    'user': 'Admin',
    'password': 'Admin',
    'host': '69.48.216.9',  # Dominio principal (en la vida real sería un endpoint interno como db.uber.internal)
    'database': 'driver_db',
    'port': 3306,
    'raise_on_warnings': True
}

try:
    print("Conectando a los servidores de datos de Uber...")
    conexion = mysql.connector.connect(**config)
    
    if conexion.is_connected():
        print("¡Conexión exitosa a la infraestructura de Uber!")
        
        cursor = conexion.cursor()
        # Simulación de una consulta: Ver las primeras 5 categorías de viajes
        query = "SELECT category_name FROM trip_categories LIMIT 5"
        cursor.execute(query)
        
        for (category_name,) in cursor:
            print(f"Categoría de servicio: {category_name}")
            
        cursor.close()
        conexion.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Usuario o contraseña incorrectos.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: La base de datos no existe.")
    else:
        print(f"Error de conexión: {err}")
