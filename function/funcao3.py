
def soma_valores (vlr1, vlr2):
    soma = vlr1 + vlr2 # ou valor_soma_1 + valor_soma_2, não sendo necessário passar os parâmetros
    return soma

def retorna_soma_2 (vlr1, vlr2): # sem usar soma
    return vlr1 + vlr2

def mostra_soma (vlr1, vlr2): # sem o return
    print("Soma: ", vlr1 + vlr2)

if __name__ == '__main__':
    valor_soma_1 = int(input("Primeiro valor: "))
    valor_soma_2 = int(input("Segundo valor: "))

    print("Resultado da soma: ", soma_valores(valor_soma_1, valor_soma_2))

    print("Soma de valores reais: ", soma_valores(2.1, 5.3)) # passando diretamente, sem variáveis

    print("Soma sem a variável soma: ", retorna_soma_2(2,5)) # retornando sem usar a variável soma

    mostra_soma(valor_soma_1, valor_soma_2)