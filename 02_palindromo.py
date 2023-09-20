# Comprobar que de una palabra o frase introducida por el usuario es un palíndromo,
# es decir, se lee igual de izquierda a derecha que de derecha a izquierda
from builtins import input


def invertir_cadena(cadena_a_invertir):
    cadena_invertida = ""
    for letra in cadena_a_invertir:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida


def quitar_espacios(cad):
    return cad.replace(" ", "")


def comprueba_palindromo(cadena_original):
    cadena_original = quitar_espacios(cadena_original)
    cadena_invertida = invertir_cadena(cadena_original)
    return True if cadena_original == cadena_invertida else False


cadena = input("Introduzca una frase: ")
if comprueba_palindromo(cadena):
    print("¡Enhorabuena! La frase introducida es un palíndromo")
else:
    print("La frase introducida NO es un palíndromo")
