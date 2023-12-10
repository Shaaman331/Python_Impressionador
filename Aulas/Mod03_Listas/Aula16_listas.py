produtos = ['tv', 'celular','mouse','teclado','geladeira','forno','tablet']

estoque = [1000, 1500, 350, 270, 900, 540, 200]

print('Vendas do produto {} foram de {} unidades'.format(produtos[3], estoque[3]))

i = produtos.index('geladeira')
qtde_estoque = estoque[i]

print('Quantidade em estoque da geladeira é de:{}'.format(qtde_estoque))

produto = input('Insira o nome do produto: ')
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque'.format(qtde_estoque, produto))
else:
    print('{}produto nao encontrado!'.format(produto))
