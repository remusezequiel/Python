import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Es necesario colocar por lo menos un argumento al lado de la llamada del archivo")
    else:
        print(sys.argv[1])
