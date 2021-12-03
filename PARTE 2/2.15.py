lista_edad=(18,10,24,70,37,20)
def edades(lista_edad):
    cont=0
    for x in lista_edad:
        if x > 20:
            cont +=1
    return (cont)
print(f'Existen {len(lista_edad)} usuarios de los cuales {edades(lista_edad)} mayores de 20 años.')