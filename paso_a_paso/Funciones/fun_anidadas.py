"""
Forma no anidada
"""
##########################################
def validacion(num_uno, num_dos):
    return num_uno > 0 and num_dos > 0
##########################################

##########################################
def division(num_uno, num_dos):
    if validacion(num_uno, num_dos):
        return num_uno / num_dos
##########################################

"""
Forma anidada
"""
##########################################
def division_anidada(num_uno, num_dos):
    #Las variables de division anidada son variables utilizables
    # dentro de las anidadas como si fuesen globales dentro de la funcion
    def validacion_ani():
        return num_uno > 0 and num_dos > 0

    if validacion_ani():
        return num_uno / num_dos
##########################################

"""
Funciones Clousure: Son basicamente funciones que crean funciones
"""
##########################################
def crear_funcion(num_uno,num_dos):
    def validacion():
        return num_uno>0 and num_dos>0
    return validacion
##########################################

"""
Funciones que reciven otras funciones como parametros
"""
##########################################
def aplicar_funcion(func):
    result = func()#V o F
    print(result)
##########################################

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#A partir de aca se ejecutara el programa.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print("Forma no anidada")
resultado = division(10,5)
print(resultado)

print("Forma anidada")
resultado = division_anidada(10,5)
print(resultado)

print("Funciones Clousure")
nueva_funcion = crear_funcion(10,5)
print(nueva_funcion())

print("Funciones aplicadas como parametros")
"""A aplicar_funcion se la pasa la funcion crear_funcion
la cual crea sibre la variable local result de aplicar_funcion
una nueva funcion. En particular, como los parametros de
crear_funcion pasan primero por la validacion este devolvera true
si cumplen con los requicitos de la validacion y si no devolvera
false"""
print("Llamado de aplicar_funcion de crear_funcion(10,5):")
aplicar_funcion(crear_funcion(10,5))
print("Llamado de aplicar_funcion de crear_funcion(10,0):")
aplicar_funcion(crear_funcion(10,0))
