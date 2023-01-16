def linea():
    print("-------------------")

def ingresa(mensaje):
    linea()
    sentence = input(mensaje + "\n --> ")
    linea()
    return sentence


def agradecimientos():
    print("\n------------------\n Gracias por\n usar\n el programa.\n------------------\n")

def clear(number):
    for i in range(number):
        print(" ")

def take_numbers(size):
    """Take a series of numbers 

    Args:
        size (numbers): Quantity of numbers to order

    Returns:
        list: list of input numbers
    """    
    number_list =[]
    counter = 0 

    while counter != size:
        number_list.append(float(input("Ingrese un numero: ")))
        counter += 1
    
    return number_list

def take_of_emptines(sentence):
    new_sentence = ""
    counter = 1
    while counter !=len(sentence):
        if sentence[counter-1:counter] != " ":
            new_sentence = new_sentence + sentence[counter-1:counter]
        counter += 1
    return new_sentence        

def ingresa_lista(size):
    the_list =[]
    counter = 0 

    while counter != size:
        the_list.append(input("Ingrese el elemento de la lista: "))
        counter += 1
        print("\t(Faltan ingresar: ", size - counter ," elementos)")
    return the_list
