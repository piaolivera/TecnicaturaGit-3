import psycopg2 as bd  # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1',   port='5432',database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            setencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'alexx@gmail.com')
            cursor.execute(setencia, valores)

            setencia = 'UPDATE persona SET nombre =%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Roldan', 'jcroldan@gmail.com', 1)
            cursor.execute(setencia,valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo un rollback {e}')
finally:
     conexion.close()

print('Termina la transacción')