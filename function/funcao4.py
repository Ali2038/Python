def soma (vlr_um, vlr_dois):
    return vlr_um + vlr_dois

def subtracao (vlr_um, vlr_dois):
    return  vlr_um - vlr_dois

if __name__ == '__main__':
    vlr_inteiro_um = int(input("Primeiro valor: "))
    vlr_inteiro_dois = int(input("Segundo valor: "))

    print("Soma = ", soma(vlr_inteiro_um , vlr_inteiro_dois), "Subtração: ", subtracao(vlr_inteiro_um, vlr_inteiro_dois))