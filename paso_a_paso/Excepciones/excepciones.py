try:
    print(2/0)
except ZeroDivisionError:
    print("No podes dividir por cero")

print("Despues de los except el programa puede seguir tranquilamente")
print("Sirve para validar errores poniendo los tipos de errores en la excepcion")
print("\nVeamos otro ejemplo: ")

try:
    lista=[1,2]
    print(lista[9])
except IndexError as ex:
    print(ex)
    print("No es posible obtener un valor de lista mayor a 2")
except ZeroDivisionError as ex:
    print(ex)
    print("No es posible dividir por cero")

print("Se termino el script")

#Para cualquier tipo de error
try:
    lista=[1,2]
    print(lista[9])
except Exception as ex:
    print(ex)
    print("No se que paso, pero hubo un error")
finally:
    print("Se termino el script")
