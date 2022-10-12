from Ejercicios.Funcion import *

def ejercicio3():

    t = sympy.Symbol("t")
    y = sympy.Function("y")

    f = sympy.Eq(y(t).diff() -y(t) / (t - 2), 2*(t - 2)**2)

    print(resolver(f))
    