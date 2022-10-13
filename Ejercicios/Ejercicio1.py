#Importamos todo el fichero para no tener que importar varias veces la misma libreria
from Ejercicios.Funcion import *

def ejercicio1():

    x = sympy.Symbol("x")
    y = sympy.Function("y")

    #Definimos la ecuación 
    f = (x**2*y(x) - y(x)) / (y(x) + 1)

    #Usamos la funcion que creamos para resolver las EDO
    print("La solución general es la siguinte: \n")
    pprint(resolver(f))
    print("\n")
    print("La solución con condición incial y(3) = -1: \n")
    try:
        condicion_inicial(f, 3, -1)
    except ValueError:
        print("Hay un logaritmo de -1 en la solución")
    else:
        pass
    print(condicion_inicial(f, 3, -1))



