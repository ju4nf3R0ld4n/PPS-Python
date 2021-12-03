def filtrar_palabras(lista,num):
    resultado=""
    for x in range(len(lista)):
        if num <= len(lista[x]):
            resultado+=lista[x]
            resultado+=", "
    print(f'Las palabras con {num} o más son {resultado}')
lista=['pollo','Real','Esternocleidomastoideo', 'Ciberseguridad']

filtrar_palabras(lista,6)