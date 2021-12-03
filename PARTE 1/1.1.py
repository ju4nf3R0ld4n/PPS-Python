print('¿Cual es tu calificación?')
nota =float(input())
if nota <=10 and nota>=9:
    print('A')
elif nota <=9 and nota>=8:
    print('B')
elif nota <=8 and nota>=7:
    print('C')
elif nota <=7 and nota>=6:
    print('D')
elif nota <=6 and nota>=0:
    print('F')
else:
    print('Valor desconocido')
