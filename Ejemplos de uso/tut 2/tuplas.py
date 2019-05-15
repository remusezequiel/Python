#Sintaxis de una tupla
tupla = ("Ezequiel", 3, 9, 1990)
print(tupla[0])
print(tupla[:])
#Convertir una lista a partir de una tupla
tup_lista=list(tupla)
print(tup_lista[:])

#Se puede hacer lo mismo al revez
lista = ["Maria",27,12,1984]
lis_tupla = tuple(lista)
print(lis_tupla)

#Para ber si algo esta en la tupla
print("Ezequiel" in   tupla)
print("Ezequiel" in lis_tupla)

#para saber cuantas veces esta el elemento "n" de la tupla
print(tupla.count(3)) #print(tupla.count( elemento "n"))

#Para conocer el total de elementos existentes en la tupla
print(len(tupla))

#Tuplas unitarias: si no ponemos una , al final no se reconose como tupla
unitariaTupla=("ezequiel",)
print(unitariaTupla)

#Empaquetado de una tupla
tupla_1 = "Maria",27,12,1984
#Desempaquetado de una tupla
nombre, dia, mes, anio = tupla_1
print(nombre)
print(dia)
print(mes)
print(anio)

#Buscar el indice dentro de la tupla
print("indice" + " " + str(tupla.index(1990)))
