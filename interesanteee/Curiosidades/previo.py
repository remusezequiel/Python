"""
************************************************************************
                    Welcome to previo.py
************************************************************************    
    This file is an abstract wich contains basic concepts on 
    python development.
    It's dish up like a quick cheat sheet in the contruction
    process of the app.
    No function example in this file is used in the app, they're
    only examples of the concepts usage.
    In this file are proposed some examples with comments of each 
    one.
    It does not exist a logic order inasmach as this is made at the
    same time that a doubt was presented. 
************************************************************************
                    Bienvenidos a previo.py
************************************************************************
    Este archivo es un resumen de conceptos de python utilizados.
    Sirve de machete rapido en el proceso de construccion del programa. 
    Ninguna funcion es utilizada durante el programa.
    Se plantean ejemplos de los diferentes conceptos y se comenta 
    cada uno de ellos.
    No existe un orden logico, ya que esta hecho a medida que se fue 
    planteando alguna duda y/o problematica particular.
"""
##################################################################
#           INDEX
#
# 1- *args and **kwargs
# 2- Programacion funcional en python y lambda funciones
##################################################################
#                       REFERENCES
# -> https://www.geeksforgeeks.org/python-programming-language/
# -> https://es.stackoverflow.com/?tags=python
# -> https://codigofacilito.com/articulos/programacion-funcional-python
##################################################################

"""----------------------------------------------------------------------------------------"""
# 1- *args and **kwargs
"""
    The special syntax *args in function definitions in python is used to 
    pass a variable number of arguments to a function.
    It is used to pass a non-keyworded, variable-length argument list.

    -> The syntax is to use the symbol * to take in a variable number of 
    arguments; by convention, it is often used with the word args.

    -> What *args allows you to do is take in more arguments than the 
    number of formal arguments that you previously defined. 
    With *args, any number of extra arguments can be tacked on to your
    current formal parameters (including zero extra arguments).

    -> For example : we want to make a multiply function that takes any
    number of arguments and able to multiply them all together. 
    It can be done using *args.

    -> Using the *, the variable that we associate with the * becomes an
    iterable meaning you can do things like iterate over it, run some higher
    order functions such as map and filter, etc.
"""
# Examples:
# First:
# Python program to illustrate   
# *args for variable number of arguments 
def myFun1(*argv):  
    for arg in argv:  
        print (arg) 
#Quit the hashtag below to test the function    
#myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

#Second:
# Python program to illustrate  
# *args with first extra argument 
def myFun2(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
#Quit the hashtag below to test the function      
#myFun2('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

"""
    The special syntax **kwargs in function definitions in python 
    is used to pass a keyworded, variable-length argument list. 
    We use the name kwargs with the double star. The reason is 
    because the double star allows us to pass through keyword 
    arguments (and any number of them).

    A keyword argument is where you provide a name to the variable
    as you pass it into the function.

    One can think of the kwargs as being a dictionary that maps 
    each keyword to the value that we pass alongside it. 
    That is why when we iterate over the kwargs there doesn’t 
    seem to be any order in which they were printed out.
"""
#Example for usage of **kwargs:
#Fist:
# Python program to illustrate   
# *kargs for variable number of keyword arguments 
def myFun3(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
#Quit the hashtag below to test the function      
#myFun3(first ='Geeks', mid ='for', last='Geeks')  

#Second:
# Python program to illustrate  **kargs for  
# variable number of keyword arguments with 
# one extra argument. 
def myFun4(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
#Quit the hashtag below to test the function
#myFun4("Hi", first ='Geeks', mid ='for', last='Geeks')


#Using *args and **kwargs to call a function
def myFun5(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
#Quit the hashtags below to test the functions
#args = ("Geeks", "for", "Geeks") 
#myFun5(*args)
#  
#kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
#myFun5(**kwargs) 

"""----------------------------------------------------------------------------------------"""
# 2- Programacion funcional en python y lambda funciones

"""
    Anonymus funcitions:
        Habrá ocasiones en las cuales necesitemos crear 
        funciones de manera rápida, en tiempo de ejecución. 
        Funciones las cuales realizan una tarea en concreto, 
        regularmente pequeña. En estos casos haremos uso de 
        funciones lambda.

    Una función lambda es una función anónima, una función
    que no posee un nombre.
    En Python la estructura de una función lambda es la siguiente:
        
        lambda argumentos : cuerpo de la función
"""
#Examples:
suma = lambda val1=0, val2=0: val1 + val2
operacion = lambda operacion, val1=0, val2=0 : operacion(val1, val2)

resultado = operacion(suma, 10, 20)

#Quit the hashtag below to test the function
#print(resultado)

"""
    Map Function:
        La función map nos permite aplicar una función sobre cada uno
        de los elementos de un colección (Listas, tuplas, etc...).
        Haremos uso de esta función siempre que tengamos la necesidad
        de transformar el valor de un elemento en otro.

        La estructura de la función es la siguiente: 
            
            map(función a aplicar, objeto iterable)

        La función a aplicar debe de retornar un nuevo valor.
        Es apartir de estos nuevos valores que obtendremos una nueva colección.
"""
#Example:
#Obtener el cuadrado de todos los elementos en la lista.
def cuadrado(elemento=0):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = list( map(cuadrado, lista) )
#Quit the hashtag below to test the function
#print(resultado)

#Como la funcion cuadrado es sencilla podriamos sintetisar este comportamiento 
#en una funcion lamda, donde podriamos definir la variable resultadoDos de la
#Siguiente manera:
resultadoDos = list(map(lambda elemento : elemento * elemento , lista))


