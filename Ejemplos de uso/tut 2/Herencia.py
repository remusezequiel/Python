#PRIMER EJEMPLO 
"""
#superclase
class Vehiculos():
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.enmarcha = False
    self.acelera = False
    self.frena = False

  def arrancar(self):
    self.enmarcha = True

  def acelerar(self):
    self.acelera = true

  def frenar(self):
    self.frena = True

  def estado(self):
    print(" Marca: ", self.marca, "\n Modelo: ", self.modelo,
          "\n En Marcha: ", self.enmarcha, "\n Acelerando: ", self.acelera,
          "\n Frenando: ", self.frena)

#La clase moto hereda las propiedades de la suerclase Vehiculo
class Moto(Vehiculos):
  pass


moto = Moto("zanella","patagonia eagel")

moto.estado()
"""

#SEGUNDO EJEMPLO
"""
  #PYTHON acepta herencia multiple

#superclase
class Vehiculos():
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.enmarcha = False
    self.acelera = False
    self.frena = False

  def arrancar(self):
    self.enmarcha = True

  def acelerar(self):
    self.acelera = true

  def frenar(self):
    self.frena = True

  def estado(self):
    print(" Marca: ", self.marca, "\n Modelo: ", self.modelo,
          "\n En Marcha: ", self.enmarcha, "\n Acelerando: ", self.acelera,
          "\n Frenando: ", self.frena)

#Clase furgoneta que hereda de vehiculo
class Furgoneta(Vehiculos):
  def carga(self, cargar):
    self.cargado = cargar
    if(self.cargado):
      return "La furgoneta esta cargada"
    else :
      return "La furgoneta no esta cargada"


#La clase moto hereda las propiedades de la suerclase Vehiculo
class Moto(Vehiculos):
  hcaballito=""
  def caballito(self):
    self.hcaballito="voy haciendo caballito"

  def estado(self):#sobre escritura de metodos
    print(" Marca: ", self.marca, "\n Modelo: ", self.modelo,
          "\n En Marcha: ", self.enmarcha, "\n Acelerando: ", self.acelera,
          "\n Frenando: ", self.frena, "\n", self.hcaballito)

#Clase independiente
class VElectricos():
  def __init__(self):
    self.autonomia = 100

  def cargarEnergia(self):
    self.cargando=True


moto = Moto("zanella","patagonia eagel")
moto.caballito()
moto.estado()

furgoneta = Furgoneta("renault", "Kangoo")
furgoneta.arrancar()
furgoneta.estado()
print(furgoneta.carga(True))



#La clase bicicleta heredara de dos clases
class BicicletaElectrica(VElectricos,Vehiculos):
  pass

bici = BicicletaElectrica()
"""


#TERCER EJEMPLO

#superclase
class Vehiculos():
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.enmarcha = False
    self.acelera = False
    self.frena = False

  def arrancar(self):
    self.enmarcha = True

  def acelerar(self):
    self.acelera = true

  def frenar(self):
    self.frena = True

  def estado(self):
    print(" Marca: ", self.marca, "\n Modelo: ", self.modelo,
          "\n En Marcha: ", self.enmarcha, "\n Acelerando: ", self.acelera,
          "\n Frenando: ", self.frena)

#Clase furgoneta que hereda de vehiculo
class Furgoneta(Vehiculos):
  def carga(self, cargar):
    self.cargado = cargar
    if(self.cargado):
      return "La furgoneta esta cargada"
    else :
      return "La furgoneta no esta cargada"


#La clase moto hereda las propiedades de la suerclase Vehiculo
class Moto(Vehiculos):
  hcaballito=""
  def caballito(self):
    self.hcaballito="voy haciendo caballito"

  def estado(self):#sobre escritura de metodos
    print(" Marca: ", self.marca, "\n Modelo: ", self.modelo,
          "\n En Marcha: ", self.enmarcha, "\n Acelerando: ", self.acelera,
          "\n Frenando: ", self.frena, "\n", self.hcaballito)

#Clase independiente
class VElectricos():
  def __init__(self):
    self.autonomia = 100

  def cargarEnergia(self):
    self.cargando=True


moto = Moto("zanella","patagonia eagel")
moto.caballito()
moto.estado()

furgoneta = Furgoneta("renault", "Kangoo")
furgoneta.arrancar()
furgoneta.estado()
print(furgoneta.carga(True))



#La clase bicicleta heredara de dos clases
#Como esta primero VElectricos hereda el __init__ de esta clase
class BicicletaElectrica(VElectricos,Vehiculos):
  pass

bici = BicicletaElectrica()







  
