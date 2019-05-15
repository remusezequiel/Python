class Persona():
  def __init__(self,nombre, edad, Lugar_residencia):
    self.nombre = nombre
    self.edad = edad
    self.lu_re = Lugar_residencia

  def descripcion(self):
    print("Nombre: " , self.nombre,
          "\n Edad: ", self.edad ,
          "\n Lugar_residencia: ",self.lu_re )



class Empleado(Persona):
  def __init__(self, salario, antiguedad):
    self.salario = salario
    self.antiguedad = antiguedad


Antonio = Persona("Antonio" , 55 , "Espania")

Antonio.descripcion()














