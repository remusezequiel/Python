"""CONSIGNA:
    Escribir una función sum() y una función multip() 
    que sumen y multipliquen respectivamente todos los números de una lista. 
    Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) 
    debería devolver 24.
"""
# IMPORTS

import bucles as bl



# METHODS

def suma(numeros):
    """ Add a list of numbers

    Args:
        numeros (number): list of nombers

    Returns:
        number: add of numbers
    """    
    n = 0
    
    for numero in numeros:
        n = n + numero   
    
    return n

def multiplico(numbers):
    """ Add a list of numbers

    Args:
        numeros (number): list of nombers

    Returns:
        number: product of numbers
    """        
    n = 1
    
    for number in numbers:
        n = n * number   
    
    return n



# EXECUTION

if __name__ == "__main__":
    answer = ''

    while answer != 'n':
        cantidad = int(input("Ingrese la cantidad de numeros que tendra la lista: "))
        
        lista = bl.take_numbers(cantidad)
        
        bl.linea()
        print("Si los sumo: ", suma(lista))
        print("Si los multiplico: ", multiplico(lista))
        bl.linea()
       
        answer = input("¿Quiere seguir intentando? (s/n): ")
        bl.clear(15)

    bl.agradecimientos()