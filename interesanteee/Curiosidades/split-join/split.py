"""
Consideremos la siguiente Cadena:
"""

cadena = "Mi nombre es Ezequiel"

"""
Al utilizar la funcion split, podemos separar palabra por palabra de dicha
cadena de la siguiente forma:
"""
 lista_de_la_cadena = cadena.split()
 print(lista_de_la_cadena)

 """
Asi como en join, tambien podemos identificar un separador para split.
Si en la cadena de texto deseamos convertir a lista las palabras estuvieran
separadas por un salto de linea, como por ejemplo.
 """

cadena = ''' Fulano
Mengano
suntano'''
lista_de_la_cadena = cadena.split(sep='\n')


"""
Nos interesa convertir strings en listas y viceversa por que los strings
son inmutables, mientras las listas son mutables. Es decir, en una lista podemos
modificar un elemento de la misma mientras que en un string no es posible
hacerlo directamente.

Mas info:

docs.python.org/3.6/library/stdtypes.html#str.split
docs.python.org/3.6/library/stdtypes.html#str.join
"""
