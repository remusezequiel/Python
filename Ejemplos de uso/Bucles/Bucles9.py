nombre="Pildoras informaticas"#Esto tiene 20 caracteres
contador=0

for i in nombre:
	if i==" ":#Ignoro los espacios para poder contar la cantidad de letras
		continue
	contador+=1

print(contador)

#Ejemplo de pass: Pass sirve para ignorar codigo, basicamente

class MiClase:
	pass # para implementar mas tarde

#Ejemplo de "else":
email=input("Introduce tu email: ")

for i in email:
	if i=="@":
		arroba=True
		break
else:#Fijate que esta igualmente ideltado que el for
	arroba=False

print(arroba)
