from Ejercicios.helpers import *
from Ejercicios.Funcion import *
from Ejercicios.Ejercicio1 import ejercicio1
from Ejercicios.Ejercicio2 import ejercicio2
from Ejercicios.Ejercicio3 import ejercicio3
from Ejercicios.Ejercicio4 import ejercicio4

def lanzador():
    while True:
        limpiar_pantalla()
        print("========================") 
        print(" BIENVENIDO AL MENU ") 
        print("========================") 
        print("Elige el ejercicio que quieres resolver")
        print("========================") 
        print("[1] Ejercicio 1 ") 
        print("[2] Ejercicio 2 ") 
        print("[3] Ejercicio 3 ") 
        print("[4] Ejercicio 4 ")
        print("[5] Cerrar el Manager ")
        print("========================")

        opcion = input("> ")
        limpiar_pantalla()

        if opcion == "1":
            ejercicio1()
            
        if opcion == "2":
            ejercicio2()

        if opcion == "3":
            ejercicio3()

        if opcion == "4":
            ejercicio4()
            
        if opcion == "5":
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")