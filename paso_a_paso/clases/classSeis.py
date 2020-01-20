"""
properties => Con las properties nosotros podemos trabajar con atributos
privados a partir
"""


class Usuario:
    def __init__(self,username, password, email):
        self.username = username
        #Quiero que el password sea modificable solo desde la clase
        #__password va a ser un atributo privado
        self.__password = self.__generar_password(password)
        self.email = email

    #Metodo privado
    #Una pseudo encriptacion usando upper, trucha pero encriptacion al fin
    def __generar_password(self, password):
        return password.upper()

    #Getter
    @property
    def password(self):
        return self.__password
    #setter
    @password.setter
    def cambio_password(self, valor):
        self.__password = self.__generar_password(valor)


manolo = Usuario("Manolo", "esteseraelpassword", "manolo@gmail.com" )
print(manolo.username)
#Al tener el @property transformo la funcion en atributo
print(manolo.password)
manolo.cambio_password = 'Nuevo password'
#con la propiedad setter de la propiedad password puedo modificar el valor
print(manolo.password)
