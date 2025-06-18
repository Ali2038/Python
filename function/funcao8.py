def calcula_idade (ano):
    return 2025 - ano

if __name__ == '__main__':
    ano = int(input("Nascimento: "))
    print("Idade: ", calcula_idade(ano))