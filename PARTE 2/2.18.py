print('Qué año quieres saber...')
ano=int(input())
def es_bisiesto(ano):
    cont_4 = ano%4
    cont_100 = ano%100
    if cont_4 == 0 and cont_100 != 0:
        print(f'El año {ano} es bisiesto')
    else:
        print(f'El año {ano} no es bisiesto')
es_bisiesto(ano)