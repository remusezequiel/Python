def enter():
	print(" ")

valido=False

email=input("Introduce tu email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True
enter()
if valido:
	print("Email correcto")
else:
	print("Email incorrecto")