import psycopg2  # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1',   port='5432',database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # cierra el cursor con el "with"
            setencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores= (
                ('Juan Carlos', 'Roldan', 'rcarlos@gmail.com', 4) ,
                ('Romina', 'Ayala', 'Rayala@gmail.com', 8)
            )
            cursor.executemany(setencia, valores)  # De esta manera ejecutamos la setencia
            registros_actualizados = cursor.rowcount
            print(f'Los registros actulizados son {registros_actualizados}')


except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
     conexion.close()