numero = 5
factorial = 1
"""
    Mientras el numero sea mayor a cero a factorial se lo multiplicara
    por el valor de numero y luego al numero se le restara 1.
    Esto se iterara hasta que el valor de numero sea 0.
"""
while numero > 0:
    factorial = factorial * numero
    numero -= 1

print(factorial)

print('----------------------')
#¿Como paso esto a una funcion para poder utilizarla con cualquier numero?

def factorial(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

f = factorial(3)
print(f)

print('----------------------')

#Entonces:
print('el factorial de 1 es', factorial(1))
print('el factorial de 2 es', factorial(2))
print('el factorial de 3 es', factorial(3))
print('el factorial de 4 es', factorial(4))

print('----------------------')
#Lo que es lo mismo que:
for f in range(0,20):
    print('El factorial de ', f, ' es ', factorial(f))

print('----------------------')
#Puedo pasar esto a una funcion!
def rango_factorial(min,max):
    for f in range(min,max+1):
        print('El factorial de ', f, ' es ', factorial(f))

rango_factorial(0,10)
