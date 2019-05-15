edad=int(input("Ingresa una edad: "))

while edad<5 or edad>150:
	print("Has introducido una edad negatica. Vuelve a intentarlo")
	edad=int(input("Ingresa una edad: "))


print("Edad del aspirante " + str(edad))	