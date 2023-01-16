"""
CONSIGNA: Definir una función inversa() que calcule la inversión de una cadena. 
--------- Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

"""
# IMPORTS

import bucles as bl



# METHODS

def inversa(sentence):
    """This program take a sentence and write it backwards

    Args:
        frase (string): sentence to rewrite

    Returns:
        string: the inverse of the sentence
    """    
    size = len(sentence)
    counter = size
    new_sentence = ""

    while counter != 0:
        new_sentence = new_sentence + sentence[counter-1:counter]
        counter -= 1        
        
    return new_sentence


# EXECUTION

if __name__ == "__main__":
    answer = ''

    while answer != 'n':
        bl.linea()
        sentence = input("Ingrese una frase: \n --> ")
        bl.linea()

        print("La frase al inverso es: \n", inversa(sentence))
        
        bl.linea()
        answer = input("¿Quiere seguir intentando? (s/n): ")
        bl.clear(15)

    bl.agradecimientos()