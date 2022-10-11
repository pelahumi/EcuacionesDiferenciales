#Importamos todo el fichero para no tener que importar varias veces la misma libreria
from Ejercicios.Funcion import *

def ejercicio1():

    x = sympy.Symbol("x")
    y = sympy.Function("y")

    #Definimos la ecuación 
    f = (x**2*y(x) - y(x)) / (y(x) + 1)

    #Usamos la funcion que creamos para resolver las EDO
    print(resolver(f))

ejercicio1()

