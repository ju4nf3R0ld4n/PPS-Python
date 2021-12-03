def superposicion(lista1,lista2):
    lon1=len(lista1)
    lon2=len(lista2)
    for x in range(lon1):
        for y in range (lon2):
            if lista1[x] == lista2[y]:
                print(f'Exite coincidencias en el numero {lista1[x]}')
lista1 = [1,2,3,4]
lista2 = [1,5,6,0]
superposicion(lista1,lista2)