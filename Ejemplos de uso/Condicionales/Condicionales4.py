salario_presidente=int(input("Introduce el salario del presidente:"))
print("Salarios presidente" + str(salario_presidente))

salario_director=int(input("Introduce el salario del director:"))
print("Salarios director" + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area:"))
print("Salarios jefe de area" + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo:"))
print("Salarios administrativo" + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")