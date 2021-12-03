lista=['Antonio', 'alejandro', 'pepe','Adrian']
def list_nom(lista):
    cont=0
    for x in lista:
        if x[0] == 'a' or x[0] == 'A':
            cont +=1
    return(cont)
print(f'Existen {len(lista)} usuarios, {list_nom(lista)} empiezan por A.')
