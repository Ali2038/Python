def calcula_dobro ():
    dobro = valor * 2
    return dobro

def calcula_triplo ():
    triplo = valor * 3
    return  triplo

if __name__ == '__main__':
    valor = int(input("Valor inteiro: "))

    print("Valor do dobro: ", calcula_dobro())
    print("Valor do triplo: ", calcula_triplo())