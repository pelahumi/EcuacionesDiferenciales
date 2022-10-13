from Ejercicios.Funcion import *

def ejercicio4():

    t = sympy.Symbol("t")
    y = sympy.Function("y")

    ecuacion = sympy.Eq(2*t*y(t).diff() - y(t), 3*t**2)

    print("La solucion es la siguiente: ")
    pprint(resolver_y_no_despejada(ecuacion, t, y))
    grafica()

