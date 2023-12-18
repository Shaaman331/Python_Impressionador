"""
Metodos uteis em Dicionario
.items() -> retorna um par (chave, valor) de cada elemento no dicionário  
itens() dos dicionarios
itens_dicionario = dicionario.items()

for item in dicionario.items()
    cada item do dicionario em forma de tupla
"""

vendas_tecnologia = {"notebook asus":2450,"iphone":1500,"sansung galaxy":12000,"tv sansung": 10000,"tablet":1720,"ps5":14300,"notebook dell": 17000,"ipad": 1000,"notebook hp": 1000}

for item in vendas_tecnologia.items():
    print(item)  

print()
# Mostrando os itens como uma lista, sem serem tuplas
for produto, qtde in vendas_tecnologia.items():
    print(f'{produto} tem : {qtde} unidades.')  # Aqui estamos usando a desestrutura
print()

# Produto com vendas acima de 5000 unidades
    
for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000: 
        print(f'O produto {chave} foi vendido com mais de 5000 unidades!')
print()

for produto, qtde in vendas_tecnologia.items():
    if qtde > 5000:
        print(f'O {produto} vendeu: {qtde} unidades.') 
print()
