"""
poo: paradigma de programacion

objeto: entidades como lapiz, borrador,... cualquier cosa que tenga caracteristicas definidas
y que pueden realizar una cierta cantidad de acciones utilizando sus caracteristicas propias

EN PYTHON TODO ES UN OBJETO
"""
#Para las clases la convencion es CamelCase y no con guiones bajo como las variables
class Lapiz():
    #Atributos
    color = 'Amarillo'
    contiene_borrador = True
    usa_grafito = True

#Creo el OBJETO
lapiz_generico = Lapiz()
print(lapiz_generico.color)
print(lapiz_generico.contiene_borrador)
print(lapiz_generico.usa_grafito)
