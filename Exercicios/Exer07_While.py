print("Lista de produtos")
vendas = []

while True: # Criando loop infinito
    produto = input("Digite o produto: ")
    if not produto: #Se nao tiver produto break
        break
    qtde = int(input("Digite a quantidade: "))  
    vendas.append([produto, qtde])
    
print(vendas)


      
