"""
    Consigna: Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
    --------- 
"""
import bucles as bl

def max_de_tres(n_1,n_2, n_3):
    """This method takes three numbers and return de max number between them. 
    
    Args:
        n_1 (number): number to compare
        n_2 (number): number to compare
        n_3 (number): number to compare

    Raises:
        Exception: _description_

    Returns:
        number: The maximun of all numbers
    """   
    if n_1>n_2 and n_1>n_3:
        return n_1
    elif n_2>n_1 and n_2>n_3:
        return n_2   
    elif n_3>n_1 and n_3>n_2:
        return n_2   
    else:
        raise Exception("Los tres numeros son iguales")


def program():
    """ 
    This program asks for 3 numbers. 
    Then it compares them and asks if you want to iterate the process again
    """    
    answer = ''
    while answer != 'n':
        numbers = bl.take_numbers(3)
        max_number = max_de_tres(numbers[0], numbers[1], numbers[2])
        print("\nEl maximo numero es: ", max_number, "\n")
        answer = input("¿Quiere seguir intentando? (s/n): ")

# Execution
if __name__ == "__main__":
    program()
    print("\n------------------\n Gracias por\n usar\n el programa.\n------------------\n")