"""
Los modulos son archivos .py los cuales van a poder ser utilizados
dentro de otro archivos

Primero debemos tener preparados los archivos

por lo general tenemos un archivo main.py que es donde vamos a llamar
 al modulo que ya tiene codigo hecho utilizable
 En este archivo vamos a usar unos modulos sencillos
"""
#Tenemos varias formas de llamar modulos, dependiendo de
#su ubicacion y de como lo vamos a usar

import resta
from suma import suma as s


resultado = resta.resta(10,2,3)# |5|
print(resultado)
resultado = resta.resta(10,2,3,5,1)#10-2 = 8-3 = 5-5 = 0-1 = |-1|
print(resultado)
resultado = resta.resta(10,10,2)#10-10= 0-2 = |-2|
print(resultado)
resultado = resta.resta(1,2,3)#1-2= -1-3 = |-4|
print(resultado)
resultado = resta.resta(10,2,3)# |5|
print(resultado)
resultado = resta.resta(10,2,3,5)# |5|
print(resultado)

resultado = s(10,2,3,5)# |20|
print(resultado)
