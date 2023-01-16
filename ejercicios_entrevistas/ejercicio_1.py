"""
    CONSIGNA  :   Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
    --------      (Es cierto que python tiene una función max() incorporada, 
                    pero hacerla nosotros mismos es un muy buen ejercicio.)
"""

def max_dos(num_1, num_2):
    """Compara dos numeros. Devuelve el maximo de ambos, excepto cuando
        cuando son iguales

    Args:
        num_1 (number): Primer numero a comparar
        num_2 (number): Segundo numero a comparar

    Raises:
        Exception: Se muestra cuando ambos numeros son iguales

    Returns:
        number: El valor maximo entre los numeros comparados
    """    
    if num_1 > num_2:
        return num_1
    elif num_2>num_1:
        return num_2
    else:
        raise Exception("Los valores son iguales, por lo tanto no existe un valor maximo")

def programa():
    """ Toma la funcion max_dos para iterarla hasta que la perosna indique que no 
    """    
    answer = ''
    while answer != 'n':
        num_1 = float(input("Ingrese el primer numero: "))
        num_2 = float(input("Ingrese el segundo numero: "))

        maximo = max_dos(num_1, num_2)
        print("El valor maximo es: ", maximo, "\n", "---------")
        answer = input("¿Desea hacer otra prueba? (s/n): ")

if __name__ == "__main__":
    
    programa()
    print("\n------------------\n Gracias por\n usar\n el programa.\n------------------\n")
    
    


