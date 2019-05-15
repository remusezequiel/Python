def line():
	print("____________________")	
def point_line():
	print(".....................................................")
"""Aca empieza el programa con llamado a las funciones"""		

print("Programa de becas")

distancia_escuela=int(input("Introduce la distancia en la escuela en kilometros:"))
numero_hermanos=int(input("Introduce el numero de numero_hermanos:"))
salario_familiar=int(input("Introduce el salario familiar bruto:"))

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<20000:
	print("Tienes derecho a becas")
else:
	print("No tienes derecho a becas")

line()
print("Tus datos son:")
point_line()
print("Distancia a la escuela:" + str(distancia_escuela))
point_line()
print("Numero de hermanos:" + str(numero_hermanos))
point_line()
print("salario familiar:" + str(salario_familiar))
point_line()
