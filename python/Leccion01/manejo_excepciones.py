from NumerosIgualesExpetion import NumerosIgualesException

resultado =None
#a = 7 #Podemos pedir las variables dentro del try y que sean ingresadas por el usuario
#b= 0
try:
    a= int(input("Digite el primer valor: "))
    b= int(input("Digite el segundo valor: "))
    if a == b:
        raise NumerosIgualesException('Son números iguales') #Atra ves de raise llamamos a nuestra clase exception
    resultado= a/b
except TypeError as e:
    print(f'TypeError- Ocurrio un error{type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError- Ocurrio un error: {type(e)}')
except Exception as e:
    print (f'Exception- Ocurrió un error: {type(e)}')
else:
    print("No se encontro ninguna excepción")
finally:
    print("Ejecucion de este bloque finally")

print (f'El resultado es: {resultado}')
print ('Seguimos ...')



