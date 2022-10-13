from Funcion import *

def ejercicio4():

    t = sympy.Symbol("t")
    y = sympy.Function("y")

    ecuacion = sympy.Eq(2*t*y(x).diff() - y, 3*t**2)

    print("La solucion es la siguiente: ")
    print(resolver(ecuacion))

