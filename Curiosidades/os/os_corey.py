"""
Este archivo muestra el uso de llas diferentes funciones y posibles usos
de la libreria os

Enlace: www.youtube.com/watch?v=tJxcKyFMTGo
"""


import os
from datetime import datetime

#Muestro todo lo que tiene este modulo
print(dir(os))

#Muestro el directorio sobre el cual esta parado dicho archivo
print(os.getcwd())

#Cambio de directorio
os.chdir('/home/ezequiel/Escritorio')

#Vuelvo a mostrar el directorio sobre el cual esta parado dicho archivo
print(os.getcwd())

print(os.listdir())

#Crear un directorio
os.mkdir('creado_con_python')

#Me meto en el directorio que cree
os.chdir('/home/ezequiel/Escritorio/creado_con_python')

#Creo un directorio con un subdirectorio
os.makedirs('creo_subdirectorio/creo_sub_subdirectorio')

#Vuelvo al directorio anterior
os.chdir('/home/ezequiel/Escritorio/creado_con_python')

#Borro los dos directorio que cree
os.removedirs('creo_subdirectorio/creo_sub_subdirectorio')

#Voy para atras
os.chdir('/home/ezequiel/Escritorio')

#borro el primer directorio que cree
os.rmdir('/home/ezequiel/Escritorio/creado_con_python')

################################################################################
#                   Para el manejo de archivos                                 #
################################################################################

"""
file = open('/home/ezequiel/Escritorio/cambio.txt', "w")
file.write("Primer Linea" + os.linesep)
file.write("Segunda Linea")
file.close()

#os.rename('cambio.txt', 'txt_con_python.txt')
os.rename('txt_con_python.txt', 'cambio.txt')

#Fijate que podes hasta crear un archivo python usando python
file = open('/home/ezequiel/Escritorio/python.py', "w")
file.write("print('Hola como estas?')" + os.linesep)
file.write("print(3.14 * 5)")
file.close()
"""
#Funcion stat
print(os.stat('cambio.txt'))

print(os.stat('cambio.txt').st_size)

print(os.stat('cambio.txt').st_mtime)

mod_time = os.stat('cambio.txt').st_mtime

print(datetime.fromtimestamp(mod_time))


#Caminar sobre directorios
for dirpath, dirnames, filenames in os.walk('/home/ezequiel/Escritorio/Libros'):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()



print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'cambio.txt')

print(file_path)


print(os.path.exist('/tmp/test.txt'))
print(os.path.exist('/home/ezequiel/Escritorio/Libros'))
