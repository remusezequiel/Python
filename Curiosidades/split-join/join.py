"""
#Consideremos la siguiente lista:
"""

paises = ['Argentina', 'Uruguay', 'Chile', 'Paraguay']

"""
Si deseamos convertir esta lista en una cadena de caracteres, utilizamos
la funcion "join" de la siguiente forma:
"""

#'separador'.join(lista)
new_paises = ','.join(paises)
print(new_paises)

"""
Probemos con varios separadores, para ver como quedan
"""
new_paises = ''.join(paises)
print(new_paises)

new_paises = ' '.join(paises)
print(new_paises)

new_paises = '='.join(paises)
print(new_paises)

new_paises = '/'.join(paises)
print(new_paises)

"""
Por ejemplo, imaginemos que tenemos una serie de caracteres los cuales
representan numeros en una lista. Cada valor nos determina una serie de
acciones realizadas o no realizadas, por lo que esto seran unos numeros
binarios y necesitamos unirlos para conocer que numero decimal representan
a partir de una funcion que resivira un string. Entonces, tenemos el siguiente
numero:
"""

binario = ['1','1','0','1','0','0']
#lo unimos
new_binario = ''.join(binario)
print(new_binario)
