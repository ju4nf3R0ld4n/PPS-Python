
def suma(lista):
    resultado =0
    num=len(lista)
    for x in range(num):
        resultado += lista[x]
    print(f'La suma de los número es:{resultado}')
def multiplicar(lista):
    resultado=1
    num=len(lista)
    for x in range(num):
        resultado *=lista[x]
    print(f'La multiplicación de los número es:{resultado}')
lista = [1,2,3,4]
suma(lista)
multiplicar(lista)