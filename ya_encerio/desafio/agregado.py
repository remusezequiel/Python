######################################################
def convertir_a_binario(entero):
	lista = []

	while entero > 1:
		resto = entero % 2
		lista.append(resto)
		entero = entero // 2
	lista.append(entero)

	lista_inversa = lista[::-1]	
	return lista_inversa
######################################################

######################################################
def unir(lista):
	a_lista = [str(item) for item in lista]
	cadena = ''.join(a_lista)
	return cadena
######################################################

######################################################
def contar_ceros(binario):
	contador_unos = 0
	contador_ceros = 0
	acumulador = []

	for i in binario:
		if i == '1':
			contador_unos = 1 #Si se crusa con un 1 => suma 1 y ademas entra a la condicion de abajo
			if contador_unos == 1:
				acumulador.append(contador_ceros) # acumulo el contador de ceros en una lista
				contador_ceros = 0 #Vuelvo a inicializar los contadores
				contador_unos = 0
		elif i == '0':
			contador_ceros += 1

	#print(acumulador)		
	maximo = max(acumulador)
	return maximo
######################################################

######################################################
"""
Probar con diferentes numeros Enteros. En particular 
 32 = 1000000, que al evaluarlo con la funcion del desafio
retornara cero
"""
#######
n = int(input("Introduce un entero: "))
b = convertir_a_binario(n)
u = unir(b)
c = contar_ceros(u)

print("Resultado de convertir a binario: ", b)
print("Al pasarlo a lista: ",u)
print("El resultado de la funcion del desafio: ",c)

