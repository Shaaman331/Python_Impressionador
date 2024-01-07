"""
Calcule o percentual da lista de Vendedores
"""
meta = 10000
vendas = {
    "Joao" : [1500, 1300],
    "Julia": [2700, 4500],
    "Maria": [2000, 800],
    "Pedro": [900, 700],
    "Ana" : [10300, 5000],
    "Alon" : [7800, 5250],
}

def calculo_meta(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
        bateram_meta.append((vendedor, vendas[vendedor]))
    perc_meta = len(bateram_meta) / len(vendas)
    return bateram_meta, perc_meta
    
print("Vendedores que atingiram a Meta: ",calculo_meta(1000, vendas))

p_meta, vendedores_acima_meta = calculo_meta(meta, vendas)
print(p_meta)
print(vendedores_acima_meta)

print()
#Codigo optmizado 
def vendas_acima_meta(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
        if sum(vendas[vendedor]) > meta:
            bateram_meta.append((vendedor, vendas[vendedor]))
    return bateram_meta

def calculo_meta(meta, vendas):
    bateram_meta = vendas_acima_meta(meta, vendas)
    perc_meta = len(bateram_meta) / len(vendas)
    return bateram_meta, perc_meta

meta = 10000
vendas = {
    "Joao" : [1500, 1300],
    "Julia": [2700, 4500],
    "Maria": [2000, 800],
    "Pedro": [900, 700],
    "Ana" : [10300, 5000],
    "Alon" : [7800, 5250],
}

p_meta, vendedores_acima_meta = calculo_meta(meta, vendas)
print(p_meta)
print(vendedores_acima_meta)