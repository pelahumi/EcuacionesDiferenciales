#Importamos la librería que nos ayudará a resolver las EDO
import sympy
from pprint import pprint
import numpy as np

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
    
