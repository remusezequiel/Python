""" CONSIGNA : Definir una función generar_n_caracteres() 
                que tome un entero n y devuelva el caracter multiplicado por n. 
                 Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
# IMPORTS
import bucles as bl

# METHODS

def generar_n_caracteres(size, character):
    """Takes an integer and a character. 
    Returns the character multiplied by that number

    Args:
        size (number): Number of times to write the character
        character (char): Character to write

    Returns:
        string: the multiplied character
    """    
    new_character = ""
    for i in range(size):
        new_character = new_character + character
    return new_character

# EXECUTION

if __name__ == "__main__":
    answer = ''

    while answer != 'n':

        size = int(input("Cantidad de caracteres: "))
        character = input("Caracter a repetir: ")
        
        print("El string final es: ", generar_n_caracteres(size, character))

        
        answer = input("¿Quiere seguir intentando? (s/n): ")
        bl.clear(15)

    bl.agradecimientos()


