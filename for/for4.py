somaSequencia = 0
contador = 0
for i in range (7,-1,-1):
    print(i)
    contador += 1
    somaSequencia += i
print("Quantidade: ", contador)
print("Soma: ", somaSequencia)
print("Média aritmética: ", somaSequencia/contador)