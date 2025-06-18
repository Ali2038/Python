def conversao (horas, minutos):
    return (horas * 60) + minutos

if __name__ == '__main__':
    entrada_horas = int(input("Horas: "))
    entrada_minutos = int(input("Minutos: "))

    print("Conversão em minutos: ", conversao(entrada_horas, entrada_minutos))