# if-elif-else

numero = int(input("Ingrese un numero por favor: "))

if numero % 2 == 0:
    print(f"{numero} es múltiplo de dos")
elif numero % 4 == 0:
    print(f"{numero} es múltiplo de cuatro y de dos")
else:
    print(f"{numero} no es múltiplo de dos")