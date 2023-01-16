'''
CONSIGNA: 
---------  Definir un histograma procedimiento() que tome una lista de 
        números enteros e imprima un histograma en la pantalla. 
            Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
            
        ****
        *********
        *******
            
'''
# IMPORTS
import bucles as bl

# METHODS
def histograma_procedimiento(lista):
    """It print an * per unit in every element in list

    Args:
        lista (list): Info for the histogram
    """    
    for i in lista:
        print("*" * int(i))
    

# EXECUTION
if __name__ == "__main__":
    answer = ''

    while answer != 'n':

        size = int(input("Cantidad de Elementos de la lista: "))
        list_1 = bl.ingresa_lista(size)
        histograma_procedimiento(list_1)
        
        answer = input("¿Quiere seguir intentando? (s/n): ")
        bl.clear(15)

    bl.agradecimientos()

