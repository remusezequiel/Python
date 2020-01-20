"""
Metodos privados y publicos:

#Los atributos privados son atributos que no pueden ser modificados
por el usuario
"""
class Usuario:
    def __init__(self,username, password, email):
        self.username = username
        #Quiero que el password sea modificable solo desde la clase
        #__password va a ser un atributo privado
        self.__password = self.__generar_password(password)
        self.email = email

    #Metodo privado
    def __generar_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password

manolo = Usuario("Manolo", "esteseraelpassword", "manolo@gmail.com" )
print(manolo.username)
#Al ser atributos privados no pueden modificarse desde aqui
#Ni tampoco llamarse
#print(manolo.password)
#manolo.password = 'cambioPassword'
#print(manolo.password)
print(manolo.email)
#Para poder tomar el password, creamos un getter en la clase llamada get_password
print(manolo.get_password())
