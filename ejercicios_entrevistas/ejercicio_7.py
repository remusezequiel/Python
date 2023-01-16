"""CONSIGNA:      Definir una función superposicion() que tome dos listas y 
   ---------    devuelva True si tienen al menos 1 miembro en común o devuelva 
                False de lo contrario. 
                  Escribir la función usando el bucle for anidado.
"""
# IMPORTS
import bucles as bl



# METHODS
def superposicion(lista_1, lista_2):
    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                return True
    return False

def pedir_lista():
    size = bl.ingresa("¿De que tamaño seran la lista? \n") 
    bl.linea()
    lista = bl.ingresa_lista(int(size))
    bl.linea()
    return lista

# EXECUTION

if __name__ == "__main__":
    answer = ''

    while answer != 'n':

        print(" ** Primer Lista: ** ")
        lista_1 = pedir_lista()
        print(" ** Segunda Lista: ** ")
        lista_2 = pedir_lista()
        
        bl.linea()
        print("Las listas ingresadas son")
        print("--> ", lista_1)
        print("--> ", lista_2)
        bl.linea()

        print("Comparando ...")
        respuesta = superposicion(lista_1, lista_2)
        print("Terminado!\n")
        
        bl.linea()
        print("¿Tienen al menos un elemento en comun? \n --> ", respuesta)
        bl.linea()
        
        answer = input("¿Quiere seguir intentando? (s/n): ")
        bl.clear(15)

    bl.agradecimientos()