def mostrar_valor(p_valor):
    print("Parâmetro recebido: ", p_valor)

def mostrar_dois_valores(vlr_um, vlr_dois):
    print("Parâmetros recebidos: ", vlr_um, vlr_dois)

if __name__ == '__main__':
    mostrar_valor(5)
    mostrar_valor(28.5)
    mostrar_valor(-55)

    print("\nSegunda forma de fazer (Com variáveis, sem input)")
    v_positivo = 20
    mostrar_valor(v_positivo)
    nmr_real = 54.50
    mostrar_valor(nmr_real)
    v_negativo = -100
    mostrar_valor(v_negativo)

    print("\nUtilizando dois valores")
    mostrar_dois_valores(5, 10)