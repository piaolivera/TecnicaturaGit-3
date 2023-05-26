import psycopg2  # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1',   port='5432',database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # cierra el cursor con el "with"
           setencia = 'DELETE FROM persona WHERE id_persona= IN %s'
           entrada = input("Digite lo números de registro a eliminar(separados por coma): ")
           valores =(entrada, ) #Es una tupla de valores
           cursor.execute(setencia, valores)  # De esta manera ejecutamos la setencia
           registros_eliminados = cursor.rowcount
           print(f'Los registros eliminados son {registros_eliminados}')


except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
     conexion.close()