"""
    ESTRUCTURA
--------------------
while condicion:
    codigo
else:
    codigo
"""

contador = 0

while contador < 4 :
    print(contador)
    contador+=1
else:
    print('While a terminado')

#Contando hasta 10

contador = 0

while contador < 10 :
    print(contador)
    contador+=1
else:
    print("El contador termina con su valor en: ", contador)

#Expreciones break y continue
while contador < 20:
    print(contador)
    contador+=1
    if contador < 14:
        continue
    if contador == 14:
        #Aca va a cortar y no va a mostrar el else porque se saltea todo el bucle
        break
else:
    print("El contador termina con su valor en: ", contador)


#Uso de banderas (flag)
#Las banderas son valores booleanos que

cont = 0
flag = True

while flag:
    print(cont)
    cont += 1

    if cont == 5:
        continue
    if cont == 6:
        flag=False
else:
    print("El contador termina con su valor en: ", cont)
