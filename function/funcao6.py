def maior_numero (vlr_um, vlr_dois):

    if vlr_um >= vlr_dois:
        maior_valor = vlr_um
    else:
        maior_valor = vlr_dois

    return maior_valor


if __name__ == '__main__':
    inteiro_um = int(input("Primeiro valor: "))
    inteiro_dois = int(input("Segundo valor: "))

    print("Maior valor: ", maior_numero(inteiro_um, inteiro_dois))