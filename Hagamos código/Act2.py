import random
num=random.randrange(10)
resultado = False
while resultado == False:
    print("Di un número:")
    num2 = int(input())
    if num==num2:
        print(f"Adivinaste el número es:{num}")
        resultado=True
    else:
        print("No adivinaste el número, sigue intentándolo")
        if num > num2:
            print("El número es mayor")
        else:
            print("El número es menor")