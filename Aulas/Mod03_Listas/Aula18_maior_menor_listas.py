print('Tamanho da lista')
produtos = ['apple tv','mac','iphone x','Ipad','apple watch','mac book','airpods']

tamanho = len(produtos)
print (f'Temos {tamanho} produtos')    

vendas = [1000, 1500, 15000, 270, 900, 100, 1200]
total_de_vendas= sum(vendas) # soma todos os valores de uma lista.  
print ('Total de vendas: ', total_de_vendas)    
mais_vendidos = max(vendas)
menos_vendidos = min(vendas)
media_de_vendas = sum(vendas)/len(vendas)   
i =produto_mais_vendido = vendas.index(mais_vendidos)
produto_mais_vendido = produtos[i]

i = vendas.index(menos_vendidos)
produto_menos_vendido = produtos[i] 

print(f'O produto menos vendido é {produto_menos_vendido}')
print(f'O produto mais vendido é o {produto_mais_vendido}')
print(f'A média de vendas é {media_de_vendas}')
print(f'O máximo de vendas é {mais_vendidos}')
print(f'O minimo de vendas é {menos_vendidos}')