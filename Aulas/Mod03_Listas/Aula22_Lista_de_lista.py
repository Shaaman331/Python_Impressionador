print("Listas de Listas")
vendedores = ["Lucca", "Marcos","Gabriel"]
produtos = ["ipad","iphone", "airdots"]
vendas = [
    [100, 2500],
    [200, 5000],
    [50, 6000],
    [90, 1500 ]

]  

vendas_ipad_lucca = vendas[0][1]
vendas_marcos = vendas [1][1]
vendedor_gabriel = vendas[2][1]
print(f"O vendedor {vendedores[0]} vendeu {vendas[0][0]} ipad com o preco: R$ {vendas_ipad_lucca}")
print(f"O vendedor {vendedores[1]} vendeu {vendas[1][0]} iphone com o preco: R$ {vendas_marcos}")
print(f"O vendedor {vendedores[2]} vendeu {vendas[2][0]} airdots com o preco: R$ {vendedor_gabriel}")   
