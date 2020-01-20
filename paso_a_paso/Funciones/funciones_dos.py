def suma(a,b):
    return a+b

def division(numerador,denominador):
    return numerador / denominador

def multiples_valores():
    return 1,2,'lola'

def show_result( func ):
    print(func)

####################################
result = suma(10,11)
print(result)
print('####################################')

result = division(10,2)
print(result)
print('####################################')

result = division(10,2)
print(result)

result = division(2,10)
print(result)

result = division(denominador=2,numerador=10)
print(result)

print('####################################')

result = multiples_valores()
print(result)

pri = result[0]
sec = result[1]
ter = result[2]

print(pri,'\n',sec,'\n',ter)

print('Otra forma de hacer esto mismo es: ')

pri = multiples_valores()[0]
sec = multiples_valores()[1]
ter = multiples_valores()[2]

print(pri,'\n',sec,'\n',ter)

print('Otra forma de hacer esto mismo es: ')

pri, sec, ter = multiples_valores()
print(pri,'\n',sec,'\n',ter)

print('Uso de show result: ')
show_result(suma(1,2))
