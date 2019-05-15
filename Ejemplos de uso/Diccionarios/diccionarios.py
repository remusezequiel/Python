#Funcion para dejar un espacio en blanco
def enter():
	print(" ")

def acceder_diccionario(diccionario,dic_elem):
	print(diccionario[dic_elem])#Y se puede acceder al valor de cada diccionario
	enter()


"""
#Los diccionarios van entre llaves
miDiccionario={"Alemania": "Berlin","Francia": "Paris","Reino Unido":"Londres","España":"Madrid"}
print(miDiccionario["España"])#Y se puede acceder al valor de cada diccionario
enter()
"""
#dic={clave:valor}
miDiccionario={
        "Alemania": "Berlin",
        "Francia": "Paris",
        "Reino Unido":"Londres",
        "España":"Madrid"
        }
acceder_diccionario(miDiccionario,"España")

#agrego en ele diccionario a italia con la clave y el valor: dic[clave]=valor
miDiccionario["Italia"]="Lisboa"
#Asi se imprime todo lo que hay adentro del diccionario
print(miDiccionario)
enter()

#Se sobre escribe. Los diccionarios se sobresciben no puede existir una palabra con mas de un valor
miDiccionario["Italia"]="Roma"
#Elimino del diccionario a Reino Unido
del miDiccionario["Reino Unido"]
print(miDiccionario)
enter()

#Ahora creo una tupla
"""Las tuplas van entre corchetes"""
miTupla=["España","Francia","Reino Unido", "Alemania"]
miDiccionario={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Berlin"}
print(miDiccionario)
enter()

#Algo mas extendido
miDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(miDiccionario["anillos"])
enter()

#Algo maaaas extendio
miDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario["anillos"])
enter()

#Cositas curiosas
print("Cositas curiosas")
print("Keys:")#Definiciones
print(miDiccionario.keys())
enter()
print("Values:")#Valores del diccionario
print(miDiccionario.values())
enter()
print("Len:")#Cuenta
print(len(miDiccionario))

