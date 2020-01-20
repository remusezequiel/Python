#Permite iterar objetos iterables, ejemplo tuplas, diccionarios, listas y strings

list = [0,1,2,3,4,5,6,7,8,9]

#Iteracion de los elementos de la lista
for i in list:
    print(i)

print("----------------------------------")
new_range = range(0,10)
for i in new_range:
    print(i)

print("----------------------------------")
new_range = range(0,10,2)#con salto de 2 en 2
for i in new_range:
    print(i)

print("----------------------------------")
new_range = range(10,33,3)#con salto de 2 en 2
for i in new_range:
    print(i)

print("----------------------------------")
indice = 0
for i in list:
    print(i, "tiene el indice", indice)
    indice+=1

print('Lo cual es lo mismo que lo siguiente:')

for indice, i in enumerate(list):
    print(i, "tiene el indice", indice)

print('Que pasa si los pasamos al reves:')

for i,indice in enumerate(list):
    print(i, "tiene el indice", indice)

print("----------------------------------")
#Trabajar con respecto al trabajo de la lista
for valor in range(len(list)):
    print(valor,"- Hola")
print("----------------------------------")
#Los strings son iterables
for valor in "Caca":
    print(valor,"- Hola")
#Tambien podemos iterar diccionarios
dictionary = {'a': 1, 'b':2, 'c':3, 'd':4}
for key, value in dictionary.items():
    print('La llave es: ', key, ' y el valor es: ', value)
