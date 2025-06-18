precoCompra = float(input("Valor de compra: "))
precoVenda = float(input("Preço de venda: "))
nomeproduto = input("Nome do produto: ")

if precoVenda > precoCompra:
    print("Teve Lucro.", "Nome do produto: ", "\nNome do produto: ", nomeproduto, "\nValor venda: ", precoCompra, "\nValor compra: ", precoCompra)
elif precoVenda == precoCompra:
    print("Os valores são iguais.", "\nNome do produto: ", nomeproduto, "\nValor venda: ", precoCompra, "\nValor compra: ", precoCompra)
else:
    print("Teve prejuízo.", "Nome do produto: ", nomeproduto)