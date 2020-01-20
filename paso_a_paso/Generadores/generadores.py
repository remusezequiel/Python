"""
Los generadores se utilizan para generar objetos
sin necesidad de guardar la informacion en ram

yield es como el return, pero la gracia de usar yield
es que conserva la iteracion del bucle para la siguiente vez
que se le invoque
"""

def return_valores():
    print("hola mundo 1")
    return True

def generador(*args):
    for i in args:
        yield args * 10

def contador(max):
    n = 0
    while n<max:
        yield n
        n += 1

def recorre(list):
    while True:
        for n in list:
            yield n

#print(return_valores())
for i in generador(1,2,3):
    print(i)

#uso de contador
gen = recorre(['a','b','c','d'])
print(gen)
gen.__next__
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(iter(gen))
