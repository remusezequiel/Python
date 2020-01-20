"""
El override es la sobreescritura de metodos y la prioridad con la que
python toma estos metodos.

En este caso dentro de la clase mascota y dentro de la clase gato
tenemos el mismo metodo show_name. Que va a hacer gato, como el metodo se llama
desde la clase gato, primero se fija si el metodo esta dentro de gato, si no
se va a fijar a Felino y si no esta en felino, se va a ir a buscar el metodo a
mascota, que es donde hay otro show_name. Va atomar y utilizar el primero que
encuentre.
"""

class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal):#Clase padre
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino esta casando")

class Mascota:

    def __init__(self, nombre):
        self.nombre = nombre

    def show_name(self):
        print(self.nombre)

class Gato(Felino,Mascota):#hijo de Felino

    def __init__(self, nombre):
        #Mandamos el nombre al init de mascota, asi se puede usar
        Mascota.__init__(self, nombre)
        self.nombre_gato = nombre

    def gato_cazador(self):
        self.cazar()

    def show_name(self):
        Mascota.show_name(self)
        print("El nomebre del gato es: ", self.nombre)

class Jaguar(Felino):#hijo de Felino
    pass


gato = Gato('Miky')
#gato.nombre = 'Miky'
gato.show_name()
