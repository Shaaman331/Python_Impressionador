"""
Transformando Listas em Dicionarios com metodo zip
Estrutura:
* Dicionário com valores padroes:
dicionario = dict.fromkeys(lista_chaves, valor_padrao)

* Dicionario a partir de listas de tuplas:
dicionario = dict(lista_tuplas)

* Transformar uma lista em um dicionário usando o método zip e os indices das 
listas:

Passo 1: Transformar lista em lista de tuplas com o metodo Zip
Passo 2: Transformar em dicionario

lista_tuplas = zip(lista_1, lista_2) dicionario = dict(lista_tuplas)

"""

produtos = ["iphone","sansung galaxy","tv sansung","ps5","tablet","ipad","tv philco","notebook hp","notebook dell","notebok asus",]
vendas = [1500, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450 ]

#Usando metodo zip 
lista_tuplas = list(zip(produtos, vendas))
print("\nLista de Tuplas: ", lista_tuplas)

#Transformando lista de tuplas em dicionario
dicionario_de_vendas = dict(lista_tuplas)
print("\nDicionario de Vendas:", dicionario_de_vendas)
print()

#Acessando os dados do dicionario
print("Dicionario gerado pelo laco for")
for chave in dicionario_de_vendas:
    print(f"O produto {chave} foi vendido por R$: {dicionario_de_vendas[chave]}")


#Transformando lista de tuplas em dicionario

dicionario = dict(lista_tuplas)
print("\nDicionario gerado pela lista de Tuplas: \n", dicionario_de_vendas)

#Acessando dados pelo indice
print("\nAcessando pelo indice")
indice = produtos.index("ipad")
print(f"Venda do iPad é R$ {vendas[indice]}")

#Acessando dados pelo dicionario
print("\nAcessando pelo dicionario")
print(f"Venda do Ipad é R$ {dicionario_de_vendas['ipad']}")
