def cuenta(cadena):
    contador = 0
    while cadena[contador:]:
        contador += 1
    return  contador

frase = 'Python es un lenguaje de programacion chungo'
print(cuenta(frase))
