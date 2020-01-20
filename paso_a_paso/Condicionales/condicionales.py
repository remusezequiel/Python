fruta = 'kiwi'

"""
if condicion:
    codigo
else:
    codigo
"""
if fruta == 'kiwi':
    print(fruta)
else:
    print("La fruta no es kiwi")

def es_kiwi(fruta):
    if fruta == 'kiwi':
        return 'La fruta es un {}'.format(fruta)
    else:
        return 'La fruta es un/a {}, no un kiwi'.format(fruta)

fun = es_kiwi("banana")
print(fun)

#> | < | <= | >= | != | ==

if True:
    print("Es verdadero")
else:
    print("Es falso")

#Las listas vacias representan falso
if []:
    print("Es verdadero")
else:
    print("Es falso")

#Las listas vacias representan falso
if [0]:
    print("Es verdadero")
else:
    print("Es falso")


#Un uno es verdadeo y el cero es falso
if 1:
    print("Es verdadero")
else:
    print("Es falso")

if 0:
    print("Es verdadero")
else:
    print("Es falso")



#La palabra reservada None le dice a python que la variable no tiene valor
#En particular un None es un valor falso al igual que cualquier cosa vacias
valor = None
if valor:
    print("Es verdadero")
else:
    print("Es falso")


#Uso de and:
"""
Tabla de verdad del and:
p | q | p and q
1 | 1 |    1
1 | 0 |    0
0 | 1 |    0
0 | 0 |    0
"""
valor = 1
valor_dos = 40
if (valor) and (valor_dos > 20):
    print("Es verdadero")
else:
    print("Es falso")
