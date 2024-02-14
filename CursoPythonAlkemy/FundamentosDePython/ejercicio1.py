"""
Crear un algoritmo para calcular la sumatoria de los primeros 100 numeros con el ciclo while.
"""
def linea():
    print("---------------------")
    
respuesta = 0
contador = 0
texto_1 = "La suma de los primeros 100 numeros es: "

while contador<100:
    contador+=1
    
    # print(str(respuesta), " + " , str(contador) ) // este comentario muestra la cuenta que se realizara
    respuesta= respuesta+contador        
    # print("\t\t =>", respuesta) // este comentario muestra el resultado de la suma en esta iteracion
    

print(texto_1, respuesta)