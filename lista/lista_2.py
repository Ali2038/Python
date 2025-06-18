notas = list()

while True:
    nota = float(input("Digite a nota ou [-1] para sair: "))

    if nota == -1:
        break
    else:
        notas.append(nota)

print(f"Média aritmética: {sum(notas)/len(notas):.2f}")
print("Quantidade de alunos: ", len(notas))
print("\nLista na horizontal: ", notas)
print("Lista na vertical: ")
for item in notas:
    print(item)