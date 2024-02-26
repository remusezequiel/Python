# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:16:37 2024

@author: Ezequiel Remus
"""

"""
Enunciado:

Cierta empresa requiere una aplicación informática 
para administrar los datos de su personal, del
cual se conoce:

- número de DNI
- nombre
- apellido 
- año de ingreso.

Existen dos categorías de
empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo, 
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes
captados no llega a cubrir el salario mínimo, cobrará
el salario mínimo. 

-----

Los empleados con salario fijo
tienen un sueldo básico y un porcentaje adicional
en función del número de años que llevan la empresa: 
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre
completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).

creen 10 empleados

"""
class Empleado:
    """Empleado Base"""
    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

    def mostrar_salario(self):
        pass



class EmpleadoFijo(Empleado):
    """Empleado Fijo: Hereda de Empleado Base"""
    def __init__(self, dni, nombre, apellido, anio_ingreso, sueldo_basico):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.sueldo_basico = sueldo_basico

    def mostrar_salario(self):
        """Pregunta: ¿Puedo trabajar directamente con la fecha actual?"""
        anios_empresa = 2024 - self.anio_ingreso
        if anios_empresa < 2:
            return self.sueldo_basico
        elif 2 <= anios_empresa <= 5:
            return self.sueldo_basico * 1.05
        else:
            return self.sueldo_basico * 1.10



class EmpleadoComision(Empleado):
    """Empleado Comision: Hereda de Empleado Base"""
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def mostrar_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        if salario < self.salario_minimo:
            return self.salario_minimo
        else:
            return salario

def mostrar_salarios(empleados):
    """ Muestra el salario de un empleado sin distinguir de que clase biene"""
    for empleado in empleados:
        print(f'{empleado.nombre} {empleado.apellido}: {empleado.mostrar_salario()}')




if __name__ == "__main__":
    
    # Creo una lista de 10 Empleados
    empleados = [
        EmpleadoFijo('12345678', 'Juan',     'Perez', 2021, 30000),
        EmpleadoFijo('14344678', 'Julian',   'Pixel', 2020, 30000),
        EmpleadoFijo('22345678', 'Agustina', 'Nuñez', 2022, 30000),
        EmpleadoFijo('13345678', 'Ignacio',  'Gutierrez', 2020, 30000),
        EmpleadoFijo('13355678', 'Luciana',  'Zapata', 2021, 30000),
        EmpleadoComision('23456789', 'Guido', 'Pasciucco', 2012, 20000, 30, 1500),    
        EmpleadoComision('24456789', 'Ezequiel', 'Remus', 2014, 20000, 2, 1500),    
        EmpleadoComision('24456489', 'Ana', 'Gomez', 2014, 20000, 8, 1500),    
        EmpleadoComision('22456789', 'Ana2', 'Gomez', 2021, 20000, 5, 1500),    
        EmpleadoComision('23432789', 'Ana3', 'Gomez', 2018, 20000, 3, 1500),
    ]
    
    mostrar_salarios(empleados)
    
    # print(f'Empleado con más clientes: {empleado_con_mas_clientes(empleados).nombre}')




