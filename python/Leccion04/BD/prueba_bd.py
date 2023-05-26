import psycopg2  # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1',   port='5432',database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # cierra el cursor con el "with"
            setencia = 'SELECT * FROM persona WHERE id_persona= %s' #Placeholder
            id_persona = input('Digite un valor númerico para el id_persona: ')
            cursor.execute(setencia, (id_persona, ))  # De esta manera ejecutamos la setencia
            registros = cursor.fetchone()  # Recuperamos todos los registros que serán una lista
            print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
     conexion.close()
#cursor.close() no hace falta debido a que lo cerramos con WITH
# https://www.psycopg.org/docs/usage.html




