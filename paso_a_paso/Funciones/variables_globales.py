"""
Variables locales:
    Existen solo en el contexto de la funcion.
    No pueden modificar a las variables que esten fuera de la funcion.
    Una variable local no puede afectar a una variable global

Variables Globales:
    las variables globales ecisten en cualquier contexto.
    Al ser pasadas como parametro de una funcion modificara a las
    variables locales dentro de la funcion para obtener un nuevo retorno.
    No podemos modificar valores globales dentro de una funcion
"""
def palidromo(frase):
    frase = frase.replace(' ','')
    print(frase)
    return frase == frase[::1]


sentencia = 'anita lava la tina'
print(sentencia)
resultado = palidromo(sentencia)
print(sentencia)
print(resultado)

#Nueva funcioan palidromo:
def new_palidromo():
    new_value = sentencia.replace(' ','')
    return new_value == frase[::1]

sentencia = 'anita lava la tina'
print(sentencia)
resultado = palidromo(sentencia)
print(sentencia)
print(resultado)


#Ejemplo de funcionamiento de una variable global:
def var_global():
    variable_global = 'Cambiar Variable'

variable_global = 'Esto es una variable global'
print(variable_global)
var_global()
print(variable_global)

#Como vez, el llamado de la funcion no modifica el valor de la variables
#Sin en bargo, podemos modificar los valores usando la funcion global dentro de la funcion

def new_var_global():
    global variable_global
    variable_global = 'Ahora si la cambia'

variable_global = 'Esto es una variable global'
print(variable_global)
new_var_global()
print(variable_global)


#Como hago una funcion que cree nuevas funciones globales?

def crear_global():
    global nueva_variable
    nueva_variable = 'Esto es una variable global'

crear_global()
print(nueva_variable)
