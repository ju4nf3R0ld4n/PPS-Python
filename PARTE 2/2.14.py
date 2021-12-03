print('Escribe un numero binario:')
q=input()
def bin_ent(bin):
    res=0
    g=len(bin)
    for x in range(len(bin)):
        res +=pow(2,x)*int(bin[g-x-1]) #inversa para empezar por la izq y no por dcha
    return (res)
print(f'El entero es {bin_ent(q)}')
