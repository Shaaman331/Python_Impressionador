print("Analise de vendas")
meta = 1000
vendas = [("Joao", 15000),
          ("Julia", 27000),
          ("Marcus", 9900),
          ("Maria", 3750),
          ("Ana", 10300),
          ("Alon", 7870),] 

for vendedor, qtde in vendas: #criando unpacked de tuplas
    if qtde >= meta:
        print(f"O {vendedor} bateu a meta, vendeu{meta} unidades")


print("\nCrescimento de vendas")
vendas_produtos = [("iphone", 558147, 951642),("galaxy", 712350, 244295),("ipad",553823, 26966),
                   ("tv", 405252, 787604), 
                   ]


for produto, vendas2020, vendas2019 in vendas_produtos:
    if vendas2020 > vendas2019:
        crescimento = vendas2020 / vendas2019 - 1
        print(f"O  produto {produto} teve  {vendas2019} vendas em 2019.E {vendas2020} vendas em 2020. Creescimento de {crescimento:.1%}")
