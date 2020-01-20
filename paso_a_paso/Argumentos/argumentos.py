"""
Imaginate que necesitas hacer una funcion que a priori no sabes cual
es la cantidad de parametros que queres pasarle.

Por ejemplo, como hago una funcion que me sume una cantidad x de numeros pasados
por parametros y este x no sea un valor fijo....

Bueno, para esto podemos hacer lo siguiente:
"""
def impresion_multiples_parametros(*param):
    print(param)
    print(type(param))

res = impresion_multiples_parametros(1,2,3,4,5,6,7,8)

print("######################################################")
#De esta forma puedo crear la funcion suma de arriba de esta forma
def suma(*sumame):
    result = 0
    for i in sumame:
        result = result + i
    return result

s = suma(1,2,3,4,5,6,7)
print(s)
print("######################################################")
"""
Por convencion a *sumame que representa una cantidad x de parametros se le
da el nombre de *args el cual siempre sera una tupla.

Existe otra convencion que se llama **kwargs en el cual los argumentos
estaran guardados en diccionarios. Como es un diccionario, es necesario
pasarle la clave y el valor.
"""
def lala(**kwargs):
    print(kwargs)

res = lala(caca = "Mucha", valor = 'De mierda', dos = 3)

print("######################################################")
def obtengo_valor(**kwargs):
    valor = kwargs.get('valor', 'no contiene valor')
    print(valor)

res = obtengo_valor(caca = "Mucha", valor = 'De mierda', dos = 3)
"""
*  -> n valores -> tuplas
** -> n valores -> diccionario
"""
