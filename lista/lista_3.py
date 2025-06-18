from tls.tls_csv2SUMO import index

valores = list()

while True:
    entrada_valor = int(input("Digite o valor ou [0] para sair: "))
    if entrada_valor == 0:
        break
    else:
        valores.append(entrada_valor)

valores.sort()

print("Menor valor da lista: ", valores[0])
print("Maior item da lista: ", valores[-1])
print("\nLista na ordem horizontal: ", valores)
print("Lista na vertical: ")
for item in valores:
    print(item)