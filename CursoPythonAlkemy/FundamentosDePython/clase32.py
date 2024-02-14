# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:19:16 2024

@author: Hp
"""
"""
#    COLECCIONES DE DATOS
#...........
# Listas [elementos]

dias_semana = ["Lunes", "Martes", "Miercoles", 
               "Jueves", "Viernes", "Sabado", "Domingo"]

print(dias_semana)

for dia in dias_semana:
    print(dia)
#...........    
# Metodos de listas
"""
#    append(): Agrega un elemento al final de la lista (si no elijo un
#              posicion)
"""    
dias_semana.append("Osvaldo")

"""
#    extend(): extiende en base a una lista pasada como parametro
"""
meses = ["Enero", "Febrero"]
dias_semana.extend(meses)

"""
#    insert(): es como append pero primero le tenemos que pasar el 
#              indice donde se quiere meter 
"""
meses.insert(2, "Marzo")

"""
#pop(): elimina un elemento pasado como parametro.
#        Si no le pasas parametro elimina el ultimo
"""
dias_semana.pop()

"""
#    sort
"""
numeros = [9,3,8,2,7,4]
numeros.sort()
"""
#reverse()
"""
numeros.reverse()

#...........
# TUPLAS: Como las listas pero son inmutables
#...........
"""
#    Methods: Count, index
"""
preposiciones=("A", "Ante", "Bajo", "Con")
print(preposiciones.count("Ante"))
print(preposiciones.index("Ante"))

#...........
# Diccionarios: Colecciones key/Value. Se utilizan para crear objetos/entidades
#...........
persona = {
    "Nombre":"Juan",
    "Apellido":"Gommez",
    "Edad": 23,
    "PromNotas": [9,4,8],
    "es_estudiante": False
    }

print(persona["Nombre"])
print(persona.get("Nombre"))
print(persona.keys())
print(persona.values())
print(persona.items())

persona.pop("PromNotas")
print(persona.items())
persona.clear()
print(persona.items())
"""

#...........
# FUNCIONES
#...........

def sumar_iva(precio):
    return precio*1.21

res_1 = sumar_iva(200)
res_2 = sumar_iva(450)

print(res_1)
print(res_2)













