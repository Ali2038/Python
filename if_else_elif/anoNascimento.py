dataNascimento = int(input("Data de nascimento: "))
nome = input("Nome: ")
anoAtual = 2025

calculoNascimento = anoAtual - dataNascimento

if calculoNascimento >= 16:
    print("Pode votar.", "\nNome:", nome , "\nAno de nascimento: ", dataNascimento, "\nIdade: ", calculoNascimento)
else:
    print("Não pode votar.", "\nNome:", nome , "\nAno de nascimento: ", dataNascimento, "\nIdade: ", calculoNascimento)