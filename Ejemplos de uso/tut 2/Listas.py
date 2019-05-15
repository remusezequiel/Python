lista = ["Maria", "Pepe", "Marta", "Antonio"]

#Imprimo toda la lista
print(lista[:])

#Imprimo el elemento ubicado en el lugar 2 de la lista sabiendo que empieza contando desde 0
print(lista[2])

#Acceso a una porcion de lista
print(lista[0:2])#Desde cero hasta 2 exclusivo, es decir excluye del 2 emn adelante
print(lista[1:3])#Escribe Pepe y Marta
print(lista[2:])#Estcribe desde en dos hasta que termine la lista


#Agregado de un elemento a la lista
lista.append("Sandra")#se agrega al final de la lista
print(lista[:])

#Otra forma es agregar el elemento en un lugar que queremos
lista.insert(2,"Ramon")
print(lista[:])

#Concatenar otra lista:
lista.extend(["extend_1","extend_2","extend_3"])
print(lista[:])

#SI quiero saber el indice:
print(lista.index("Pepe"))
#Para buscar un elemonto en la lista:
print("lola" in lista)
print("Pepe" in lista)

#Para eliminar un elemento:
lista.remove("extend_1")
print(lista[:])

#Para eliminar el ultimo elemento de la lista:
lista.pop()

#Se pueden sumar listas

lista_1=[1,2,3]
lista_2=[4,5,6]
print(lista_1+lista_2)


#Para unir dos listas diferentes:

lista_3 = ["Maria","jose"]
lista_4 = [1,6,8]
lista_5 = lista_3+lista_4
print(lista_5[:])

#Repetidor de listas:
lista_6 = ["lola", 6, 'c'] * 3
print(lista_6[:])

















