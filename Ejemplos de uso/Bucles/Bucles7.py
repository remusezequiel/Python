import math#Importo la clase math para poder utilizar la clase

print("Programa de caldulo de raiz cuadrada")
numero=int(input("introduce un numero: "))

intentos=0
while numero<0:
	print("No se puede hayar raices de numeros negativos")

	if intentos==2:
		print("Has consumidos demasiados intentos. El programa ha finalizado")
		break;

	numero=int(input("introduce un numero: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))	