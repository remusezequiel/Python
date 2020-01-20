"""
Metodos de clase: les pertenecen a la clase

Buscar Factory method
"""

class Animal:
    volador = True

class Cocodrilo(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def new(cls, nombre):
        cls.volador = False
        return Cocodrilo(nombre)

#Los metodos de clase pueden acceder a los atributos de las
#clases de las cuales estamos heredando
cocodrilo = Cocodrilo.new('Coco')
print(cocodrilo.nombre)
print(cocodrilo.volador)
