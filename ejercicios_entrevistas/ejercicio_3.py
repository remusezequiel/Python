"""
CONSIGNA: Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
---------
"""

from bucles import linea, agradecimientos, clear

import os

def is_vocal(character):
    """This method take a letter and return True if the letter is a vocal

    Args:
        character (char): letter to decide

    Returns:
       bool: True if the letter is a vocal
    """    
    if character in ['a','e','i','o','u']:
        return True
    else:
        return False



if __name__ == "__main__":
    answer = ''

    while answer != 'n':
        linea()
        character = input("Ingrese una letra: ")
        print("--> ¿Es vocal? : ", is_vocal(character), "\n")
        linea()
        answer = input("¿Quiere ingresar otra letra? (s/n):  ")
        clear(20)

    agradecimientos()    