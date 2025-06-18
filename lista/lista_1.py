lista = []

while True:
    entrada = int(input("Digite o valor, [0] para sair ou [1] para pesquisar: "))

    if entrada == 0:
        break
    elif entrada == 1:
        nmr_pesquisar = int(input("Valor a buscar: "))
        if nmr_pesquisar in lista:
            print("O valor está na lista na posição: ", lista.index(nmr_pesquisar))
        else:
            print("O valor Não está na lista.")

    else:
        lista.append(entrada)

print("\nLista na horizontal: ", lista)

print("\nLista na vertical: ")
for item in lista:
    print(item)

print("\nQuantidade de elementos na lista: ", len(lista))
print("Soma dos valores na lista: ", sum(lista))
print("Maior valor: ", max(lista))
print("Menor valor: ", min(lista))

lista.insert(0, 33)

lista.sort()
print("Lista na ordem crescente: ", lista)

lista.reverse()
print("Lista na ordem decrescente: " , lista)

print("Média aritmética dos valores: ", sum(lista)/ len(lista))

maiores_que_dez = 0


for item in lista:
    if item >= 10:
        maiores_que_dez += 1

print("Quantidade de valores maiores que dez: ", maiores_que_dez)


print(f"Porcentagem dos números maiores que dez:{((maiores_que_dez/len(lista)) * 100):.2f} %")


lista.remove(33)