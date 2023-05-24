archivo = open('prueba.txt', 'r',encoding='utf8') #read= para leer , a= para agregar mas información
#print(archivo.read())         # las letras son: 'r'= read, 'a'=append, 'w'=write,'x'= para crear un archivo y si el archivo no existe envia un error

#print(archivo.read(16))
#print(archivo(10)) #Continuamos desde la linea anterior
#print(archivo.readline()) #Nos lee la  linea completa

#vamos a iterar el archivo, cada una de las lineas
#for linea in archivo:
   # print(linea)  iteramos todos los elementos del archivo
#print(archivo.readlines()) #nos muestra en pantalla como si fuera una lista

#Anexamos información , copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() #Cerramos el primer archivo
archivo2.close() #cerramos el segundo archivo


print('Se ha terminado el proceso de leer y copiar archivos')
