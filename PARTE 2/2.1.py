def max(num1,num2):
    if num1 > num2:
        print(f'{num1} es mayor que {num2}')
    elif num1 == num2:
        print(f'{num1} es igual que {num2}')
    else:
        print(f'{num1} es menor que {num2}')
print('Escribre primer número')
num1=int(input())
print(f'Escribre segundo número')
num2=int(input())
max(num1,num2)
