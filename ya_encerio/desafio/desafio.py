"""
	Idea del ejercicio:
		Crear una funcion que recive un string numerico que representa un numero
		binario. Luego lo que debemos hacer es contar los ceros que existen entre
		cada extremo de unos.
		La funcion debe retornar el numero maximo de ceros existente entre cada 
		extremos de unos dentro del string.
"""
##############
#Solucion:
##############

##########################################################################
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
##########################################################################

##############
#Puebas:
##############
"""
Nota: por definicion de binary gap, por ejemplo para 32 es un 1 que consecutivamente
presenta una cantidad de 5 ceros, sin en bargo, al no encontrarse con ningun 1 ni
en el medio ni en el final el total de binary gaps es cero.

Por otro lado, cuando le paso "0000101" me cuenta 4 ceros... Pero denuevo, en realidad
el numero binario "0000101" representa al numero "101", ya que los ceros de adelante
no poseen ningun valor agregado al numero, es decir, "0000101" = "101"
por lo que en realidad, el numero binario "0000101" no sera una posibilidad de entrada.

En el caso de que sea una posibilidad de entrada, habria que modificar dicho codigo 
validando dicha entrada de numeros. Pero en mi codigo estoy suponiendo que no se dara
dicha entrada de numero en su uso. Sin embargo, en las pruebas dejo en claro que este
devolvera 4 porque cuenta los ceros hasta llegar al uno 
"""

pruebas = [
	"1001111", "11111", "100101", "10010000001",
	 "0000101 (caso no validado)", "1010000", "10100100001", "100000"
]

r = 0
#Recorro la lista de pruebas 
for p in range(len(pruebas)):
	r = contar_ceros(pruebas[p])
	print(" Para -> ", pruebas[p], ":" ,r)
##########################################################################






















