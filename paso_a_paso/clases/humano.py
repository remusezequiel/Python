class Humano:
    #Metodo Constructor
    def __init__(self,nombre,edad):
        #Atributos
        self.nombre = nombre
        self.edad = edad

    def hablar(self, mensaje):
        print(mensaje)

    class Profesion:
        def cual(prof):
            print(prof)


pepe = Humano('pepe', 25)

pepe.Profesion.cual("Programacion")
