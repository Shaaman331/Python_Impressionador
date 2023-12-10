print("Alteracoes Incrementais")
lista = ["mac", "iphone"]
vendas = [100, 200]
lista = lista + ["Ipad"]
print(f"Lista de produtos: {lista}")    
soma_vendas = 300
print(f"Soma de vendas: {soma_vendas}")
soma_vendas = soma_vendas + 500
print(f"Nova Soma de Vendas: {soma_vendas}")    

print("Copiando listas")
copia_lista = lista.copy()
print(f"Cópia da lista: {copia_lista}")
lista[1] = "iphone 11" 
lista2 = lista.copy()
print("Mudanças na cópia")  
print(lista2)

