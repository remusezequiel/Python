#!/usr/bin/python3
#-*- coding: utf-8 -*-

#Correr primero en la terminal el comando: lsof -i -n

"""
Ejemplo Cliente-servidor en python
Programa servidor
"""

#Importaciones

#Utilidades de red y conexion
import socket

#Definimos parametros necesarios por defecto
ip = "0.0.0.0"
puerto = 9999
data_conection = (ip, puerto)
#Se podran conectar 5 clientes como maximo
max_conections = 5

"""
Creamos el servidor. Realmente es un objeto de tipo socket que esta a la escucha
Le indicamos que utilice IPv4y TCP/IP. Podriamos tambien utilizar UDP o IPv6
"""
#socket.AF_INET para indicar que utilizamos IPv4y
#socket.SOCK_STREM para utilizar TCP/IP (no udp)

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Asignamos los valores del socket_servidor
socket_servidor.bind(data_conection)

#ASignamos el numero maximo de conecciones
socket_servidor.listen(max_conections)

"""
Nuestro socket ya esta creado, ahora falta ponerlo en escucha
"""

print("Esperando conexiones en %s %s" %(ip, puerto))
cliente, direccion = socket_servidor.accept()
print("Conexion establecida con %s %s" %(direccion[0], direccion[1]))

"""
El metodo socket.accept() permanecera a la escucha hasta recibir cualquier
peticion. Despues, en bucle indicamos lo que el servidor debe hacer al recibir
cada conexion
"""

#Bucle de escucha. En el indicamos la forma de actuar al recibir las tramas
#del Cliente
while True:
    datos = cliente.recv(1024)#Int = numero maximo de bytes
    if datos == "exit".encode():
        print("Vas a salir del server")
        cliente.send("exit".encode())
        break
    print("Recibido %s" %datos)
    cliente.sendall("--Recibido--".encode())

print("----CONEXION CERRADA----")
socket_servidor.close()
