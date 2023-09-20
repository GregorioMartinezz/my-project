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


# Esto primero son test para comprobar que funciona adecuadamente
assert comprueba_palindromo("dabale arroz a la zorra el abad")
assert comprueba_palindromo("yo hago yoga hoy")
assert comprueba_palindromo("lol")
assert not comprueba_palindromo("abcde")
# Esto es el programa que pregunta la frase y comprueba
cadena = input("Introduzca una frase: ")
if comprueba_palindromo(cadena):
    print("¡Enhorabuena! La frase introducida es un palíndromo")
else:
    print("La frase introducida NO es un palíndromo")
