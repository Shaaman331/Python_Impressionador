"""
Crie um programa que imprima(print) os principais indicadores da loja Hashtag&Drink
no ultimo ano.

Valores do ultimo ano:
Quantidade de Vendas de Coca = 150
Quantidade de Vendas de Pepsi = 130
Preço Unitário da Coca = 1,50
Preço Unitário da Pepsi = 1,50
Custo da loja 2.500.00
"""
qtd_pepsi = 130
qtd_coca = 150
preco_pepsi = 1.50
preco_coca = 1.50
custo = 2500

#Qual o faturamento da Pepsi da loja?
print(qtd_pepsi * preco_pepsi)

#Qual o faruramento da Coca da loja ?
print(qtd_coca * preco_coca)

#Qual foi o lucro da loja ?
faturamento = qtd_coca * preco_coca + qtd_pepsi * preco_pepsi
lucro = faturamento - custo
print(faturamento)
print(lucro)

#Qual foi a margem da loja ?
print(lucro / faturamento)

#Execicio 2

codigo = input("Qual é o codigo da bebida?(insira em letra maiuscula): ")
print("BAC" in codigo)

