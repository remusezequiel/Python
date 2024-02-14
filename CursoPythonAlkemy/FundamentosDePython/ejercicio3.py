"""Crea una función llamada verificar_calificacion que reciva tres parámetros: mota_1, nota_2, nota_3
    -> Dentro de la funcion calcular el promedio de notas
    -> Si el promedio es mayor o igual a 6, entonces la función debe retornar un mensaje "Aprobado", 
       en caso contrario sera "Reprobado"    
"""
# FUNCIONES
def linea():
    print("---------------------")

def verificar_calificacion(nota_1,nota_2, nota_3):
    promedio = (nota_1+nota_2+nota_3)/3

    if promedio >=6:
        return("Aprobado")
    else:
        return("Reprobado")

# EJECUCION
if __name__ == "__main__":
    contador = 0
    lista_notas = [None]*3

    linea()
    while contador < 3:
        
        nota = float(input("Ingrese la nota: "))
        lista_notas[contador] = nota           
        contador += 1
    
    linea()
    
    print("\nLista de notas ingresada: ", lista_notas)
    print("\nEl alumno esta: ", verificar_calificacion(lista_notas[0],lista_notas[1],lista_notas[2]))




