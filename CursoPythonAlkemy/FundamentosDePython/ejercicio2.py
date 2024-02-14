"""
Crear una lista de 5 elementos y luego aplica los siguientes accionables:
    -> Imprimir el ultimo elemento
    -> Modificar el valor del tercer elemento
    -> Agregar dos elementos
    -> Eliminar algún elemento
"""

mi_lista = ["elem_0", "elem_1", "elem_2", "elem_3", "elem_4"]

# Muestro el ultimo elemento
print(mi_lista[4])

# Modificar el valor del tercer elemento
mi_lista[2] = "new_elem_2"

# Agrego dos elementos
mi_lista.append("elem_5")
mi_lista.append("elem_6")
print(mi_lista)

# Elimino el ultimo elemento que agregue
del(mi_lista[len(mi_lista)-1])
print(mi_lista)