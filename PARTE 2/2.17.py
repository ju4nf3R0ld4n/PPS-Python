print('Escribre una palabra y te cuento cada vocal broh!')
palabra=input()
def contar_vocales(palabra):
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0
    for x in palabra:
        if x == 'a':
            cont_a += 1
        elif x == 'e':
            cont_e += 1
        elif x == 'i':
            cont_i += 1
        elif x == 'o':
            cont_o += 1
        elif x == 'u':
            cont_u += 1
    print(f'A={cont_a}, E={cont_e}, I={cont_i}, O={cont_o}, U={cont_u}' )
contar_vocales(palabra)
