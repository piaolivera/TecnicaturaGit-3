#Declaramos una variable para abrir un archivo

try:                    #ecoding= para que nos permita colocar acentos
    archivo = open('prueba.txt', 'w', encoding='utf8') #metodo "open" , w = write que en inglés es escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras.\n')
    archivo.write('Como por ejemplo: acción, ejecución y producción\n')
    archivo.write(' las letras son:\n r= read=leer, \na = append= anexa, \nw = write=escribe ,\nx= para crear un archivo y si el archivo no existe envia un error')
    archivo.write('\nt esta es para texto o text, \nb archivos binarios, \w+ lee y escribe, son iguales  r+ \n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos')

except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() #con esto se debe cerrar el archivo
#archivo.write('Todo quedo perfecto') esto es un error !!! debido a que el archivo ya esta cerrado

