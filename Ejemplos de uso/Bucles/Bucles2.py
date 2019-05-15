def validar_email(parametro):
	email=False;
	for i in parametro:
		if i=="@":
			email=True;
	return email		

def condicion(value):
	if value==True:
		print("Email correcto")
	else:
		print("Email incorrecto")
	
		
#El programa empieza aca
cadena=input("Ingresa tu email:  ")
valor=validar_email(cadena)
condicion(valor)

