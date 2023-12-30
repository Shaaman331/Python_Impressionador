"""
Iterable 
É uma estrutura que armazena dados que pode ser "iterada", ou seja que podemos fazer um for 
dentro dele e ir passando item a item. É como se fosse um tipo de lista onde se pode olhar
cada um dos elementos
"""
produtos = ["iphone","sansung galaxy","tv sansung","ps5","tablet","ipad","tv lg","notebook hp","notebook dell"]
for produto in produtos:
    print(produto)
print()

texto = "luca@gmail.com"
# Iterável é composta por letras, vamos separar as letras em itens da iterável
separador_de_letras = ""
for ch in texto:
    print(ch)

vendas_produtos = {"iphone": 15000,"sansung galaxy": 12000,"tv sansung": 10000,"ps5": 14300,"tablet": 1720,"ipad": 1000,"tv lg": 2500,"notebook hp": 1000,"notebook dell": 17000}

for produto in vendas_produtos:
    print("{}: {} unidades".format(produto, vendas_produtos[produto]))


#Range
def adicionar_produto(produtos, estoque):
    if produtos not in produtos_estoque:
        produtos_estoque[produtos] = estoque
    else:
        produtos_estoque[produtos] += estoque

produtos_estoque = {}

produtos = input("Digite o produto: ")
estoque = int(input("Digite a quantidade do estoque: "))
adicionar_produto(produtos, estoque)

for produto, quantidade in produtos_estoque.items():
    print("{}: {} unidades em estoque".format(produto, quantidade))

produtos = ["arroz","feijao","macarrao","atum","azeite"]
estoque = [50, 100, 20, 5, 80]

for i in range(5):
    print("{} tem {} unidades no estoque".format(produtos[i], estoque[i]))

print()

print(range(1 , 10))
for x in range(2, 10):
    print(x)

print("Classificacao de funcionarios")
funcionarios = ["Maria", "Jose","Antonio","Francisco","Ana","Luiz","Paulo","Carlos","Manoel","Pedro","Francisco"]
vendas = [2750, 1900, 500, 1200, 1111, 999, 990, 880, 800, 450, 400, 300, 300, 120, 90, 80, 70]
print("Funcionarios Classe B")
for i in range(3, 7):
    print("{}: fez {} vendas".format(funcionarios[i], vendas[i]))


