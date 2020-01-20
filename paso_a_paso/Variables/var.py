"""
Una variable es un espacio en la memoria ram que va a almacenar datos de un
cierto tipo. Tenemos que notar que las variables al alojarce en la memoria ram
solo pueden usarse cuando el programa esta en ejecucion, luego estos lugares
que son guardados por la ram se limpian, se pierden.

Podemos almacenar:

 -> Caracteres : 'c'
 -> Cadenas de Caracteres : "Cadenas"
 -> Numeros : 8, 8.9
 -> Bools: True, False
"""

#En la variable curso se guarda el valor ""Python 3""
#Por conversion las variables en python se notan en minusculas
curso = "Python 3"
#Si necesitamos mas palabras en la variables se realiza con un guion bajo
curso_matematicas = "Derivadas"

#Imprimimos en consola
"""
Lo que hacemos aca es pasarle el valor de la variable a la funcion
print la cual imprime en pantalla el valor de la variable
"""
print(curso)
print(curso_matematicas)
"""
    Otra forma de imprimir un texto mas personalizado seria algo asi:
"""
print("Estas en el curso de ", curso)
print("Los cursos existentes son: \n\t{} \n\t{}".format(curso,curso_matematicas))

"""
Como dijimos, las variables se almacenan en ram, lo cual hace que se permita su redefinicion
por ejemplo podemos definir la variable "numero" que almacenara un numero (int o float)
y despues a este sumarle un valor sobre la misma variable, lo cual en tiempo de ejecucion podra
 cambiarse dicho valor. Veamos esto:
"""

numero = 3
print(numero)
numero = numero + 1
print(numero)
numero = numero - 2
print(numero)

impuesto = 12.5 / 100
precio = 100.50
pi = precio * impuesto
print(pi)
ppi = precio + pi
print(ppi)
r = round(ppi,2)
print(r)
