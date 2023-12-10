produtos = ['apple tv', 'mac','iphone','apple watch','mac book ','airpods']
#adicionar produto
produtos.append('iphone 11')
print(produtos)
#remover produto    
remover_produto = 'iphone x'
if remover_produto in produtos:
    produtos.remove('iphone x') 
else:
    print('{} nao exite na lista de produtos'.format(remover_produto))
try:
    produtos.remove('iphone 8') #se o item não existir, vai dar erro e passar para except   
    print(produtos)
except:
    print("O item {} nao existe".format(remover_produto))

