#Funcion para dejar un espacio en blanco
def enter():
	print(" ")

#funcion "yield" construye un objeto iterable con el primer valor almacenado. Es como el return pero iterable
"""Programa para generar numeros pares utilizando generadores"""
#usando funciones seria asi
"""
def genera_pares(limite):
	num=1
	miLista=[]
	while num<limite:
		miLista.append(num*2)
		num+=1

	return miLista

print(genera_pares(10))#va a generar 10 numeros pares

enter()
"""
def generador_pares(limite):
	num=1
	
	while num<limite:
		yield num*2
		num+=1

devuelvePares=generador_pares(10)
#for i in devuelvePares:
#	print(i)

#devuelveParesenter()

#Usando el metodo "next"	
print(next(devuelvePares))
print("Aqui podria haber mas codigo")

print(next(devuelvePares))
print("Aqui podria haber mas codigo")

print(next(devuelvePares))
