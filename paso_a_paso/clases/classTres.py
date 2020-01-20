"""
Cuando queremos que los objetos inicialicen con
una cierta cantidad de atributos y valores, esos Atributos
deben ser inicializados en el metodo init
"""
################################################################################
class Lapiz:

    #Atributos
    def __init__(self,color,borrador,grafito):
        self.color = color
        self.contiene_borrador = borrador
        self.usa_grafito = grafito

    #Metodos: funciones dentro de la clase
    def dibujar(self):
        if self.es_valido_para_borrar():
            print("El lapiz esta dibujando.")
        else:
            print("El lapiz no tiene borrador.")

    def borrar(self):
        print("El lapiz esta borrando.")

    def es_valido_para_borrar(self):
        return self.contiene_borrador
################################################################################

#Si tenes un init con argumentos debes pasarle los parametros de init a la clase
lapiz_generico = Lapiz('verde',True, True)
lapiz_generico.color #Atributos sin parentesis
lapiz_generico.dibujar()#Metodos con los parentesis
lapiz_generico.contiene_borrador = False#Le cambio el valor al atributo
