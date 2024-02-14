# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:30:20 2024

@author: Ezequiel Remus
"""

"""
Consigna:
        Crear un pequeño programa que realice una función aritmética 
        que permita al usuario ingresar datos por la terminal acorde 
        a distintas opciones.  Para ellos debemos definir una función 
        que reciba parámetros:
            Combinar funciones nativas y funciones definidas,
            condicionales, y bucles.
   
    Si el usuario ingresa el nro 1, realiza la acción A.
    Si el usuario ingresa el nro 2, realiza la acción B.
"""


# FUNCION
def aritmetica_func(num_1, num_2, selector):
    if selector == 1:
        return num_1 + num_2
    elif selector == 2:
        return num_1 - num_2
    else:
        return "Error: Las opciones posibles son 1 y 2."

# EJECUCIÓN

if __name__ == "__main__":
    
    respuesta = "s"    
    
    while respuesta == "s":
        num_1 = float(input("Ingrese el primer numero: "))
        num_2 = float(input("Ingrese el segundo numero: "))
        selector = int(input("Ingrese el selector (numero entero 1o 2): "))               
        print(aritmetica_func(num_1,num_2,selector))
        respuesta = str(input("Desea seguir intentando? (s=Si/n=No) "))
   
    print("¡Gracias por usar el programa!")
 