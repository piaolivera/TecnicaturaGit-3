import psycopg2  # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1',   port='5432',database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # cierra el cursor con el "with"
            setencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores= (
                ('Carlos', 'Lara', 'clara@gmail.com'),
                ('Marcos', 'Canto', 'mcanto@gmail.com'),
                ('Marcelo', 'Cuenca', 'cuenca@gmail.com')
            ) # Es una tupla de tuplas
            cursor.executemany(setencia, valores)  # De esta manera ejecutamos la setencia
            #conexion.commit() Esto se utiliza para guardar los cambios en la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son {registros_insertados}')


except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
     conexion.close()