def mas_larga(cadena):
    resultado=cadena[0]
    for x in range(len(cadena)):
        if len(resultado) < len(cadena[x]):
            resultado=cadena[x]
    print(f'La palabra de la lista más larga es {resultado}')
cadena=['pollo','Real','Esternocleidomastoideo', 'Ciberseguridad']
mas_larga(cadena)