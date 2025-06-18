ctdMasculino = 0
ctdFeminino = 0
maior = 0
menor = 3
somaAlturas = 0
print("[0] para sair da repetição")
while True:
    altura = float(input("Digite a altura: "))
    if altura == 0:
        break
    somaAlturas += altura
    genero = input("Digite o gênero [(m) masculino] ou [(f) feminino]: ")
    if genero == "m":
        ctdMasculino += 1
    else:
        ctdFeminino += 1
    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura

print("\nMaior altura do grupo: ", maior)
print("\nMenor altura do grupo: ", menor)
print("\nQuantidade de homens do grupo: ", ctdMasculino)
print("\nQuantidade de mulheres do grupo: ", ctdFeminino)
print("\nMédia das alturas: ", somaAlturas / (ctdFeminino + ctdMasculino))