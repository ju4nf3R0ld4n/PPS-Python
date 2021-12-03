print('Señor usuario, escribe una frase')
cadena=input()
def mayus(cadena):
    res=0
    for x in range(len(cadena)):
        h=cadena[x]
        if h.isupper():
            res += 1
    print(f'Esta frase tiene {res} letras mayúsculas.')
mayus(cadena)

