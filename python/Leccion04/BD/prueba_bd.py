import  psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

cursor = conexion.cursor()
setencia= 'SELECT * FROM persona'
cursor.execute(setencia) #De esta manera ejecutamos la setencia
registros= cursor.fetchall()# Recuperamos todos los registros que serán una lista

print(registros)

cursor.close()
conexion.close()
