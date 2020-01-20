################################################################################
class Circulo:
    """
    #Variable de clase: Le pertenecen a la clase y no a los objetos
    #El guion bajo adelante le dice a los desarrolladores que
    no modifiquen ese valor
    """
    _pi = 3.1416

    def __init__(self,radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * Circulo.pi
################################################################################

c_1 = Circulo(4)
c_2 = Circulo(5)

print(c_1.radio)
print(c_2.radio)

#No necesito crear un objeto para obtener pi
print(Circulo.pi)

#Esto nos va a mostrar un diccionario con las variables de clase y las de Metodos
print(c_1.__dict__)
