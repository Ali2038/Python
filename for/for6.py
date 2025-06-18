soma = 0
ctd = 0

for i in range (0, 51, 1):
    soma += float(input("Digite a nota do aluno: "))
    ctd+= 1

print(f"Média aritmética: {soma/ctd: .2f}")