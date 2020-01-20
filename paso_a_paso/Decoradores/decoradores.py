"""
Los decoradores nos permite agregar funcionalidad
a las funciones en si.
"""
#A             #B
def decorador(func):
    def nueva_funcion():
        print("Ejecutamos la funcion")
        func()
        print("Se ejecuto la funcion")
    return nueva_funcion #C

@decorador
def saluda():
    print("Hola mundo")


#A,B, C sond Funciones
#A, recibe como parametro B para poder crear C
@decorador
def suma():
    print(10+20)
suma()

#Decorador para funciones con parametros
def deco_parametros(func):
    def funcion(*args,**kwargs):
        print("Ejecutamos la funcion que recive parametros")
        func(*args,**kwargs)
        print("Se ejecuto la funcion")
    return funcion #C

@deco_parametros
def suma_param(a,b):
    print(a+b)
suma_param(10,5)

"""
#Que pasa si la suma retorna un valor?
#los decoradores anteriores no funcarian.
#Un ejemplo de un decorador para que retorne un valor seria:
"""

def deco_return(func):
    def funcioncita(*args,**kwargs):
        print("Esta funcion va a tener un return")
        result = func(*args,**kwargs)
        print("En el paso anterior guarde el retorno en result")
        return result
    return funcioncita

@deco_return
def multi(a,b):
    return a*b

prod = multi(5,2)
print("Imprimo prod: ", prod)

"""
Los decoradores tambien pueden recibir parametros
si necesitamos que reciva otros parametros debemos hacer esto:
"""
def deco_con_parametros(is_valid):
    #
    def _deco_con_parametros(func):
        #
        def mensaje_uno():
            print("lalala")
        def mensaje_dos():
            print("lololo")
        def funcioncita(*args,**kwargs):
            if is_valid:
                mensaje_uno()
            else:
                result = func(*args,**kwargs)
                mensaje_dos()
                return result
        #
        return funcioncita
    return _deco_con_parametros

@deco_con_parametros(is_valid = True)
def resta(a,b):
    return a-b

resta = resta(5,2)
print("Imprimo esta: ", resta)

print("##########################################")

@deco_con_parametros(is_valid = False)
def resta(a,b):
    return a-b

resta = resta(5,2)
print("Imprimo resta: ", resta)
