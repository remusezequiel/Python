#Si queremos empaquetar estos mensajes en una linea de codigo
print("Estamos aprendiendo Python")
print("Estamos aprendiendo funciones basicas")
print("Poco a poco iremos avanzando")
#Podemos crear una funcion para poder reutilizar el codigo

def mensaje():
  print("Estamos aprendiendo Python")
  print("Estamos aprendiendo funciones basicas")
  print("Poco a poco iremos avanzando")

print("\n Llamamos a la funcion mensaje: ")
mensaje()

#Creamos la funcion suma
def suma_1():
  num_1=5
  num_2=7
  print(num_1 + num_2)

#Llamamos a la funcion suma
suma_1()

#Creamos la funcion suma pero para que resiva parametros
def suma_2(num_1, num_2):
  print(" " + str(num_1))
  print("+")
  print(" " + str(num_2))
  print("--------")
  print(num_1 + num_2)

suma_2(3,2)

#Otra forma seria utilizando un "return"
def suma_3(num_1,num_2):
  resultado = num_1 + num_2
  return resultado

a = suma_3(5,6)
print(a)



