def max_in_list(lista):
    resultado=0
    for x in range(len(lista)):
        if resultado < lista[x]:
            resultado=lista[x]
    print(f'el valor de la lista más alto es {resultado}')

lista=[1,999,20,55]
max_in_list(lista)