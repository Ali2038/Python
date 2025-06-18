vlrInicial = int(input("Valor inicial: "))
vlrFinal = int(input("Valor final: "))
ctd = 0
soma = 0

for i in range (vlrInicial, vlrFinal + 1, 1):
    print(i)
    ctd += 1
    soma += i

print("Quantidade de números gerados: ", ctd)
print("Soma dos números da sequência: ", soma)