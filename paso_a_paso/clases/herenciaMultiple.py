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
    nombre = ''

    def show_name(self):
        print(self.nombre)

class Gato(Felino,Mascota):#hijo de Felino
    def gato_cazador(self):
        self.cazar()

class Jaguar(Felino):#hijo de Felino
    pass


gato = Gato()
jaguar = Jaguar()

print("gato.garras_retractiles")
print(gato.garras_retractiles)
gato.nombre = 'miky'
print("gato.show_name()")
gato.show_name()
print("gato_cazador()")
gato.gato_cazador()
print("gato.terrestre")
print(gato.terrestre)
print("jaguar.garras_retractiles")
print(jaguar.garras_retractiles)
print("jaguar.cazar()")
jaguar.cazar()
print("jaguar.terrestre")
print(jaguar.terrestre)
