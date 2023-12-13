print("Tuplas")
# Tuplas sao estruturas que acessam variaveis, porem sao imutaveis
# Tuplas sao usadas para guardar varios valores em uma unica variavel
#Vantagens - Mais eficiente (em termos de performace)
#          - Protege a base de dados(por ser imutavel)
#          - Muito usada para dados heterogeneos

vendas = ("Lucca", "01/12/2020", "03/02/1990", 2000,"Estagiario")
print(vendas)

# Acessando os valores da tupla 
nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]
print(nome , data_contratacao, data_nascimento, salario, cargo)


#Usando o enumarete para acessar valores da tupla
vendas = [1000, 2000, 300, 300, 150]
funcionarios = ["Joao","Lucas","Ana","Maria", "Paula"]
for i, venda in enumerate(vendas):
    print(f"O funcionario(a) {funcionarios[i]} vendeu {venda} unidades")

#TUPLA COMPOSTA - Uma tupla pode conter outras tuplas.  
vendas = [("20/08/2020","iphone x","azul","128 gb", 350, 4000),
          ("20/08/2020","iphone x","prata","256 gb", 1500, 4000),
          ("20/08/2020","ipdad","prata","256 gb", 127, 6000),
          ("21/08/2020","ipad","prata","128gb", 981, 5000),
          ("21/08/2020","iphone x","azul","128 gb", 397, 6000),
          ("21/08/2020","iphone x","prata","128 gb",1017, 4000),
          ("21/08/2020","ipad","prata","256 gb", 50, 6000),
          ("21/08/2020","ipad","prata","128 gb", 4000, 5000),

          ]


faturamento = 0 #criacao de  variavel auxilar (incrementando valor)
for item in vendas:
    data, produto, cor, armazenamento, unidades, valor_unitario = item
    if produto == "iphone x" and data == "20/08/2020":
        faturamento += unidades * valor_unitario
        print(f"\nFaturamento do IPhone X: R$ {faturamento}")


print("\nLista de produtos mais vendidos")
produtos_mais_vendidos = "" # criacao de variavel auxiliar
qtde_produtos_mais_vendidos = 0 #criacao de variavel auxilar(incrementando valor)
cor_produto_mais_vendido = ""
capacidade_produto_mais_vendido = ""
for item in vendas:
    data, produto, cor, armazenamento, unidades, valor_unitario = item
    if data == "21/08/2020":
        if unidades > qtde_produtos_mais_vendidos:
            produtos_mais_vendidos = produto
            qtde_produtos_mais_vendidas = unidades
            cor_produto_mais_vendido = cor
            capacidade_produto_mais_vendido = armazenamento
print(f"O produto mais vendido no dia 21/08/2020 foi {produto} com {qtde_produtos_mais_vendidas} unidades. Cor: {cor_produto_mais_vendido} e capadicidade: {capacidade_produto_mais_vendido}")
