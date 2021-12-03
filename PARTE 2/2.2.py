def max_de_tres(num1,num2,num3):
    if num1 > num2 & num1 > num3:
        print(f'{num1} es mayor que {num2} y que {num3}')
    elif num2 > num1 & num2 > num3:
        print(f'{num2} es mayor que {num3} y que {num1}')
    elif num3 > num1 & num3 < num2:
        print(f'{num3} es mayor que {num2} y que {num1}')
    else:
        print('ERROR')
print('Escribe el primer número')
num1=int(input())
print('Escribe el segundo número')
num2=int(input())
print('Escribe el tercer número')
num3=int(input())
max_de_tres(num1, num2, num3)