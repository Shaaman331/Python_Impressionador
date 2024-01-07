"""
Funcao para criar calcular a carga tributaria do produto
"""

preco = 1500
custo = 400
lucro = 800
def carga_tributaria (preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco 

print(f'A carga tributária é de {carga_tributaria(preco, custo, lucro)}')

print()

#Calculo de imposto com aliquota

print()

def carga_tributaria(preco, custo, lucro, aliquota_ipi=0.045, aliquota_pis=0.0065, aliquota_cofins=0.0065):
    margem_lucrativa = preco - custo
    tributacao = margem_lucrativa * aliquota_ipi
    tributacao += margem_lucrativa * aliquota_pis
    tributacao += margem_lucrativa * aliquota_cofins
    return tributacao

preco = 2500
custo = 1800
lucro = 700

print(f'A carga tributária é de {carga_tributaria(preco, custo, lucro)}')

