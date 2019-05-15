#PRIMER EJEMPLO
""" 
class coche():
  #propiedades del coche
  largoChasis = 250
  anchoChasis = 120
  ruedas = 4
  enmarcha = False
  #Comportamientos
  def arranque(self):
    self.enmarcha = True

  def estado(self):
    if(self.enmarcha):
      return "El coche esta en marcha"
    else :
      return "El coche esta parado"



#construyo una instancia de la clase coche:
coche_1 = coche() #a esto se le llama instanciar la clase

print("El largo del coche es: ", coche_1.largoChasis)
print("El coche tiene", coche_1.ruedas, "ruedas")
#print("Estado de arranque", coche_1.enmarcha)
print(coche_1.estado())
coche_1.arranque()
#print("Estado de arranque", coche_1.enmarcha)
print(coche_1.estado())
"""


#SEGUNDO EJEMPLO
"""
class coche():
  #propiedades del coche. Estado inicial
  #definicion de un metodo constructor __init__ con dos guion bajo
  def __init__(self):
    self.__largoChasis = 250
    self.__anchoChasis = 120
    self.__ruedas = 4#Encapsulo para que no se pueda modificar el valor desde fuera
    self.__enmarcha = False

  #Comportamientos
  def arranque(self, arrancamos):
    #Este metodo permite que modifiquemos el valor del constructor desde fuera del programa
    self.__enmarcha = arrancamos
    if(self.__enmarcha):
      return "El coche esta en marcha"
    else :
      return "El coche esta parado"

  def estado(self):
    print("El coche tiene", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis,
          "y un lardo de", self.__largoChasis)



#construyo una instancia de la clase coche:
print("Creamos el objeto coche_1")
coche_1 = coche() #a esto se le llama instanciar la clase
print(coche_1.arranque(True))
coche_1.estado()


#Construyo otro coche
print("A continuacion creamos un segundo objeto")
coche_2 = coche()
print(coche_2.arranque(False))
coche_2.__ruedas = 2
coche_2.estado()
"""

#TERCER EJEMPLO
class coche():
  #Constructor encapsulado, para que esos valores solo se modifique el valor a partir de metodos pertenecientes a la clase
  def __init__(self):
    self.__largoChasis = 250
    self.__anchoChasis = 120
    self.__ruedas = 4
    self.__enmarcha = False

  #Comportamientos
  def arranque(self, arrancamos):
    self.__enmarcha = arrancamos

    if(self.__enmarcha):
      chequeo=self.__chequeo_interno()

    if(self.__enmarcha and chequeo):
      return "El coche esta en marcha"
    elif(self.__enmarcha and chequeo==False):
      return "Algo a salido Mal"
    else :
      return "El coche esta parado"

  def estado(self):
    print("El coche tiene", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis,
          "y un lardo de", self.__largoChasis)

  def __chequeo_interno(self):
    print("Realizando chequeo interno")

    self.gasolina="ok"
    self.aceite="ok"
    self.puertas="cerradas"

    if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas" ):
      return True
    else :
      return False


#Construyo una instancia de la clase coche:
print("Creamos el objeto coche_1")
coche_1 = coche() #a esto se le llama instanciar la clase
print(coche_1.arranque(True))
coche_1.estado()

#Construyo otro coche
print("------------A continuacion creamos un segundo objeto---------------")
coche_2 = coche()
print(coche_2.arranque(False))
coche_2.__ruedas = 2
coche_2.estado