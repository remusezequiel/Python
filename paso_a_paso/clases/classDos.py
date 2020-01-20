"""

"""
################################################################################
class Lapiz():

    #Atributos
    color = 'Amarillo'
    contiene_borrador = True
    usa_grafito = True

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


lapiz_generico = Lapiz()
lapiz_generico.color #Atributos sin parentesis
lapiz_generico.dibujar()#Metodos con los parentesis
lapiz_generico.contiene_borrador = False#Le cambio el valor al atributo
