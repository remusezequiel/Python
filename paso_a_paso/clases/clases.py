##############################################################
class Vehiculos():
    #____________________________
    #Metodos
    #____________________________
    #Constructor_________________
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    #"""""""""""""""""""""""""""""""""""

    #____________________________
    def arrancar(self):
        self.enmarcha = True
    #"""""""""""""""""""""""""""""""""""

    #____________________________
    def acelerar(self):
        self.acelera = True
    #"""""""""""""""""""""""""""""""""""

    #____________________________
    def frenar(self):
        self.frena = True
    #"""""""""""""""""""""""""""""""""""

    #____________________________
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enmarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena)
    #"""""""""""""""""""""""""""""""""""

##############################################################

################################################################################
#A partir de aci utilizamos la clase

auto1 = Vehiculos("ford", "Fiesta")
auto1.estado()
