#diccionario = {"clave":valor}, donde el valor puede ser de cualquier tipo.
#Las claves seran inmutables
dic = {
    'a': 55,
    'b': "Roberto",
     3 : 'Tres',
    }
print(dic)
#Los diccionarios pueden crecer o decrecer
dic['c'] = 'nuevo string'
dic['d'] = 2
print(dic)
#Modificar
dic['a'] = 48
print(dic)

#Obtener los datos desde un diccionario

valor = dic['b']
print(valor)

valor = dic.get('z', False)

#Eliminar

del dic['a']
print(dic)

#llaves
key = dic.keys()
print(key)
#valores
value = dic.value()
print(value)
#Listamos esto
list = list(key)
listt = list(value)
print(list)
print(listt)


#Extender diccionario a partir de otro diccionarios
