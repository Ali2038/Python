numero = float(input("Digite o número: "))

if numero < 0:
    print("Número negativo.", "Número: ", numero, "Dobro: ", numero *2)
elif numero > 0:
    print("Número positivo.", "Número: ", numero, "Dobro: ", numero *2)
else:
    print("Número nulo.", "Número: ", numero, "Dobro: ")