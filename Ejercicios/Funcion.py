#Importamos la librería que nos ayudará a resolver las EDO
import sympy

def resolver(f):
    #El parámetro f será la ecuación a resolver

    #Primero definimos las incógnitas
    x = sympy.Symbol("x")
    y = sympy.Function("y")
    
    #Usamos la función para resolver la ecuación
    solucion = sympy.dsolve(y(x).diff(x) - f)

    return solucion

    
