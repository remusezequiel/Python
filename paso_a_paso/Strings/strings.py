#Si uso comillas dobles para delimitar el string
#Entronces puedo usar dentro comillas simples
#y viceversa
string = "'Hola Mundo!'"
otro_string = '"Hola otra vez"'
comillas = "\"Esto va a estar entre comillas\""

print(string,"\n",otro_string,"\n",comillas)

#Concatenacion de strings
course = "Python 3"
name = "Eduardo"
final_message = "Nuevo curso de " + course + " por " + name
print(final_message)
final_message = "Nuevo curso de %s por %s" %(course,name)
print(final_message)
final_message = "Nuevo curso de {} por {}".format(course,name)
print(final_message)
