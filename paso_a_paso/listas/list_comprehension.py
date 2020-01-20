list = []#False
for i in range(0, 101):
    list.append(i)

print(list)

print("-----------------------------------------------------")
#Creacion de la lista con comprehension
#list_comp = [valor a agregar a la lista for i in range(0,101)]
list_comp = [i for i in range(0,101)]
print(list_comp)

print("-----------------------------------------------------")
#Con restricciones
list_pares = [par for par in range(0,101) if par%2 == 0]
print(list_pares)

print("-----------------------------------------------------")
#Hago lo mismo pero con tuplas
tupla = tuple((par for par in range(0,101) if par%2 != 0))
print(tupla)

print("-----------------------------------------------------")
diccionario = {
                i:v for i, v in enumerate(list)
                if i % 2 == 0
            }
print(diccionario)
