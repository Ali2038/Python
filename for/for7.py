vlrInicial = int(input("Valor inicial: "))
vlrFinal = int(input("Valor final: "))
ctd = 0
soma = 0

# ordem crescente
if vlrInicial < vlrFinal:
    for i in range(vlrInicial, vlrFinal + 1, 1):
        print(i)
        ctd += 1
        soma += i
    print("Valores em ordem crescente.")

elif vlrInicial > vlrFinal:
    # ordem decrescente
    for i in range(vlrInicial, vlrFinal - 1, -1):
        print(i)
        ctd += 1
        soma += i
    print("Valores em ordem decrescente.")

else:
    print("Os valores são iguais!")

print("Quantidade de números gerados: ", ctd)
print("Soma dos números da sequência: ", soma)
