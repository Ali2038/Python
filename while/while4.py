menorValor = 999999999999
qtdValoresDigitados = 0
somaValoresDigitados = 0
while True:
    valor = int(input("Digite o valor: "))
    if valor == 0:
        break
    qtdValoresDigitados += 1
    somaValoresDigitados += valor
    if valor < menorValor:
        menorValor = valor
print("\nO menor valor é: ", menorValor)
print("\nQuantidade de valores digitados: ", qtdValoresDigitados)
print("\nSoma dos valores digitados: ", somaValoresDigitados)
print(f"\nMédia dos valores digitados: {somaValoresDigitados/qtdValoresDigitados: .2f}")