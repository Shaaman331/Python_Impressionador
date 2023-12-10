produto = input('Qual o nome do produto? ')
categoria = input('Qual a categoria do produto? ')
qtde = int(input('Qual a quantidade atual do produto ? '))

if produto and categoria and qtde:
    if categoria == 'bebidas':
        if qtde < 75:
            print('Solicitar {} á equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
    elif categoria == 'limpeza':
        if qtde < 30:
            print('Solicitar {} a equipe de compras,temos apenas {} unidades em estoque'.format(produto, qtde))
    else:
        if qtde < 50:
            print('Solicitar {} a equipe de compras,temos apenas {} unidades em estoque'.format(produto, qtde))

else:
    print('Preencha todas as informacoes')
