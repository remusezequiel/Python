import random
import datetime
import sys
import time

#Uso de random

valor = random.randint(0,10)
print(valor)
lista = [True, "carlos", 3, 3.14]
valor = random.choice(lista)
print(valor)
random.shuffle(lista)
print(lista)

#uso de datetime

ahora = datetime.datetime.now()
print(ahora)

#uso de sys
for i in range(100):
    #pequeño delay
    time.sleep(0.5)
    #Escribime esto
    sys.stdout.write("\r%d %%" % i)
    #ponelo en pantalla
    sys.stdout.flush()
