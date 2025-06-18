ctd = 0
soma = 0
nmrPar = 0
nmrDigitados = 0
print("Digite {0} para sair: ")

while True:
    nmrPar = int(input("Digite um número par: "))
    if nmrPar == 0:
        break
    elif nmrPar % 2 == 0:
        ctd += 1
        soma = nmrPar + soma
    else:
        print("O número tem que ser par!")
    nmrDigitados += 1

print(f"Média dos números: {soma/ctd: .4f}")
print("Números pares: ", ctd)
print("Números Digitados: ", nmrDigitados)
