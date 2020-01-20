class Usuario:
    pass

usuario = Usuario()
#Creamos un nuevo atributo dentro del objeto

print(usuario.__dict__)
usuario.nombre = 'Ezequiel'

print(usuario.nombre)
print(usuario.__dict__)
"""
Vemos que podemos crear los atributos
dentro de los objetos sin tener que declararlos dentro de las clases
"""


class User:
    def __init__(self):
        #Privado
        self.__password = "Este es un secreto"
    def mostrar_pass(self):
        print(self.__password)
user = User()
user.__password = "Este ya no es un secreto"
print(usuario.__dict__)
user.mostrar_pass()

"""
Metodos magicos:
"""

class Clase:
    def __new__(cls):
        print("Este es el verdadero constructor")
        print("El constructor new si o si necesita un retorno")
        return super().__new__(cls)

    def __init__(self):
        print("Este metodo constructor se ejecutara despues")

    def __str__(self):
        return "Esto se imprime cuando intento mostrar el objeto"

    def __getattr__(self, nombre):
        print("Aqui mostramos que no se encontro el atributo")
        self.otros_metodos()

    def otros_metodos(self):
        print("Otros metodos")

cl = Clase()
print(cl)
print(cl.apellido)
