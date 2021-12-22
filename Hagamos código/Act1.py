def inversa (cadena):
    x = len(cadena)
    resultado = ""
    h = x
    for y in range(x):
        resultado += cadena[h-y-1]
    return resultado

def es_palindromo(cadena):
    reves=inversa (cadena)
    if reves==cadena:
        print(f"La palabra: {cadena} es un palíndromo")
    else:
        print(f"La palabra: {cadena} no es un palíndromo")

es_palindromo("radaor")

