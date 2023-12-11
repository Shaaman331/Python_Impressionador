print("Formas de interromper um for")
# Exemplo 1:    
vendas = [100, 150, 1500, 2000, 120]
meta = 110
vendedores = ["Joao", "Julia", "Ana", "Jose", "Maria"]
for venda in vendas:
    if venda < meta:
        print("A loja nao ganha bonus")
        break
    else:   
        print("A loja ganha bonus")

print()
for venda in vendas:
    if venda < meta:
        continue
    print(venda)

print()

# Exemplo 2:
for vendedor in vendedores:
    if vendedor == "Ana":
        break
    print(vendedor)
    print()
    