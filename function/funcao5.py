def soma (vlr_um, vlr_dois):
    return vlr_um + vlr_dois

def subtracao (vlr_um, vlr_dois):
    return  vlr_um - vlr_dois

if __name__ == '__main__':
    vlr_inteiro_um = int(input("Primeiro valor: "))
    vlr_inteiro_dois = int(input("Segundo valor: "))

    print(" [-] soma", "\n [+] subração")
    escolha_menu = (input("Escolha: "))

    if  escolha_menu == "+":
        print("Soma: ", soma(vlr_inteiro_um, vlr_inteiro_dois))

    elif escolha_menu == "-":
        print("Subtração: ", subtracao(vlr_inteiro_um, vlr_inteiro_dois))

    else:
        print("Opção inválida")