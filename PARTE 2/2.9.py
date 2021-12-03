def generar_n_caracteres(num,carac):
    contador =""
    for z in range(num):
        contador +=carac
    print(contador)
def procedimiento(lista):
    for a in range(len(lista)):
        generar_n_caracteres(lista[a],'*')

lista=[1,2,3,4,5,6]
procedimiento(lista)