from Ejercicios.Funcion import *


def ejercicio2():

    x = sympy.Symbol("x")
    y = sympy.Function("y")

    #Definimos la ecuación
    ecuacion = sympy.Eq(y(x).diff()*np.sin(x), y(x)*np.log(y(x)))