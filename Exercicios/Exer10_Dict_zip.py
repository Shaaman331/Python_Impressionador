"""
Transforme lista em dicionarios usando zip
"""

produtos = ["iphone", "sansung galaxy", "ipad", "notebook asus", "notebook dell", "ps5"]
vendas_2019 = [ 5001, 1304, 3500, 4500, 3450]
vendas_2020 = [ 3440, 4500, 6000, 1345, 6000]

# Usando o zip para criar um dicionario com os produtos como chaves e as vendas de 2019 e 2020
print("Dicionario de vendas")
vendas = list(zip(vendas_2019, vendas_2020))
print(vendas)
print()

# Usamos o dict zip  para cria um dicionario com a lista de  produtos e  vendas
print("Dicionario de produtos e vendas")
dicionario_de_vendas = dict(zip(produtos, vendas))
print(dicionario_de_vendas)


