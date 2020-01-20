"""
Veamos que ambas clases tienen igual metodo y propiedades. Para no repetirnos
debemos utilizar el metodo de herencia

Debemos crear una clase que nos permita utilizar los metodos y atributos
PUBLICOS para crear la clase gato y la clase jaguar.

Que tienen en comun => ambos son felinos

class Gato:
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino esta casando")


class Jaguar:
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino esta casando")

gato = Gato()
jaguar = Jaguar()
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

class Gato(Felino):#hijo de Felino
    def gato_cazador(self):
        self.cazar()

class Jaguar(Felino):#hijo de Felino
    pass


gato = Gato()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(gato.gato_cazador())
print(gato.terrestre)
print(jaguar.garras_retractiles)
print(jaguar.cazar())
print(jaguar.terrestre)
