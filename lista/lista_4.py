notas = []
aprovados = 0
print("Digite [0] para sair.")
while True:
    entrada = float(input("Nota: "))
    if entrada == 0:
        break
    else:
        notas.append(entrada)

print("Média aritmética: ", sum(notas)/len(notas))
print("Maior nota: ", max(notas))

for item in notas:
    if item >=5:
        aprovados += 1
print("Total aprovados: ", aprovados)

print("\nLista na ordem vertical: ")
for item in notas:
    print(item)


