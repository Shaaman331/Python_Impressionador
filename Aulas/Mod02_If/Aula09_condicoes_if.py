"""
Condições no Python -> if
Estruturas 
Uso simples
if condição:
    o que faze caso seja verdadeira
    
"""
print("Condição if")
meta = 50000
qtd_vendida = 65300

if qtd_vendida > meta:
    print("Batemos a meta de vendas do Iphone, vendemos {} unidades.".format(qtd_vendida))

print()

print("Condição if else")
meta = 50000
qtd_vendida = 65300
if qtd_vendida > meta:
    print("Batemos a meta de vendas de Iphone, vendemos {} unidades.".format(qtd_vendida))
else:
    print("Infelizmente não batemos a meta. vendemos {} unidades. A meta era de {} unidades.".format())