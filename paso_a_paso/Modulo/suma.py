#!usr/bin/python3
"""
Aca colocamos todo lo que hace el modulo
"""
__author__ = "Ezequiel Remus"
__copyrigth__ = "-"
__credits__ = "Ezequiel Remus"

__license = "GPL"
__version__ = "1.0.1"
__manteiner__ = "Ezequiel Remus"
__email__ = "ezequielremus@gmail.com"
__status__ = "Developer"


def suma(*args):
    """
    Esta funcion suma todos los n elementos pasados por parametros
    """
    result = 0
    for i in args:
        result += i
    return result

#print(__name__)
if __name__ = '__main__':
    print("Modulo suma cargado")
