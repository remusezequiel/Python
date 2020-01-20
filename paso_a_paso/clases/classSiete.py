"""
Metodos estaticos:Estan en la clase pero no tiene el self

Metodos de Instancia: Son los que tienen self y se encuentran dentro de la clase
"""

################################################################################
class Circulo:
    """
    #Variable de clase: Le pertenecen a la clase y no a los objetos
    #El guion bajo adelante le dice a los desarrolladores que
    no modifiquen ese valor
    """
    @staticmethod
    def pi():
        return 3.1416

    def __init__(self,radio):
        self.radio = radio

    def area(self):#Metodo de instancia
        return self.radio * self.radio * Circulo.pi()
################################################################################

c_1 = Circulo(4)
print(Circulo.pi())
print(c_1.radio)
print(c_1.area())
