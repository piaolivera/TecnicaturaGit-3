import psycopg2  # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1',   port='5432',database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # cierra el cursor con el "with"
            setencia = 'SELECT * FROM persona WHERE id_persona IN %s' #Placeholder
            entrada = input('Digite los id_persona a buscar(separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            cursor.execute(setencia, llaves_primarias)  # De esta manera ejecutamos la setencia
            registros = cursor.fetchall()  # Recuperamos todos los registros que serán una lista
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
     conexion.close()
#cursor.close() no hace falta debido a que lo cerramos con WITH
# https://www.psycopg.org/docs/usage.html

