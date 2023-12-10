("Calculando  Listas ")
meta = 10000
vendas = [
    ["Joao", 15000],
    ["Julia", 27000],
    ["Marcus", 9900],
    ["Maria", 3750],
    ["Ana", 10300],
    ["Alon", 7870],
]

print()
print("Calculando o total de vendas")
acima_meta = [] #Criando  variavel auxiliar
for venda in vendas:    
    if venda[1] > meta: 
        acima_meta.append(venda)
print(acima_meta)
print(f"{len(acima_meta) / len(vendas):.1%} dos vendedores bateram a meta")

print()
print("Calculando o total de vendas acima da meta")    
qtde_vendedores_acima = 0

for venda in acima_meta:
    if venda[1] >= meta:
        qtde_vendedores_acima += 1
print(f"{(qtde_vendedores_acima) / len(vendas):.1%} dos vendedores bateram a meta")

print()
print("Calculando o melhor vendedor")
melhor_vendedor = ""
maior_vendas = 0
for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]
print(f"O melhor vendedor foi {melhor_vendedor} com {maior_vendas} vendas.")

