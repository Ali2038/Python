ct = 0
soma = 0
print("Digite [-1] para sair da repetição")
disciplina = input("Nome da disciplina: ")
while True:
    nota = float(input("Digite a nota: "))
    if nota == -1:
        break
    ct += 1
    soma = soma + nota
print("Notas digitadas: ", ct)
print("Soma das notas: ", soma)
print(f"Média das notas: {soma/ct:.2f}")
print("Disciplina: ", disciplina)