print("Estrura While")
# Exemplo 1:
print("Registro de produtos")
venda = input("Registre um produto. Para cancelar o de registro de um novo, aperte enter com caixa vazia: ")
vendas = []
while venda != "":
    vendas.append(venda)    
    venda = input("Registre um produto. Para cancelar o de registro de um novo, aperte enter com caixa vazia: ")

print("\nRegistro Finalizado. As vendas cadastradas foram: {}".format(vendas)) 


# Exemplo 2:    
n = int(input("Digite um número: "))
c = 0
while n != 0:
    n -= 1
print()
# Exemplo 3:
vendas = [941, 852, 783, 714, 697, 689, 685, 670, 631, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ["Maria","Jose","Antonio","Joao","Francisco","Ana","Luiz","Paulo","Carlos","Manoel","Pedro","Francisca","Marcos","Raimundo","Sebastiao", "Antonia", "Marcelo", "Jorge", "Marcia", "Geraldo", "Adriana"]
meta = 100
i = 0 # indice de vendedores

while vendas[i] > meta:
    print(f"{vendedores[i]} bateu a meta. Vendas: {vendas[i]} ")
    i += 1 # incrementacao para interromper o loop infinito
    