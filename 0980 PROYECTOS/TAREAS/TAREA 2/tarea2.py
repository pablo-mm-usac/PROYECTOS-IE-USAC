import psycopg2 

#Conectar con la base de datos
dbname = 'proyectos'
host = 'localhost'
port = '5432'
user = 'postgres'
password = '202201199'

#Conexión a la base de datos
try:
    with psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn, conn.cursor() as cursor:




        # Insertar datos en la tabla 'redes'
        try:
            cursor.execute("INSERT INTO REDES (NOMBRE, CARNET) VALUES (%s, %s);", ("PABLO", 202201198))
            conn.commit()
            print("Registro insertado correctamente en la base de datos.")
        except Exception as e:
            print(f"Error durante la inserción en la base de datos: {e}")

except Exception as e:
    print(f"Error durante la conexión a la base de datos: {e}")
