""""
CONSIGNA:
---------
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
# IMPORTS
from ejercicio_5 import inversa
import bucles as bl



# METHODS
def es_palidromo(word):
    """This method takes a word 
    and analyzes if it is a palidrome.
    --> ! It don't work with sentences.

    Args:
        word (string): the word to be analised

    Returns:
        bool: If it is palidroma returns true
    """    
    inverse = inversa(word)
    if sentence == inverse:
        return True
    else:
        return False     

# Adisional 
def es_frase_palidroma(sentence):
    """This method takes a word 
    and analyzes if it is a palidrome.
    --> ! It don't work with sentences.

    Args:
        word (string): the word to be analised

    Returns:
        bool: If it is palidroma returns true
    """    
    inverse = inversa(sentence)
    inverse = bl.take_of_emptines(inverse)
    sentence = bl.take_of_emptines(sentence)

    if sentence == inverse:
        return True
    else:
        return False   

# EXECUTION

if __name__ == "__main__":
    answer = ''

    while answer != 'n':
        bl.linea()
        sentence = input("Ingrese una frase: \n --> ")
        bl.linea()

        print("La frase al inverso es: \n", inversa(sentence))
        print("¿Es palidroma?: \n", es_frase_palidroma(sentence))
        bl.linea()
        answer = input("¿Quiere seguir intentando? (s/n): ")
        bl.clear(15)

    bl.agradecimientos()