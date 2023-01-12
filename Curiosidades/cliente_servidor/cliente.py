#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
El inicio del archivo es igual. Importamos las utilidades necesarias e
inicializamos las variables con los parametros para la conexion
"""

#Importaciones
#Utilidades de red y conexion
import socket

#declaracion de las variables

ip_server = "0.0.0.0"#Es lo mismo que localhost o 0.0.0.0
puerto_servidor = 9999

"""
Creamos de nuevo el socket pero en vez de ponerlo en escucha, lo conectamos
con el servidor cuyos parametros estan indicados en las variables.
"""

#Configuramos los datos para conectarnos con el servidor
#socket.AF_INET para indicar que utilizamos IPv4y
#socket.SOCK_STREM para utilizar TCP/IP (no udp)
#Todos los protocolos deben ser los mismos que en el servidor

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip_server, puerto_servidor))
print("Conectado con el servidor %s %s" %(ip_server,puerto_servidor))

"""
Finalmente indicamos lo que queremos hacer con la coneccion.
En este caso tambien lo haremos en bucle. Ya que la forma de funcionamiento
que elegi para el ejemplo es que el cliente mande un mensaje al servidor y el
servidor le responda "Recibido". Cuando el cliente reciba el mensaje de Recibido
volvera a perdir un mensaje al usuario para poder mandarlo de nuevo al servidor
y asi infinitamente. Para cerrar la conxion el usuario debe escribir en el
cliente "exit" y mandar ese mensaje al servidor.
Al llegar al servidor, este enviara el mensaje exit al cliente y mostrara un
mensaje de Coneccion cerrada y cerrara la coneccion
"""

while True:
    msg = input("> ")
    cliente.send(msg.encode())
    respuesta = cliente.recv(4096)
    print(respuesta)
    if respuesta == "exit".encode():
        break

print("----CONEXION CERRADA----")
cliente.close()
