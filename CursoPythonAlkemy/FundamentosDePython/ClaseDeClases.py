# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:19:50 2024

@author: Hp
"""

"""
OBJETO: 
    
INSTANCIAS: Ejemplar de un objeto basado en la clase
"""
"""
def empleado_con_mas_clientes(empleados):
    max_clientes = max(empleados, key=lambda empleado: empleado.clientes_captados if isinstance(empleado, EmpleadoComision) else 0)
    return max_clientes
"""

class Auto:
    #Propiedades / Atributos
    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
    
    
    #Setters y Getters
    # Setter - Establece valores de cada atributo
    # Getter - 
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getAnio(self):
        return self.anio
        return self.anio
    
    #Metodos - compartimientos, acciones
    def tocarBocina():
        print("pi pii")
    
    def mostrarAuto(self):
        print(f'Marca: {self.getMarca()}' )
        print(f'Modelo: {self.getModelo()}' )
        print(f'Color: {self.getMarca()}' )
        print(f'Anio: {self.getMarca()}' )