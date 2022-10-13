#Importamos la librería que nos ayudará a resolver las EDO
import sympy
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

def resolver(f):
    #El parámetro f será la ecuación a resolver

    #Primero definimos las incógnitas
    x = sympy.Symbol("x")
    y = sympy.Function("y")
    
    #Usamos la función para resolver la ecuación
    solucion = sympy.dsolve(y(x).diff(x) - f)

    return solucion

def condicion_inicial(f, a, b):

    x = sympy.Symbol("x")
    y = sympy.Function("y")

    #Definimos la condicion inicial
    CI = {y(a) : b}
    
    solucion = sympy.dsolve(f, y(x), ics= CI)

    return solucion
    
def resolver_y_no_despejada(f, x, y):

    x = sympy.Symbol("x")
    y = sympy.Function("y")
    
    #Usamos la función para resolver la ecuación
    solucion = sympy.dsolve(f)

    return solucion

def grafica():
    t = np.linspace(-5, 5, 500)
    fig, ax = plt.subplots()
    for C in range(-4, 4, 1):
        y = C*np.sqrt(t) + t**2
        ax.plot(t, y, label= "Para $C=%s$" %C)
        plt.xlim(-5, 7)
        plt.legend(loc="best")
        plt.savefig("Ejercicios/Img/Familia_soluciones.png")
    
