list = ["string", 15, 3.14, True]
print(list)

#LAs listas pueden crecer o decrecer
list.append(6)
#Append coloca el caracter pasado en la ultima posicion de la lista
print(list)

#tambien tenemos el metodo insert el cual nos permite insertar un
#nuevo elemento a la lista en el indice que queramos
list.insert(1, "insert")
print(list)

#podemos eliminar alguna cosa de la listas
list.remove(15) #VA a eliminar los 15 que alla en la lista
print(list)

#El metodo pop nos sirve para obtener el ultimo elemento de la lista
pop = list.pop()
print(pop)

"""
Si tenemos una lista de numeros, podemos ordenarla mediante el metodo sort
"""
#Dada una lista desordenada
number_list = [9,7,8,6,4,5,3,2,1]
print(number_list)
#organizo
number_list.sort()
print(number_list)

#organizada en reversa
number_list.sort(reverse=True)
print(number_list)

"""
Podemos unir listas como si de conjuntos se tratasen
"""
conj_1 = [1,2,3]
print(conj_1)
conj_2 = [4,5,6]
print(conj_2)
#Aca lo que decimos basicamente es (A U B)
conj_1.extend(conj_2)
print(conj_1)
